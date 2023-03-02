from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt 
import numpy as np
import cv2
import os
from tkinter import DISABLED, END, INSERT, filedialog
import pandas as pd

#function to convert pixel image
def recolor_pixels(image, from_color, to_color, outfile):
    #read image
    image = Image.open(image).convert('RGB')
    #get pixel values
    pixel_values = list(image.getdata())
    #initialize new image
    new_image = []
    #change pixels
    for pixel in pixel_values:
        if pixel == from_color:
            new_image.append(to_color)
        else:
            new_image.append(pixel)
    
    #rebuild image and save
    image.putdata(new_image)
    image.save(outfile)

#function to alter contrast
def adjust_contrast(image, factor, outfile):
    #read image
    image = Image.open(image).convert('RGB')
    #initialize enhancer
    enhancer = ImageEnhance.Contrast(image)
    #enhance by factor
    enhanced_image = enhancer.enhance(factor)
    #save enhanced image
    enhanced_image.save(outfile)

#function to alter the sharpness of an image
def adjust_sharpness(image, factor, outfile):
    #read image
    image = Image.open(image).convert('RGB')
    #initialize enhancer
    enhancer = ImageEnhance.Sharpness(image)
    #enhance by factor
    enhanced_image = enhancer.enhance(factor)
    #save image
    enhanced_image.save(outfile)

#function to alter saturation of an image
def adjust_saturation(image, factor, outfile):
    #read image
    image = Image.open(image).convert('RGB')
    #initialize enhancer
    enhancer = ImageEnhance.Color(image)
    #enhance by factor
    enhanced_image = enhancer.enhance(factor)
    #save image
    enhanced_image.save(outfile)

#a function to perform k-means clustering on an image and recolor based on the average values of the clusters
def kmeans_transform(image, k, outfile, iterations, epsilon, attempts):
    #read image
    image_in = Image.open(image)
    #convert to array
    image_array = np.asarray(image_in)
    #reshape image to a 2D array with RGB values
    pixel_values = image_array.reshape((-1,3))
    #convert pixel values to float
    pixel_values = np.float32(pixel_values)
    #define run criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, iterations, epsilon)
    #perform kmeans clustering
    retval, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)
    # convert data into 8-bit values
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]
    
    #convert data to tuples
    segmented_data = [tuple(pixel) for pixel in segmented_data]
    
    #read image to make alterations
    image = Image.open(image, 'r').convert('RGB')
    #construct new image
    image.putdata(segmented_data)
    image.save(outfile)

#a function to trace boundaries between colors
def trace_color_boundaries(image, color, outfile, threshold):
    #read image
    image = Image.open(image).convert('RGB')
    #shape into array
    image_array = np.asarray(image)
    #record dimensions
    height = image_array.shape[0]
    width = image_array.shape[1]
    #initialize list for new pixel values
    new_image = []
    #iterate through each pixel and get all adjacent pixels
    for i in range(height):
        for j in range(width):
            current_pixel = image_array[i][j].tolist()
            try:
                above_pixel = image_array[i-1][j].tolist()
            except:
                above_pixel = 'NA'
            
            try:
                below_pixel = image_array[i+1][j].tolist()
            except:
                below_pixel = 'NA'
            
            try:
                left_pixel = image_array[i][j-1].tolist()
            except:
                left_pixel = 'NA'
            
            try:
                right_pixel = image_array[i][j+1].tolist()
            except:
                right_pixel = 'NA'
            
            try:
                diagonal_up_left_pixel = image_array[i-1][j-1].tolist()
            except:
                diagonal_up_left_pixel = 'NA'
            
            try:
                diagonal_up_right_pixel = image_array[i-1][j+1].tolist()
            except:
                diagonal_up_right_pixel = 'NA'
            
            try:
                diagonal_down_left_pixel = image_array[i+1][j-1].tolist()
            except:
                diagonal_down_left_pixel = 'NA'
            
            try:
                diagonal_down_right_pixel = image_array[i+1][j+1].tolist()
            except:
                diagonal_down_right_pixel = 'NA'
            
            #format adjacent pixels into a list
            adjacent_pixels = [above_pixel,below_pixel,left_pixel,right_pixel,diagonal_up_left_pixel,diagonal_up_right_pixel,diagonal_down_left_pixel,diagonal_down_right_pixel]
            #count number of times the current pixel matches adjacent pixels
            pixel_in_count = adjacent_pixels.count(current_pixel)

            #if count adjacent pixels are not the same color, recolor them
            if pixel_in_count < threshold:
                new_image.append(color)
            else:
                new_image.append(tuple(current_pixel))
            
    #write new image
    image.putdata(new_image)
    image.save(outfile)