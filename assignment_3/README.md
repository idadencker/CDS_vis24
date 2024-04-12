# Transfer learning 


## Introduction
This program contains scripts that will load and finetune the VGG16 model to test how well the models perform on predicting the class of different scanned documents of the ```Tobacco3482``` dataset. 
The VGG16 model is a convolutional neural network model pretrained on the ImageNet dataset which contains more than 14 million annotated images of different categories. VGG16 is considered to be one of the best computer vision models to date. 
Training CNNs from scratch is exteremly time-consuming and computationally heavy. When doing transfer learning, we can load a pretrained model and finetune it on new data to make it more task-specific. 
However one problematic apsect of CNNs are their tendency to overfit when training on small datasets. To account for such issue, batch normalization and data augmentation (DA) is applied to secure robustness. 
The program contains 3 different py scripts: 1 that finetune the VGG16 model withouth Batch Normalization (a baseline model), 1 that finetune the VGG16 model with Batch Normalization and 1 that finetune the VGG16 model with data augmentation. For each model an optimizer must be specified as either 'adam' or 'sgd'. A loss curve plot and a classification report for the model is saved in the out folder. 


## Data source
The dataset is the ```Tobacco3482``` dataset which consists of tobacco-related document images belonging to 10 classes such as letter, form, email, resume, memo, etc. The dataset has 3482 images. The dataset can be found [here](https://www.kaggle.com/datasets/patrickaudriaz/tobacco3482jpg?resource=download). 


## Repository structure

The repository consists of 2 bash scripts, 1 README.md file, 1 txt file, and 3 folders. The folders contains the following:

-   in: for storing input data
-   out: holds the saved results i.e. plots and classification reports 
-   src: consists of 3 scipts for implementing transfer learning on the VGG16 model


## Reproducibility 
To make the program work do the following:

1) download the dataset and place it in the 'in' folder. Unzip it so data becomes accessible 
2) in the .py script you want to run change folder_path to where your data is located 
3) in a terminal start by running the following code (make sure your directory is set to where setup.sh is located):
    $ source setup.sh
4) open the run.sh and put the name of the script you want to run in line 4 e.g.:
    $ python src/Transfer_learning_no_batch_normalization.py "$@"
5) in the terminal type what optimizer you want "adam" or "sgd" by running:
    $ source run.sh -o "adam"
A loss curve plot and a classification report will be saved the the out folder 


## Summary and discussion
From looking at the performance of the models we see that the model implementing batch normalization using the adam optimizer performs best with an accuracy score of 74%. Inspecting the loss curve for the model we see that loss for both test and validation starts to flatten out for every epoch which is good. However, we also see signs of overfitting since the validation set has a higher loss and a lower accuracy. The implimentation of the sgd optimizer is less prone to overfitting, however on the expence of slightly lower accuracy. 
Multiple things can be implemented to prevent overfitting e.g. data augmentation. However the performance of the DA models don't achieve higher accuracy, though from looking at the plots they seem to have tackled the overfitting better. Altering images by horizontal flips and 90 degress rotations might confuse the model too much, perhaps since the images allready are not of the best quality and therefore more sensitive to DA. 
Epochs is set to be 10 and from looking at the plots it seems sufficient for most models, however raising the number of epochs could improve performance on some of the models. Batch_size is set to 32 to help avoid overfitting on the small dataset and to reduce computational expences.
It should always be considered that the pretrained VGG16 model is trained on certain images in certain categories. If e.g. scanned documents of say email, letter etc. is not included, the model will perform poorly even after finetuning. 

