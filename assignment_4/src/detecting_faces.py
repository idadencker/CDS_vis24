import os
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt


# Function to extract decade from filename:
def extract_decade(filename):
    parts = filename.split("-")
    year = int(parts[1])
    decade = (year // 10) * 10
    return decade


#function for using facenet
def get_num_faces(file_path):
    mtcnn = MTCNN(keep_all=True)    
    resnet = InceptionResnetV1(pretrained='casia-webface').eval()
    img = Image.open(file_path)
    boxes, _ = mtcnn.detect(img)
    if boxes is not None:
        num_faces = boxes.shape[0]  # Count the number of detected faces
    else:
        num_faces = 0  # No faces detected

    return num_faces


#Function for looping through files and saves

#function for plotting


def main():
    folderpath = "newspapers_2/"
    faces_rawcount_per_decade = {}   
    perc_pages_with_faces_per_decade = {}  
    pages_per_decade = {}
    
    #function for looping and saving




if __name__ == "__main__":
    main()