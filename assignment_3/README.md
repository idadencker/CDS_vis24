# Transfer learning 

This program contains scripts that will load and finetune the VGG16 model to test how well the models perform on predicting the class of different scanned documents. The VGG16 model is a convolutional neural network pretrained on the ImageNet dataset which contains more than 14 million annotated images of different categories. VGG16 is considered to be one of the best computer vision models to date. 
The program contains 3 different py scripts: 1 that finetune the VGG16 model withouth Batch Normalization, 1 that finetune the VGG16 model with Batch Normalization and 1 that finetune the VGG16 model with data Augmentation. For each model an optimizer must be specified as either 'adam' or 'sgd'. A loss curve plot and a classification report for the model is saved in the out folder. 

The dataset is the Tobacco3482 dataset which consists of tobacco-related document images belonging to 10 classes such as letter, form, email, resume, memo, etc. The dataset has 3482 images.


To make the program work do the following:

1) in the .py script you want to run change folder_path to where your data is located 
2) in a terminal start by running the following code (make sure your directory is set to where setup.sh is located):
    $ source setup.sh
3) open the run.sh and put the name of the script you want to run in line 4 e.g.:
    $ python src/Transfer_learning_no_batch_normalization.py "$@"
4) in the terminal type what optimizer you want "adam" or "sgd" by running:
    $ source run.sh -o "adam"
A loss curve plot and a classification report will be saved the the out folder 

From looking at the performance of the models we see that..

Epochs is set to be 10, however from inspecting the plots.. Batch_size is set to 32.. Data augmentation might not work because.. We should always consider that the pretrained VGG16 model is trained on certain images in certain categories. If e.g. scanned documents of say email, letter etc. is not included, the model will perform poorly even after finetuning. 

