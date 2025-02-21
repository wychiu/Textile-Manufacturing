import numpy as np
import torch.nn.functional as F
import torch
from torch import nn, optim
from torch.utils.data import DataLoader, TensorDataset

''' The functions for training and testing model. 
    The details of implementation refer Pytorch's official documentations'''

def train(x_train, y_train, model, EPOCHS, lr=1e-3, verbose=True):
    model.train()

    train = TensorDataset(torch.Tensor(np.array(x_train)), torch.Tensor(np.array(y_train)))
    train_loader = DataLoader(train, batch_size=128, shuffle=False)

    critrien = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    score_history = []
    for epoch in range(EPOCHS):
        running_loss = 0.0
        score_all = []
        for i, data in enumerate(train_loader):
            inputs, labels = data
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = critrien(outputs, labels)
            score = torch.mean(torch.abs((outputs - labels) / labels)) * 100
            score_all.append(score.item())
            loss.backward()
            optimizer.step()

            ## print statistics
            running_loss += loss.item()
            if verbose:
                if i % 10 == 9:  # print every 2000 mini-batches
                    print('[%d, %5d] loss: %.3f  Train_MAPE: %.3f' %
                          (epoch + 1, i + 1, running_loss / 10, score), "")
                    running_loss = 0.0

        score_history.append(sum(score_all) / len(score_all))

    return model, score_history


def predict(x_test, y_test, model):
    model.eval()

    test = TensorDataset(torch.Tensor(np.array(x_test)), torch.Tensor(np.array(y_test)))
    test_loader = DataLoader(test, batch_size=1, shuffle=False)

    real = []
    prediction = []

    for i, data in enumerate(test_loader):
        inputs, labels = data
        outputs = model.forward(inputs)
        outputs = outputs.detach().item()
        labels = labels.detach().item()
        real.append(labels)
        prediction.append(outputs)

    return prediction
