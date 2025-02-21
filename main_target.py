# -*- coding: utf-8 -*-
import os
import pandas as pd
import time
import numpy as np
from pylab import *
import copy
import torch
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn import svm
from sklearn.metrics import mean_absolute_percentage_error
from utils import load_data, save_model
from train_test import train, predict
from network import Net, Target_Net
from ensemble import ensemble_arch
from feature import get_feature
from SVR_configuration import *

########## Set the direction of transfer learning ############
target = 'Moisture'
# source(from)
fac_source = 'A'
line_source = '2'
types_source = 'N'
# target(to)
fac = 'A'
line = '1'
types = 'N'

################## training parameter setting #########################
EPOCH = 20  # for Direct learning
EPOCH_transfer = 20  # for transfer learning
EPOCH_ensemble = 20  # for EDTL
learning_rate = 1e-3
proportion = [0.2, 0.4, 0.6, 0.8, 1.0]  # The proportion of data using
AverageTimes = 10  # conduct multiple experiments and average the performance to reduce variance

source_features = get_feature(line=f'{fac_source}{line_source}', type_=types_source, target=target)
features = get_feature(line=f'{fac}{line}', type_=types, target=target)

train_file = f'data/Factory{fac}/stenter{line}/training_{types}.csv'
test_file = f'data/Factory{fac}/stenter{line}/testing_{types}.csv'

models_list = ['Direct Learning', 'Transfer Learning', 'EDTL']

if __name__ == '__main__':
    # The save path of simulation result
    result_path = "./result/" + str(time.strftime("%m_%d_%H%M",
                                                  time.localtime()) + "(" + target + line_source + types_source + " to " + line + types + ")")
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    for i in range(AverageTimes):
        seed = 100 + i
        print(f'-' * 40 + f'Seed = {seed}' + f'-' * 40)

        # Load the source model's parameters
        model_source = Net(len(source_features))
        model_source.load_state_dict(torch.load(f"./pretrained_model/{target}{line_source}{types_source}.pkl"))

        # Load data
        x_train, y_train = load_data(features, target=target, file=train_file, seed=seed)
        x_test, y_test = load_data(features, target=target, file=test_file)

        # Data Normalization
        x_data = np.concatenate([x_train, x_test])
        scalar = MinMaxScaler()
        x_data = scalar.fit_transform(x_data)
        x_train = x_data[:len(x_train)]
        x_test = x_data[len(x_train):]

        score_of_model = dict()  # Use to log the performance of different method

        for name in models_list:
            print(f"  {name}")
            score_pro = []
            # used to log the performance of the trained model
            # under different proportions of training data

            for j, n in enumerate(proportion):
                print(f"    Use {n * 100}% data to training")
                num_sample = int(len(x_train) * n)
                np.random.seed(seed)
                sample_index = np.random.choice(len(x_train), num_sample, replace=False)
                x_train_sample = x_train[sample_index]
                y_train_sample = y_train[sample_index]

                estimator = None
                if name == 'Direct Learning':
                    torch.manual_seed(seed)
                    estimator = Net(x_train.shape[1])
                    train_model, score_history = train(x_train_sample, y_train_sample,
                                                       estimator,
                                                       EPOCHS=EPOCH,
                                                       lr=learning_rate,
                                                       verbose=False)

                    y_pred = predict(x_test, y_test, train_model)
                    score = mean_absolute_percentage_error(y_true=y_test, y_pred=y_pred)


                elif name == 'Transfer Learning':
                    torch.manual_seed(seed)
                    estimator = Target_Net(model_source, x_train.shape[1], model_source.fc1.in_features)
                    target_model, score_history = train(x_train_sample, y_train_sample,
                                                        estimator,
                                                        EPOCHS=EPOCH_transfer,
                                                        lr=learning_rate,
                                                        verbose=False)

                    y_pred = predict(x_test, y_test, target_model)
                    score = mean_absolute_percentage_error(y_true=y_test, y_pred=y_pred)

                elif name == 'EDTL':
                    torch.manual_seed(seed)
                    transfered_model = Target_Net(model_source, x_train.shape[1], model_source.fc1.in_features)
                    c = SVR_parameter[line_source + types_source + ' to '
                                      + line + types][target]['C']
                    eps = SVR_parameter[line_source + types_source + ' to '
                                        + line + types][target]['epsilon']

                    ''' Define meta-model '''
                    if type(eps) is list:
                        fusion_model = svm.SVR(C=c, epsilon=eps[j])
                    else:
                        fusion_model = svm.SVR(C=c, epsilon=eps)

                    ensemble_model = ensemble_arch(transfered_model, fusion_model)
                    estimator = ensemble_model
                    trained_fusion = estimator.fit(x_train_sample, y_train_sample,
                                                   lr=learning_rate,
                                                   epoch=EPOCH_ensemble)

                    _, y_pred = estimator.predict(x_test, y_test)
                    score = mean_absolute_percentage_error(y_true=y_test, y_pred=y_pred)

                score_pro.append(score * 100)

            score_of_model[name] = score_pro

        score_of_model_df = pd.DataFrame(score_of_model)

        # save the logging
        score_of_model_df.to_csv(f"{result_path}/result({seed}).csv", encoding="utf_8_sig")
