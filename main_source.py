import os
import time
import matplotlib.pyplot as plt
import torch
from pylab import *
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_absolute_percentage_error
from utils import load_data, save_model, plot_distribution
from train_test import train, predict
from network import Net
from feature import get_feature

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

''' Source model training, use the source domain dataset (A2, B) '''

### set training parameter ###
EPOCH = 30
target = 'Moisture'  # predicted target
fac = 'A'  # Factory
line = '2'  # production line
types = 'N'  # Fabric type. If use B production line data, set types is ""
train_file = f'data/Factory{fac}/stenter{line}/training_{types}.csv'
test_file = f'data/Factory{fac}/stenter{line}/testing_{types}.csv'
seed = 100  # random seed, control the randomness of neural network initialization
###############

features = get_feature(line=f'{fac}{line}', type_=types, target=target)
print(features)

if __name__ == '__main__':

    x_train, y_train = load_data(features, target=target, file=train_file, seed=seed)
    x_test, y_test = load_data(features, target=target, file=test_file, seed=seed)
    # Data Normalization
    x_data = np.concatenate([x_train, x_test])
    scalar = MinMaxScaler()
    x_data = scalar.fit_transform(x_data)
    x_train = x_data[:len(x_train)]
    x_test = x_data[len(x_train):]

    # neural network initialization
    torch.manual_seed(seed)
    model = Net(x_train.shape[1])

    # model training
    trained_model, score_history = train(x_train=x_train,
                                         y_train=y_train,
                                         model=model,
                                         EPOCHS=EPOCH)

    # save the parameters of pretrained model
    image_path = "./image/pretrain/" + str(time.strftime("%m_%d", time.localtime()) + "(" + target + line + types + ")")

    save_model(model=trained_model, name=f'{target}{line}{types}')

    threshold = 0

    pred = predict(x_test, y_test, trained_model)
    score = mean_absolute_percentage_error(y_true=y_test, y_pred=pred)
    plot_distribution(score=score,
                      y_test=y_test,
                      pred=pred,
                      types=types,
                      prodction_line=f'{fac}{line}',
                      target=target,
                      image_path=image_path)
