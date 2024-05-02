# Image classification


## Introduction
This program contains scripts that will load, preprocess and classify the multiclass cifar10 dataset. One script implements a logistic regression classifier, including hyperparameter tuning of defined hyperparameters to determine the model with the greatest accuracy. The other script implements an architecturally more complex model, a multilayer perceptron (MLP) model. MLP is a feedforward artificial neural network, consisting of fully connected neurons, capable of learning complex patterns and relationships within data. 
Model performance of both models are evaluated and scoring metrics are summerised in the saved classification report alongside with a loss curve plot for the MLP model.
The results from both methods are summarized and discussed.


## Data 
The data used for classification is the CIFAR-10 dataset which consist of 6000 32x32 colour images for 10 different classes, totalling 60.000 images. The dataset can be loaded using the cifar10.load_data function, and will produce a train/test split of 50.000 training images and 10.000 test images. More details on the data are available [here](https://www.cs.toronto.edu/~kriz/cifar.html)


## Repository overview 
The repository consists of:
- 1 README.md file
- 2 bash scripts
- 1 requirenments file
- out folder for holding the saved results
- src folder containing the 2 scripts for conduction image classification 


## Reproducibility 
To make the program work do the following:

1) clone the repository 
```python
$ git clone "URL HERE"
```
2) In a terminal set your directory:
```python
$ cd assignment_2
```
3) To create a virtual environment run:
```python
$ source setup.sh
```
4) To run the 2 scripts and save results run: 
```python
$ source run.sh
```
2 classification reports and a loss curve plot for the MLP model will be saved the the out folder 

Please note that the scripts may take some time to execute. You can track information on hyperparameter tuning for logistic regression and the iterations for the MLP model in the terminal output.



## Summary and discussion
From looking at the classification...

for MLP: a logistic activation is applied
number of hidden layers is set to 100 to account for the fact that the dataset contains labels of 10 different classes. When inspecting the loss curve.. 