# import the necessary packages
from imutils import paths
import argparse
import cv2
import shutil

#import sys, os, glob, shutil


def variance_of_laplacian(image):
	#create a folder called images and put all images there 
    #run the next line in CMD and make sure you are in the same folder 
    #C:\Users\RICHIE\Desktop\detect_blurr_images>
    #python move_blurr_images.py --images images

	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
	help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())


folder_path = ('C:/Users/RICHIE/Desktop/detect_blurr_images/')

dest = "C:/Users/RICHIE/Desktop/detect_blurr_images/blur_img/"



for imagePath in paths.list_images(args["images"]):
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)

	if fm < args["threshold"]:
		shutil.move(folder_path + imagePath, dest)
	
