from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt 
import numpy as np
import cv2
import os
from tkinter import DISABLED, END, INSERT, filedialog
import pandas as pd

#function to convert background image
def recolor_background(image, from_color, to_color, outfile):
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
    enhanced_image = converter.enhance(factor)
    #save image
    enhanced_image.save(outfile)