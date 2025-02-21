import os
import numpy as np
import pandas as pd
import torch
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

''' Commonly used functions '''

def load_data(features,
              target,
              file,
              seed=100):
    ''' Load the dataset '''
    raw_dataset = pd.read_csv(file, low_memory=False)
    raw_dataset = shuffle(raw_dataset, random_state=seed)
    x = raw_dataset[features].to_numpy()
    y = raw_dataset[target].to_numpy()

    return x, y

def split_data(x_data, y_data, proportion):
    num_split = np.random.choice(len(x_data), int(len(x_data) * proportion), replace=False)
    x_val = x_data[num_split]
    y_val = y_data[num_split]

    x_train = x_data[np.delete(np.arange(len(x_data)), num_split)]
    y_train = y_data[np.delete(np.arange(len(y_data)), num_split)]

    return x_train, y_train, x_val, y_val


def save_model(model, name):
    ''' save the parameters of trained models '''
    saved_path = f"./pretrained_model"
    if not os.path.exists(saved_path):
        os.makedirs(saved_path)
    saved_name = f"{saved_path}/{name}.pkl"
    with open(saved_name.encode('utf-8'), 'wb') as f:
        torch.save(model.state_dict(), f)

    print("Save model")


def plot_distribution(score, y_test, pred,
                     types, prodction_line, target, image_path,
                      save_figure=False):

    ''' Plot a bar chart to show the data distribution,
    comparing the predicted values with the ground truth values. '''

    plt.figure()
    plt.hist(y_test, bins=100, density=False, color='lightcoral', alpha=1, label='ground truth')
    plt.hist(pred, bins=100, density=False, color='blue', alpha=0.3, label='Model predict')

    # plt.xlabel("MAPE = {:.2f} % ".format(mape), fontsize=14)
    plt.xlabel(" Target values", fontsize=12)
    plt.ylabel('Amount', fontsize=12)
    plt.legend()
    plt.title(f"Distribution of {target} ({prodction_line}{types})", fontsize=12)
    plt.text(0.2, 0.7, f"MAPE = {score:.2f} %", fontsize=14, transform=plt.gca().transAxes,
             horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='white', alpha=0.8))
    if save_figure:
        if not os.path.exists(image_path):
            os.makedirs(image_path)
        plt.savefig(image_path + '/' + target + types + str(' {:.2f}%'.format(score)) + '.jpg')
    plt.show()




