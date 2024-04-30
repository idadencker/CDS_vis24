# Building a simple image search algorithm


## Introduction
This program contains a script that will load images of scanned 


papers from 3 different swiss newspapers to investigate the presence of human faces over the years of publication. Old newspapers are largely dominated by plain text and few illustrations, however with the advansing technology of personal cameraes that took place in 20th centary, more faces appeared in the newspapers. This program will use a pre-trained CNN model finetuned for face detection. Documentation for the model can be found [here](https://medium.com/%2540danushidk507/facenet-pytorch-pretrained-pytorch-face-detection-mtcnn-and-facial-recognition-b20af8771144). The results are grouped by decade and 1 csv for each newspaper is saved, showing per decade: the total count of faces and the percentage of pages that have at least 1 face on them. A plot is saved showing the latter for all 3 newspapers. The results are summarised and discussed.


## Data 
The dataset consists of ... The dataset can be found and downloaded [here](https://zenodo.org/records/3706863). 


## Repository overview 
The repository consists of:
- 1 README.md file
- 2 bash scripts
- 1 requirenments file
- in folder for storing input data
- out folder for holding the saved results
- src folder containing the script for counting faces and a utils folder


## Reproducibility 
To make the program work do the following:

1) download the dataset and place it in the 'in' folder. Unzip it so data becomes accessible 
2) in the .py script change folderpath to where your data is located 
3) in a terminal start by running the following code (make sure your directory is set to where setup.sh is located):
    $ source setup.sh
4) run
    $ python run.sh
... will be saved the the out folder 


## Summary and discussion
