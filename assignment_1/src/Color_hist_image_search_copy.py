import sys
import os
import glob
sys.path.append("..")
import cv2 
import numpy as np
import matplotlib.pyplot as plt
from utilss.imutils import jimshow as show
from utilss.imutils import jimshow_channel as show_channel
import matplotlib.pyplot as plt
import pandas as pd
import shutil
from pandas import DataFrame


def calculate_target_image(filepath_target):
    '''
    Load in image
    '''
    image_f1 = cv2.imread(filepath_target)
    '''
    Extract color histogram and normalize
    '''
    hist_f1 = cv2.calcHist([image_f1], [0,1,2], None, [255, 255, 255],  [0,256, 0,256, 0,256])
    norm_hist_f1 = cv2.normalize(hist_f1, hist_f1, 0, 1.0, cv2.NORM_MINMAX)
    
    return norm_hist_f1



def loop_through_files(filepath_all, norm_hist_f1):

    '''
    Define dataframe to put the distances and filenames in
    '''
    distances_all = pd.DataFrame(columns= ("Filename", "Distance"))

    '''
    Loop through all files
    '''
    for file in sorted(os.listdir(filepath_all)):
            '''
            Creates a filepath for each flower and reads in the image
            '''
            filepath_f_x = os.path.join(filepath_all, file)
            image_fx = cv2.imread(filepath_f_x) 
            
            '''
            Creates a filename for each image
            '''
            filename_fx = file.split(".jpg") [0] 

            


            '''
            Extract the color histogram and normalizes it
            '''
            hist_fx = cv2.calcHist([image_fx], channels = [0,1,2], mask = None, histSize = [255,255,255], ranges = [0,256, 0,256,0,256]) 
            norm_hist_fx = cv2.normalize(hist_fx, hist_fx, 0, 1.0, cv2.NORM_MINMAX) 
            '''
            Saves an image for each file
            '''
            
            
            '''
            Compare extracted histogram to the target histogram. Saves the filename and the distance to the target in a row and put in in the dataframe
            '''
            dist_fx = round(cv2.compareHist(norm_hist_f1, norm_hist_fx, cv2.HISTCMP_CHISQR),2) 
            row_fx = [filename_fx, dist_fx]
            distances_all.loc[len(distances_all)] = row_fx


            
    return distances_all


def save_distances(distances_all):
    final_df=(distances_all.nsmallest(6, ["Distance"])) 
    out_path = "out/distance_metrics_color_hist.csv"
    final_df.to_csv(out_path, index=False)





def plot_images(distances_all, filepath_target, filepath_all):
    fig, axs = plt.subplots(1, 6, figsize=(15, 15))

    #get the 5 closest to target
    closest_images_filenames = distances_all.nsmallest(6, ["Distance"])["Filename"].tolist()
    
    # Plot the target image and the 5 closest images
    images_to_plot = [filepath_target] + [os.path.join(filepath_all, filename + ".jpg") for filename in closest_images_filenames[1:]]
    
    for i, image_path in enumerate(images_to_plot):
        image = cv2.imread(image_path)
        #axs[i].imshow(image)
        #show(image)
    
    plt.tight_layout()
    plt.savefig(f"out/plot_{i}")
    plt.show()







def main():
    filepath_target = os.path.join("..",
                            "..",
                            "..",
                            "..",
                            "cds-vis-data",
                            "flowers", 
                            "image_0001.jpg")
    norm_hist_f1 = calculate_target_image(filepath_target)
    filepath_all = os.path.join("..",
                                "..",
                                "..",
                                "..",
                                "cds-vis-data",
                                "flowers")

    distances_all = loop_through_files(filepath_all, norm_hist_f1)

    
    save_distances(distances_all)
    plot_images(distances_all, filepath_target, filepath_all)
    

    





if __name__ == "__main__":
    main()