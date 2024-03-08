import os
import argparse
import numpy as np

def file_loader():
    parser= argparse.ArgumentParser(description= "Loading and printing an array")
    parser.add_argument("--input", #long form name
                        "-i",#short form name 
                        required= True, #must give it an input (file name e.g. csv) in the command 
                        help= "Filepath to CSV for loading and printing") 
    args = parser.parse_args()
    return args

def main():
    args= file_loader() #execute fileloader funcction and put in args
    filename = os.path.join("..",
                            "..",
                            "..",
                            "..",
                            "cds-vis-data",
                            "data",
                            "sample-data",
                            args.input) #my main function define argument parser, will take in the input from the user in cmd line 

    data= np.loadtxt(filename, delimiter=",")

    print(data)

#if your code is executed from the command line run the code function main, otherwise dont do anything 
if __name__== "__main__":
    main()

#To call in terminal: 
#remeber to be in: cd IdaHeleneDencker#2808/CDS_visual/CDS_vis24/src
#python test_script.py --input "sample-data-01.csv"