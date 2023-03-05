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

#function to calculate euclidean distance between two colors
def calculate_euclidean_distance(ps, qs):
    #map RGB values to each other
    cartesian_coordinates = list(zip(ps,qs))
    #intiailize list to store ditances for each value
    coordinate_distances = []
    #iterate through each value and calculate distance between value coordinates
    for p,q in cartesian_coordinates:
        coordinate_distance = (p-q)**2
        coordinate_distances.append(coordinate_distance)
    #calculate euclidian distance
    euclidean_distance = sum(coordinate_distances)**0.5

    return euclidean_distance

#function to calculate closest input color using euclidean distances
def classify_color(pixel_map, pixel):
    #initialize list for storing each distance pair
    color_distances = []
    #iterate through all colors in input pixel map and calculate euclidean distance
    for reference_color in pixel_map:
        reference_pixel = pixel_map[reference_color]
        euclidean_distance = calculate_euclidean_distance(reference_pixel, pixel)
        color_distances.append([euclidean_distance, reference_color])
    
    #return color with smallest euclidean distance
    nearest_color = min(color_distances)

    return nearest_color

#function to re-color image based on euclidian minimization
def euclidian_minimization_recoloring(image, color_map, outfile):
    #read image
    image = Image.open(image, 'r').convert('RGB')
    #get pixel data
    pixel_values = list(image.getdata())
    
    #initialize output array for new image
    new_image = []
    
    #cache to hold pixel - classification pairings that have already been encountered
    pixel_classifications = {}
    
    #iterate through all pixels, perform classification and counting
    for pixel in pixel_values:

        #check if pixel has already been cached
        pixel_str = ','.join(str(value) for value in pixel)
        #if so, use cache to designate pixel color
        if pixel_str in pixel_classifications:
            pixel_color = pixel_classifications[pixel_str]
            #use pixel color to get pixel rgb value
            pixel_rgb = color_map[pixel_color]
            #add pixel to new image
            new_image.append(pixel_rgb)
            
        #if not, find closest color (smallest euclidean distance)
        elif pixel_str not in pixel_classifications:
            closest_color = classify_color(color_map, pixel)
            color = closest_color[1]

            #add newly classified color to cache
            pixel_str = ','.join(str(value) for value in pixel)
            pixel_classifications[pixel_str] = color
            
            #get pixel rgb value from mappings
            pixel_rgb = color_map[color]
            #add rgb to new image
            new_image.append(pixel_rgb)
            
    #create output image
    image.putdata(new_image)
    image.save(outfile)