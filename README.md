# EDTL
- A novel model Architecture combined Ensemble learning and Deep transfer learning.
- Paper: *Enhancing Quality and Electricity Consumption Prediction in textile Heat Drying Process via Ensemble Deep Transfer Learning*

# Installing
- Anaconda
- Python 3.9
- Package
   ```
   numpy == 1.20.3
   pandas == 1.3.4
   matplotlib == 3.4.3
   torch == 1.10.2
   torchvision == 0.11.3
   tensorflow == 2.8.0
   scikit-learn == 0.24.2
   eli5 == 0.13.0

   ```
   Run the command in Anaconda prompt to install necessary packages:
   ```
   pip install -r requirements.txt
   ```


# Program description
- **main_source.py**:
  The script is used to pretrain source model.
- **main_source.py**:
  The script is used to train target model.
- **ensemble.py**: 
   The stacking architecture to combine base model via  a meta-model.
- **feature.py**: 
   The highly correlated features for each target variable while training the correspond model.
- **network.py**: 
   The neural network class builded by Pytorch.
- **train_test.py**:
   The function of training and testing neural network.
- **SVR_configuration.py**:
   SVR parameter setting for different cases
- **utils.py**
  commonly used functions.


# Example command
```
$ python main_source.py
```
### outputs
- Prediction performances of source model. 
- Model's parameters are saved as .pkl file in the folder "pretrained_model".

```
$ python main_target.py

```

### ouputs
- Load the pretrained model and perform transfer learning and Ensemble learning.
- Three methods are test, including "Direct Learning", "Transfer Learning",  and "EDTL".
- The test result are saved as .csv file in the folder "result". 
