# Detecting faces in historical newspapers


## Introduction



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


