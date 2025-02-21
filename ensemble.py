# -*- coding: utf-8 -*-

import numpy as np
import copy
from sklearn.preprocessing import StandardScaler
from train_test import train, predict
from network import Net, Target_Net
from utils import split_data

''' Define ensemble model. Adopt stacking, an ensemble architecture
    to combine base model via a meta model'''

class ensemble_arch():
    def __init__(self, model_transfer, fusion_model):
        super(ensemble_arch, self).__init__()
        self.fusion_model = fusion_model  # meta-model
        self.model_transfer = model_transfer  # used to construct base-model set

    def level1_fit(self):
        ''' Train base model set. Each base-model inherits parameters from the source
            model and fine-tunes one layer parameters. '''
        num_hidden = 0
        for child in self.model_transfer.children():
            num_hidden += 1
            for param in child.parameters():
                param.requires_grad = False

        self.num_base_model = num_hidden
        self.base_modellist = []

        for i in range(int(self.num_base_model)):
            base_model = copy.deepcopy(self.model_transfer)

            if i == 0:
                base_model.fc0.weight.requires_grad = True
                base_model.fc0.bias.requires_grad = True
                base_model.fc1.weight.requires_grad = True
                base_model.fc1.bias.requires_grad = True
                # set "True" indicates that the network can compute gradients
            elif i == 1:
                base_model.fc0.weight.requires_grad = True
                base_model.fc0.bias.requires_grad = True
                base_model.fc2.weight.requires_grad = True
                base_model.fc2.bias.requires_grad = True

            elif i == 2:
                base_model.fc0.weight.requires_grad = True
                base_model.fc0.bias.requires_grad = True
                base_model.fc3.weight.requires_grad = True
                base_model.fc3.bias.requires_grad = True

            elif i == 3:
                base_model.fc0.weight.requires_grad = True
                base_model.fc0.bias.requires_grad = True
                base_model.fc4.weight.requires_grad = True
                base_model.fc4.bias.requires_grad = True

            elif i == 4:
                base_model.fc0.weight.requires_grad = True
                base_model.fc0.bias.requires_grad = True
                base_model.fc5.weight.requires_grad = True
                base_model.fc5.bias.requires_grad = True

            elif i == 5:
                for child in base_model.children():
                    for param in child.parameters():
                        param.requires_grad = True

            trained_base_model, _ = train(self.x_train_1st, self.y_train_1st,
                                          base_model,
                                          EPOCHS=self.epoch,
                                          lr=self.lr,
                                          verbose=False)

            self.base_modellist.append(trained_base_model)

            del base_model

    def level2_fit(self):
        ''' Train the meta-model. Use the outputs of base model as training data '''
        output_1st = []
        for model in self.base_modellist:
            output = predict(self.x_train_2nd, self.y_train_2nd, model)
            output_1st.append(output)

        fusion_train = np.array(output_1st).T

        self.fusion_model.fit(fusion_train, self.y_train_2nd)

    def fit(self, x_train, y_train,
            epoch,
            lr,
            split=False):

        self.epoch = epoch
        self.lr = lr
        self.x_train = x_train
        self.y_train = y_train

        if split:
            self.x_train_1st, self.y_train_1st, \
                self.x_train_2nd, self.y_train_2nd = split_data(x_train, y_train, 0.3)
        else:
            self.x_train_1st = x_train
            self.x_train_2nd = x_train
            self.y_train_1st = y_train
            self.y_train_2nd = y_train

        self.level1_fit()
        self.level2_fit()

        return self.fusion_model

    def predict(self, x_test, y_test):
        pred_1st = []
        for model in self.base_modellist:
            pred = predict(x_test, y_test, model)
            pred_1st.append(pred)

        input_2nd = np.array(pred_1st).T

        final_pred = self.fusion_model.predict(input_2nd)

        return input_2nd, final_pred


