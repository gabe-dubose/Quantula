from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt 
import numpy as np
import cv2
import os
from tkinter import DISABLED, END, INSERT, filedialog

#function to convert change background pixels
def background_converter(image, from_color, to_color, outfile):
    #read image
    image = Image.open(image, 'r').convert('RGB')
    #get pixel values
    pixel_values = list(image.getdata())
    #initialize new image
    new_image = []
    #if pixel is black, add blue pixel to new image, else add original pixel
    for pixel in pixel_values:
        if pixel == from_color:
            new_image.append(to_color)
        else:
            new_image.append(pixel)
    
    #rebuild image and save
    image.putdata(new_image)
    image.save(outfile)

#function to alter contrast
def contrast_adjuster(image, factor, outfile):
    #read image
    image = Image.open(image, 'r').convert('RGB')
    #initialize enhancer
    enhancer = ImageEnhance.Contrast(image)
    #enhance by factor
    enhanced_image = enhancer.enhance(factor)
    #save enhanced image
    enhanced_image.save(outfile)

#function to alter the sharpness of an image
def sharpness_adjuster(image, factor, outfile):
    #read image
    image = Image.open(image, 'r').convert('RGB')
    #initialize enhancer
    enhancer = ImageEnhance.Sharpness(image)
    #enhance by factor
    enhanced_image = enhancer.enhance(factor)
    #save image
    enhanced_image.save(outfile)

#function to alter saturation of an image
def saturation_adjuster(image, factor, outfile):
    #read image
    image = Image.open(image, 'r').convert('RGB')
    #initialize enhancer
    enhancer = ImageEnhance.Color(image)
    #enhance by factor
    enhanced_image = converter.enhance(factor)
    #save image
    enhanced_image.save(outfile)

#a function to perform k-means clustering on an image and recolor based on the average values of the clusters
def kmeans_transformer(image, k, outfile, iterations, epsilon, attempts):
    #read image
    image_load = cv2.imread(image)
    #convert to RGB
    image_load = cv2.cvtColor(image_load, cv2.COLOR_BGR2RGB)
    #reshape image to a 2D array with RGB values
    pixel_values = image_load.reshape((-1,3))
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

def boundary_tracer(image, color, outfile):
    #read image
    image = Image.open(image, 'r').convert('RGB')
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

            #if all adjacent pixels (8) are not the same color, recolor them to blue
            if pixel_in_count < 8:
                new_image.append(color)
            else:
                new_image.append(tuple(current_pixel))
            
    #write new image
    image.putdata(new_image)
    image.save(outfile)


#function to run quantula segmentation
def segment_colors_ui(image, input, advanced_options, log_window):

    operation_counter = 0
    current_file = image

    #designate sample name
    try:
        sample_name = image.split('/')[-1]
        try:
            sample_name = sample_name.split('.')[0]
        except:
            pass
    except:
        sample_name = 'quantula_out'

    #set up output
    full_output_path = f"{input['out_dir']}/{sample_name}"
    os.system(f'mkdir {full_output_path}')

    #convert background if input was correctly specified
    if input['bg_from'] != "NA" and input['bg_to'] != "NA":
        log_window.insert(INSERT, f"Converting background...\n")
        log_window.update()
        outfile = f"{full_output_path}/{operation_counter}_{sample_name}_bg.png"
        background_converter(image=current_file, from_color=input['bg_from'], to_color=input['bg_to'], outfile=outfile)
        log_window.insert(INSERT, f"Background converted.\n")
        log_window.update()
        current_file = outfile
        operation_counter += 1

    #perform image adjustments if specified
    #get image adjustmnet specifications adn sort
    image_adjustment_parameters = [[input['contrast_adjust_order'], input['contrast_factor'], 'contrast'], [input['sharpness_adjust_order'], input['sharpness_factor'], 'sharpness'], [input['saturation_adjust_order'], input['saturation_factor'], 'saturation']]
    image_adjustment_parameters.sort()
    #remove specifcations with 0 order (not specified)
    image_adjustment_parameters = [value for value in image_adjustment_parameters if value[0] != 0]
    #perform image adjustmnets if list is not empty
    if len(image_adjustment_parameters) != 0:
        for operation in image_adjustment_parameters:
            #contrast adjustment
            if operation[2] == 'contrast':
                log_window.insert(INSERT, f"Adjusting Contrast...\n")
                log_window.update()
                outfile = f"{full_output_path}/{operation_counter}_{sample_name}_con.png"
                contrast_adjuster(image=current_file, factor=operation[1], outfile=outfile)
                log_window.insert(INSERT, f"Contrast adjusted.\n")
                log_window.update()
                current_file = outfile
                operation_counter += 1

            #sharpness adjustment
            elif operation[2] == 'sharpness':
                log_window.insert(INSERT, f"Adjusting Sharpness...\n")
                log_window.update()
                outfile = f"{full_output_path}/{operation_counter}_{sample_name}_shrp.png"
                contrast_adjuster(image=current_file, factor=operation[1], outfile=outfile)
                log_window.insert(INSERT, f"Sharpness adjusted.\n")
                log_window.update()
                current_file = outfile
                operation_counter += 1

            #saturation adjustment
            elif operation[2] == 'saturation':
                log_window.insert(INSERT, f"Adjusting Saturation...\n")
                log_window.update()
                outfile = f"{full_output_path}/{operation_counter}_{sample_name}_sat.png"
                contrast_adjuster(image=current_file, factor=operation[1], outfile=outfile)
                log_window.insert(INSERT, f"Saturation adjusted.\n")
                log_window.update()
                current_file = outfile
                operation_counter += 1

    #perform k-means clustering if specified
    if input['color_number'] > 0:
        log_window.insert(INSERT, f"Performing K-means clustering...\n")
        log_window.update()
        outfile = f"{full_output_path}/{operation_counter}_{sample_name}_clst.png"
        kmeans_transformer(image=current_file, k=input['color_number'], outfile=outfile, iterations=advanced_options['kmeans_iterations'], epsilon=advanced_options['epsilon_input'], attempts=advanced_options['kmeans_attempts'])
        log_window.insert(INSERT, f"Color clustering complete.\n")
        log_window.update()
        current_file = outfile
        operation_counter += 1
    
    #perform boundary tracing
    if input['boundary_tracing_color'] != 'NA':
        log_window.insert(INSERT, f"Tracing color boundaries...\n")
        log_window.update()
        outfile = f"{full_output_path}/{operation_counter}_{sample_name}_bnd.png"
        boundary_tracer(image=current_file, color=input['boundary_tracing_color'], outfile=outfile)
        log_window.insert(INSERT, f"Boundary tracing complete.\n")
        log_window.update()
        current_file = outfile
        operation_counter += 1