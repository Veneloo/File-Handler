####################################################################################################
##  Author: Axel Cazorla                                                                          ##
##  Date Created: 9/20/2023                                                                       ##
##                                                                                                ##
##  This Python scripts automates any downloaded file into a folder depending the file type.      ##
##                                                                                                ##
####################################################################################################         

import os               ##This library allow interactiosn with our operating system (Will help us with reading file names in the directory)
import shutil           ##This library gives operations like moving and copying the files
import time             ##This library allow us to add pauses in our script depending what is the interval you want it to do updates on

##Paths(This will be your downloads folder and the folders you want the files to be redirected to.)

DOWNLOAD_FOLDER = r"C:/Users/axely/Downloads"   ##This is my path you change and add yours in this line.

##Now we will be making the organied folders, you can add/remove/modify them to your convinience.
ORGANIZED_FOLDERS = {
    "jpg": r"C:/Users/axely/Pictures",
    "jpeg": r"C:/Users/axely/Pictures",
    "pdf": r"C:/Users/axely/PDFs",

}

def file_organizer():
    for filename in os.listdir(DOWNLOAD_FOLDER):         ##This line begins a loop that iterates over each file in your downloads folder. os.listdir() returns a list of all files and directories in the specified path
             
        file_extesion = filename.split('.')[-1].lower()   ##Here, we're extracting the file extension. We split the filename by the period (.) character and take the last element.
                                                          ##The lower() function ensures that the extension is in lowercase, making the comparison case-insensitive.
        
        
        if file_extesion in ORGANIZED_FOLDERS:            ##This checks if the file's extension matches one of the keys in our ORGANIZED_FOLDERS dictionary.
            source  = os.path.join(DOWNLOAD_FOLDER,filename)    ##This constructs the full path to the file in the downloads folder.
            destination = os.path.join(ORGANIZED_FOLDERS[file_extesion],filename)   ##This constructs the full path where we want to move the file.

            ##Move file to the respective directory
            shutil.move(source, destination)        ##using shutil we move the file from source(downloads folder) to destination(folders created for respective file)
            print(f"Moved {filename} to {ORGANIZED_FOLDERS[file_extesion]}")    ##we print a message letting the user know which file was moved and to which folder.

if __name__ == "__main__":
    while True:
        file_organizer()
        time.sleep(1) ##This checks it every 10 seconds. However you can set it to any timeframe(in seconds) that you would like the scrip to check it
