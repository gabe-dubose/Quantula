#!/usr/bin/env python3

import tkinter as tk	
from tkinter import *				
from tkinter import ttk
from tkinter.ttk import *
from tkinter import DISABLED, END, INSERT, filedialog
import os
from PIL import Image
from clique import sutils
from clique import qutils
import time

#initialize master
root = tk.Tk()
root.title("clique")
root.geometry("1025x800")

#set up tab control
tabControl = ttk.Notebook(root)
#get home directory path 
home_path = os.path.expanduser('~')

#set up color segmentation tab
colorSegmentationTab = ttk.Frame(tabControl)
tabControl.add(colorSegmentationTab, text ='Color Segmentation')

#set up color quantification tab
colorQuantificationTab = ttk.Frame(tabControl)
tabControl.add(colorQuantificationTab, text ='Color Quantification')

#add tabs
tabControl.grid(column=0, row=0)


####################   COLOR SEGMENTATION TAB   ####################


#IMAGE INPUT LABELED FRAME
imageInputFrame = tk.LabelFrame(colorSegmentationTab, text="Image Upload")
imageInputFrame.grid(row=1, column=0, sticky = "ew", pady=5, padx=10)

#add prompt to select image file
imageSelectPrompt = tk.Label(imageInputFrame, text="Image File:")
imageSelectPrompt.grid(row=1, column=1, pady=5, padx=10)

#function to select image
def select_image_file():
    filetypes = (('PNG File', '*.png'), ('All files', '*.*'))
    image_file = filedialog.askopenfilename(title="Open Files", initialdir = home_path, filetypes = filetypes)
    image_file_input.delete(0, END)
    image_file_input.insert(0, image_file)

#add entry for image file
image_file_input = tk.Entry(imageInputFrame)
image_file_input.grid(row=1, column=2, padx=10, pady=5)

#add button for selecting images
imageFileSelectButton = tk.Button(imageInputFrame, text="Select File", command=select_image_file)
imageFileSelectButton.grid(row=1, column=3, padx=10, pady=5, sticky="w")

#add prompt to select directory containing images
imageDirSelectPrompt = tk.Label(imageInputFrame, text="Directory:")
imageDirSelectPrompt.grid(row=2, column=1, padx=10, pady=5)

#function to select image directory
def select_image_dir():
    image_dir = filedialog.askdirectory(title="Open Directories", initialdir = home_path)
    image_dir_input.delete(0, END)
    image_dir_input.insert(0, image_dir)

#add entry for selecting directory containing images
image_dir_input = tk.Entry(imageInputFrame)
image_dir_input.grid(row=2, column=2, padx=10, pady=5)

#add button for selecting directory containing images
imageDirSelectButton = tk.Button(imageInputFrame, text="Select Folder", command=select_image_dir)
imageDirSelectButton.grid(row=2, column=3, padx=10, pady=5, sticky="w")


#BACKGROUND CONVERSION LABELED FRAME
backgroundConversionFrame = tk.LabelFrame(colorSegmentationTab, text="Background Conversion")
backgroundConversionFrame.grid(row=2, column=0, sticky = "ew", pady=5, padx=10)

#prompt for background color specification
backgroundColorPrompt = tk.Label(backgroundConversionFrame, text="Color (R,G,B):", padx=10, pady=5)
backgroundColorPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

#Entry box for background color specification
background_color_input = tk.Entry(backgroundConversionFrame, width=14)
background_color_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

#set default background color
background_color_input.insert(0, '0,0,0')

#function to convert RGB values to tkinter-readable values
def convert_rgb(rgb_values):
    r,g,b = rgb_values
    conv = f'#{r:02x}{g:02x}{b:02x}'
    return conv

#function to display background color
def display_bg_from_color():
    rgb_values = background_color_input.get()
    rgb_values = tuple([int(value) for value in rgb_values.split(',')])
    rgb_values = convert_rgb(rgb_values)
    bgColorDisplay.configure(bg=rgb_values)

#add background color checker
bgColorDisplay = Canvas(backgroundConversionFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
bgColorDisplay.grid(row=1, column=4, padx=10)

#add button to check color
bgColorViewButton = tk.Button(backgroundConversionFrame, text="View", command=display_bg_from_color)
bgColorViewButton.grid(row=1, column=3, pady=10, padx=5)

#prompt for background conversion color specification
backgroundColorPrompt = tk.Label(backgroundConversionFrame, text="Convert to (R,G,B):", padx=10, pady=5)
backgroundColorPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

#Entry box for background color specification
color_convert_input = tk.Entry(backgroundConversionFrame, width=14)
color_convert_input.grid(row=2, column=2, padx=10, pady=5, sticky="w")

#set default background color
color_convert_input.insert(0, '0,0,255')

#function to display background color conversion
def display_bg_to_color():
    rgb_values = color_convert_input.get()
    rgb_values = tuple([int(value) for value in rgb_values.split(',')])
    rgb_values = convert_rgb(rgb_values)
    bgColorConvertDisplay.configure(bg=rgb_values)

#add background color checker
bgColorConvertDisplay = Canvas(backgroundConversionFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
bgColorConvertDisplay.grid(row=2, column=4, padx=10)

#add button to check color
bgColorConvertViewButton = tk.Button(backgroundConversionFrame, text="View", command=display_bg_to_color)
bgColorConvertViewButton.grid(row=2, column=3, pady=10, padx=5)


#IMAGE ADJUSTMENTS LABELED FRAME
imageAdjustmentFrame = tk.LabelFrame(colorSegmentationTab, text="Image Adjustments")
imageAdjustmentFrame.grid(row=3, column=0, sticky = "ew", pady=5, padx=10)

#add prompt to get contrast
contrastPrompt = tk.Label(imageAdjustmentFrame, text="Contrast:", padx=10, pady=5)
contrastPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

#add scale to select contrast adjustment
contrast_input = IntVar()
contrastAdjustmentScale = tk.Scale(imageAdjustmentFrame, variable = contrast_input, from_ = -10, to = 10, orient = HORIZONTAL, width=20, sliderlength=20, length=185)
contrastAdjustmentScale.grid(row=1, column=3, pady=5, padx=10, sticky="w")

#add prompt to get contrast
contrastOrderPrompt = tk.Label(imageAdjustmentFrame, text="Order:", padx=10, pady=5)
contrastOrderPrompt.grid(row=1, column=4, pady=5, padx=5, sticky="w")

#add operation order for contrast adjustment
contrast_order_input = IntVar()
contrast_order_input.set(0)
ConstrastOrderOption = OptionMenu(imageAdjustmentFrame, contrast_order_input, *[0,0,1,2,3])
ConstrastOrderOption.grid(row=1, column=5, pady=5, padx=(0,10), sticky="e")

#add prompt to get sharpness
sharpnessPrompt = tk.Label(imageAdjustmentFrame, text="Sharpness:", padx=10, pady=5)
sharpnessPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

#add scale to select contrast adjustment
sharpness_input = IntVar()
sharpnessAdjustmentScale = tk.Scale(imageAdjustmentFrame, variable = sharpness_input, from_ = -10, to = 10, orient = HORIZONTAL, width=20, sliderlength=20, length=185)
sharpnessAdjustmentScale.grid(row=2, column=3, pady=5, padx=10, sticky="w")

#add prompt to get contrast
sharpnessOrderPrompt = tk.Label(imageAdjustmentFrame, text="Order:", padx=10, pady=5)
sharpnessOrderPrompt.grid(row=2, column=4, pady=5, padx=5, sticky="w")

#add operation order for contrast adjustment
sharpness_order_input = IntVar()
sharpness_order_input.set(0)
sharpnessOrderOption = OptionMenu(imageAdjustmentFrame, sharpness_order_input, *[0,0,1,2,3])
sharpnessOrderOption.grid(row=2, column=5, pady=5, padx=(0,10), sticky="e")

#add prompt to get saturation
saturationPrompt = tk.Label(imageAdjustmentFrame, text="Saturation:", padx=10, pady=5)
saturationPrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

#add scale to select contrast adjustment
saturation_input = IntVar()
saturationAdjustmentScale = tk.Scale(imageAdjustmentFrame, variable = saturation_input, from_ = -10, to = 10, orient = HORIZONTAL, width=20, sliderlength=20, length=185)
saturationAdjustmentScale.grid(row=3, column=3, pady=5, padx=10, sticky="w")

#add prompt to get contrast
saturationOrderPrompt = tk.Label(imageAdjustmentFrame, text="Order:", padx=10, pady=5)
saturationOrderPrompt.grid(row=3, column=4, pady=5, padx=5, sticky="w")

#add operation order for contrast adjustment
saturation_order_input = IntVar()
saturationOrderOption = OptionMenu(imageAdjustmentFrame, saturation_order_input, *[0,0,1,2,3])
saturationOrderOption.grid(row=3, column=5, pady=5, padx=(0,10), sticky="e")


#COLOR CLUSTERING AND SEGMENTATION LABELED FRAME
colorSegmentationFrame = tk.LabelFrame(colorSegmentationTab, text="Color Clustering and Segmentation")
colorSegmentationFrame.grid(row=4, column=0, sticky = "ew", pady=5, padx=10)

#add prompt to get color number
colorNumberPrompt = tk.Label(colorSegmentationFrame, text="Number of colors:", padx=10, pady=5)
colorNumberPrompt.grid(row=1, column=1, pady=5, padx=5, sticky="w")

#add entry for specifying the number of colors for K-means clustering
color_number_input = tk.Entry(colorSegmentationFrame, width = 13)
color_number_input.grid(row=1, column=2, padx=0, pady=5, sticky="w")
color_number_input.insert(0, 0)

#prompt for boundary color specification
boundaryColorPrompt = tk.Label(colorSegmentationFrame, text="Boundary Color (R,G,B):", padx=10, pady=5)
boundaryColorPrompt.grid(row=2, column=1, pady=5, padx=(5,0), sticky="w")

#Entry box for boundary color specification
boundary_color_input = tk.Entry(colorSegmentationFrame, width=13)
boundary_color_input.grid(row=2, column=2, padx=0, pady=5, sticky="w")

#set default background color
boundary_color_input.insert(0, '255,0,0')

#function to display background color conversion
def display_boundary_color():
    rgb_values = boundary_color_input.get()
    rgb_values = tuple([int(value) for value in rgb_values.split(',')])
    rgb_values = convert_rgb(rgb_values)
    boundaryColorConvertDisplay.configure(bg=rgb_values)

#add background color checker
boundaryColorConvertDisplay = Canvas(colorSegmentationFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
boundaryColorConvertDisplay.grid(row=2, column=4, padx=10)

#add button to check color
bgColorConvertViewButton = tk.Button(colorSegmentationFrame, text="View", command=display_boundary_color)
bgColorConvertViewButton.grid(row=2, column=3, pady=10, padx=5)

#OUTPUT LABELED FRAME
outputFrame = tk.LabelFrame(colorSegmentationTab, text="Output Options")
outputFrame.grid(row=5, column=0, sticky = "ew", pady=5, padx=10)

#add prompt to select output directory 
imageDirSelectPrompt = tk.Label(outputFrame, text="Directory:", padx=10, pady=5)
imageDirSelectPrompt.grid(row=1, column=1, padx=10, pady=5)

#function to select output directory
def select_out_dir():
    out_dir = filedialog.askdirectory(title="Open Directories", initialdir = home_path)
    out_dir_input.delete(0, END)
    out_dir_input.insert(0, out_dir)

#add entry for selecting output directory 
out_dir_input = tk.Entry(outputFrame)
out_dir_input.grid(row=1, column=2, padx=10, pady=5)
out_dir_input.insert(0, home_path)

#add button for selecting output directory 
outDirSelectButton = tk.Button(outputFrame, text="Select Folder", command=select_out_dir)
outDirSelectButton.grid(row=1, column=3, padx=10, pady=5, sticky="w")

#add prompt to rename output
renameOutputPrompt = tk.Label(outputFrame, text="Rename:", padx=10, pady=5)
renameOutputPrompt.grid(row=2, column=1, padx=10, pady=5)

#add entry for renaming option
rename_input = tk.Entry(outputFrame)
rename_input.grid(row=2, column=2, padx=10, pady=5)


#LOGGING
#add progress bar
colorSegmentationProgressBar = Progressbar(colorSegmentationTab, orient=HORIZONTAL, mode='indeterminate', length=300)
colorSegmentationProgressBar.grid(row=0, column=1, sticky = "sew", pady=0, padx=10)

#LOG WINDOW LABELED FRAME
logWindowFrame = tk.LabelFrame(colorSegmentationTab, text="Log Window")
logWindowFrame.grid(row=1, column=1, sticky = "new", pady=5, padx=10, rowspan=50)

#add log window
log_window = tk.Text(logWindowFrame, width=65, height=30)
log_window.grid(row=0, column=0)

#METADATA LABELED FRAME
metaDataFrame = tk.LabelFrame(colorSegmentationTab, text="Metadata Options")
metaDataFrame.grid(row=4, column=1, sticky = "new", pady=5, padx=10)

#add prompt to select metadata file
metadataSelectPrompt = tk.Label(metaDataFrame, text="Metadata File:")
metadataSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

#function to select metadata
def select_metadata_file():
    filetypes = (('CSV File', '*.csv'), ('All files', '*.*'))
    metadata_file = filedialog.askopenfilename(title="Open Files", initialdir = home_path, filetypes = filetypes)
    metadata_file_input.delete(0, END)
    metadata_file_input.insert(0, metadata_file)

#add entry for metadata file
metadata_file_input = tk.Entry(metaDataFrame)
metadata_file_input.grid(row=1, column=2, padx=10, pady=5)

#add metadata select button
metadataSelectButton = tk.Button(metaDataFrame, text="Select File", command=select_metadata_file)
metadataSelectButton.grid(row=1, column=3, pady=10, sticky="w")

#add prompt to select metadata dir
metadataDirSelectPrompt = tk.Label(metaDataFrame, text="New File:")
metadataDirSelectPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

#function to select metadata directory
def select_metadata_dir():
    metadata_dir = filedialog.askdirectory(title="Open Directories", initialdir = home_path)
    metadata_dir_input.delete(0, END)
    metadata_dir_input.insert(0, metadata_dir)

#add entry for image file
metadata_dir_input = tk.Entry(metaDataFrame)
metadata_dir_input.grid(row=2, column=2, padx=10, pady=5)

#add metadata select button
metadataDirSelectButton = tk.Button(metaDataFrame, text="Select Folder", command=select_metadata_dir)
metadataDirSelectButton.grid(row=2, column=3, pady=5, padx=(0,10))

#function to clear run
def reset_run():
    #delete image file input
    image_file_input.delete(0, END)
    #delete image directory input
    image_dir_input.delete(0, END)
    #reset background color specification to (0,0,0)
    background_color_input.delete(0, END)
    background_color_input.insert(0, '0,0,0')
    #reset background color conversion color specification
    color_convert_input.delete(0, END)
    color_convert_input.insert(0, '0,0,255')
    #reset contrast adjustment slider and operation order
    contrastAdjustmentScale.set(0)
    contrast_order_input.set(0)
    #reset sharpness adjustment slider and operation order
    sharpnessAdjustmentScale.set(0)
    sharpness_order_input.set(0)
    #reset saturation adjustment slider and operation order
    saturationAdjustmentScale.set(0)
    saturation_order_input.set(0)
    #reset number of colors input
    color_number_input.delete(0, END)
    color_number_input.insert(0, 0)
    #reset boundary tracing input
    boundary_color_input.delete(0, END)
    boundary_color_input.insert(0, '255,0,0')
    #reset output directory
    out_dir_input.delete(0, END)
    out_dir_input.insert(0, home_path)
    #reset output rename option
    rename_input.delete(0, END)
    #clear log window
    log_window.delete('1.0', END)
    #reset metadata file entry
    metadata_file_input.delete(0, END)
    #reset metadata directory entry
    metadata_dir_input.delete(0, END)

####################   ADVANCED SEGMENTATION OPTIONS WINDOW   ####################
#initialize dictionary for advacned segmentaiton options
advanced_segmentation_options = {'epsilon_input' : 0.85, 'kmeans_iterations' : 100, 'kmeans_attempts' : 10}

#function to show advanced options for color segmentation window
def show_advanced_segmentation_window():
    advancedWindow = Toplevel(root)
    advancedWindow.title("Advanced Color Segmentation Options")
    advancedWindow.geometry('325x400')

    #ADVANCED K-MEANS CLUSTERING LABELED FRAME
    advancedKmeansFrame = tk.LabelFrame(advancedWindow, text="K-means clustering advanced options")
    advancedKmeansFrame.grid(row=1, column=0, sticky = "ew", pady=5, padx=10)

    #add prompt to specify epsilon
    epsilonPrompt = tk.Label(advancedKmeansFrame, text="Epsilon:")
    epsilonPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")
    
    #add entry for epsilon
    global epsilon_input
    epsilon_input = tk.Entry(advancedKmeansFrame)
    epsilon_input.grid(row=1, column=2, padx=10, pady=5)
    #set default
    epsilon_input.insert(0, '0.85')
    #update entry
    if 'epsilon_input' in advanced_segmentation_options:
        epsilon_input.delete(0, END)   
        epsilon_input.insert(0, f"{advanced_segmentation_options['epsilon_input']}")

    #add prompt to specify iterations
    iterationsPrompt = tk.Label(advancedKmeansFrame, text="Iterations:")
    iterationsPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")
    
    #add entry for iterations
    global kmeans_iterations_input
    kmeans_iterations_input = tk.Entry(advancedKmeansFrame)
    kmeans_iterations_input.grid(row=2, column=2, padx=10, pady=5)
    #set default
    kmeans_iterations_input.insert(0, '100')
    #update entry
    if 'kmeans_iterations' in advanced_segmentation_options:
        kmeans_iterations_input.delete(0, END)   
        kmeans_iterations_input.insert(0, f"{advanced_segmentation_options['kmeans_iterations']}")

    #add prompt to specify attempts
    kmeansAttemptsPrompt = tk.Label(advancedKmeansFrame, text="Attempts:")
    kmeansAttemptsPrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")
    
    #add entry for attempts
    global kmeans_attempts_input
    kmeans_attempts_input = tk.Entry(advancedKmeansFrame)
    kmeans_attempts_input.grid(row=3, column=2, padx=10, pady=5)
    #set default
    kmeans_attempts_input.insert(0, '10')
    #update entry
    if 'kmeans_attempts' in advanced_segmentation_options:
        kmeans_attempts_input.delete(0, END)   
        kmeans_attempts_input.insert(0, f"{advanced_segmentation_options['kmeans_attempts']}")

    #add button to export information back to main window
    exportOptionsButton = tk.Button(advancedWindow, text="Save", command=save_advanced_segmentation_options)
    exportOptionsButton.grid(row=2, column=0, sticky = "ew", pady=5, padx=10)

#function to update advances segmentation clustering options
def save_advanced_segmentation_options():
    #check that epsilon is valid
    try:
        epsilon_value = float(epsilon_input.get())
        advanced_segmentation_options['epsilon_input'] = epsilon_value
    except:
        tk.messagebox.showerror("Input Error", f"Error: {epsilon_input.get()} is an invalid epsilon value.")
    
    #check that iterations is valid
    try:
        kmeans_iterations = int(kmeans_iterations_input.get())
        advanced_segmentation_options['kmeans_iterations'] = kmeans_iterations
    except:
        tk.messagebox.showerror("Input Error", f"Error: {kmeans_iterations_input.get()} is an invalid iterations value.")

    try:
        kmeans_attempts = int(kmeans_iterations_input.get())
        advanced_segmentation_options['kmeans_attempts'] = kmeans_attempts
    except:
        tk.messagebox.showerror("Input Error", f"Error: {kmeans_iterations_input.get()} is an attempts iterations value.")

####################   COLOR SEGMENTATION TAB   ####################

#add advanced options
advancedOptionsButton = tk.Button(colorSegmentationTab, text="Advanced options", command=show_advanced_segmentation_window)
advancedOptionsButton.grid(row=5, column=1, sticky = "sew", pady=5, padx=10)

#add clear run button
clearRunButton = tk.Button(colorSegmentationTab, text="Reset Run", command=reset_run)
clearRunButton.grid(row=6, column=1, sticky = "ew", pady=5, padx=10)

#function to check RGB input
def check_rgb_input(rgb_value):
    #check to see if rgb value is in correct format
    try:
        rgb_value = tuple(int(x) for x in rgb_value.split(","))
        #check to see if rgb value is valid
        rgb_check = 0
        for value in rgb_value:
            if value > 255:
                rgb_check += 1
            else:
                pass
        if rgb_check == 0:
            return rgb_value
        else:
            return 'Error_RGB_value'       
    except:
        return 'Error_format'
    
#function to check if file is readable
def check_image_file(image_file):
    try:
        Image.open(image_file, 'r')
        return 1
    except:
        return 0

#function to collect and check input
def get_input():

    #initialize dictionary to store input option
    standard_user_input = {}

    #get image file
    image_file = image_file_input.get()
    #get image directory
    image_directory = image_dir_input.get()
    #get background from color input
    background_convert_from = background_color_input.get()
    #get background to color input
    background_convert_to = color_convert_input.get()
    #get contrast adjustment input
    contrast_factor = contrast_input.get()
    contrast_adjust_order = contrast_order_input.get()
    #get sharpness adjustment input
    sharpness_factor = sharpness_input.get()
    sharpness_adjust_order = sharpness_order_input.get()
    #get saturation adjustment input
    saturation_factor = saturation_input.get()
    saturation_adjust_order = saturation_order_input.get()
    #get K input
    color_number = color_number_input.get()
    #get tracing color input
    boundary_color = boundary_color_input.get()
    #get output directory
    out_dir = out_dir_input.get()
    #get rename output option
    rename = rename_input.get()
    #get metadata file upload
    metadata_file = metadata_file_input.get()
    #get save metadata to input
    metadata_dir = metadata_dir_input.get()

    #initialize error variable
    error = 0

    #check that image file or directory has been specified
    if image_file == "" and image_directory == "" and error ==0:
        tk.messagebox.showerror("Input Error", "Error: No image file or directory was specified.")
        error += 1

    #check that image file and directory were not both specified
    elif image_file != "" and image_directory != "" and error ==0:
        tk.messagebox.showerror("Input Error", "Error: Both image file and directory were specified.")
        error += 1
    
    #check that all criteria for background color conversions are specified
    if error == 0:
        if background_convert_from == "" and background_convert_to != "":
            tk.messagebox.showerror("Input Error", "Error: Background conversion was specified, but background color was not.")
            error += 1

    #check that background conversion from RGB specifications are in the correct format
    if error == 0 and background_convert_from != "":
        background_color_from = check_rgb_input(background_convert_from)
        if background_color_from[0:5] == 'Error':
            if background_color_from == 'Error_format':
                tk.messagebox.showerror("Input Error", f"Error: Background color specification ({background_convert_from}) format not recognized.")
                error += 1
            elif background_color_from == 'Error_RGB_value':
                tk.messagebox.showerror("Input Error", f"Error: ({background_convert_from}) is an invalid RGB value.")
                error += 1

    #check that background conversion to RGB specifications are in the correct format
    if error == 0 and background_convert_to != "":
        background_color_to = check_rgb_input(background_convert_to)
        if background_color_to[0:5] == 'Error':
            if background_color_to == 'Error_format':
                tk.messagebox.showerror("Input Error", f"Error: Background color specification ({background_convert_to}) format not recognized.")
                error += 1
            elif background_color_to == 'Error_RGB_value':
                tk.messagebox.showerror("Input Error", f"Error: ({background_convert_to}) is an invalid RGB value.")
                error += 1
    
    #check that image adjustments weren't specified without telling an order and vise versa
    #check contrast
    if error == 0:
        if contrast_factor != 0 and contrast_adjust_order == 0:
            tk.messagebox.showerror("Input Error", f"Error: Contrast adjustment was specified but adjustment operation order was not.")
            error += 1
        if contrast_factor == 0 and contrast_adjust_order != 0:
            tk.messagebox.showerror("Input Error", f"Error: Contrast adjustment was not specified but adjustment operation order was.")
            error += 1 

    #check sharpness
    if error == 0:
        if sharpness_factor != 0 and sharpness_adjust_order == 0:
            tk.messagebox.showerror("Input Error", f"Error: Sharpness adjustment was specified but adjustment operation order was not.")
            error += 1
        if sharpness_factor == 0 and sharpness_adjust_order != 0:
            tk.messagebox.showerror("Input Error", f"Error: Sharpness adjustment was not specified but adjustment operation order was.")
            error += 1          

    #check saturation
    if error == 0:
        if saturation_factor != 0 and saturation_adjust_order == 0:
            tk.messagebox.showerror("Input Error", f"Error: Saturation adjustment was specified but adjustment operation order was not.")
            error += 1
        if saturation_factor == 0 and saturation_adjust_order != 0:
            tk.messagebox.showerror("Input Error", f"Error: Saturation adjustment was not specified but adjustment operation order was.")
            error += 1    
    
    #check that number of colors is a number
    if error == 0:
        if color_number == "":
            tk.messagebox.showerror("Input Error", f"Error: Number of color clusters not specified.")
            error += 1
        else:
            try:
                color_number = int(color_number)
            except:
                tk.messagebox.showerror("Input Error", f"Error: Number of colors ({color_number}) is not an integer.")
                error += 1
    
    #check that tracing RGB specifications are in the correct format
    if error == 0 and boundary_color != "":
        boundary_tracing_color = check_rgb_input(boundary_color)
        if boundary_tracing_color[0:5] == 'Error':
            if boundary_tracing_color == 'Error_format':
                tk.messagebox.showerror("Input Error", f"Error: Background color specification ({boundary_color}) format not recognized.")
                error += 1
            elif boundary_tracing_color == 'Error_RGB_value':
                tk.messagebox.showerror("Input Error", f"Error: ({boundary_color}) is an invalid RGB value.")
                error += 1  

    #check that new and existing metadata files were not both specified
    if error == 0:
        if metadata_file != "" and metadata_dir != "":
            tk.messagebox.showerror("Input Error", "Error: Both existing and new metadata options were specified.")
            error += 1

    #check that single input image can be read (images in directory will be checked at their runtime)
    if error == 0:
        if image_file != "":
            image_check = check_image_file(image_file)
            if image_check == 0:
                tk.messagebox.showerror("Input Error", f"Error: Image {image_file} could not be read.")
                error += 1

    #if no errors were encountered, assemble and return input
    if error == 0:
        if image_file != "":
            standard_user_input['image_file_input'] = image_file

        elif image_directory != "":
            files_to_get = os.listdir(image_directory)
            standard_user_input['image_dir_input'] = [f"{image_directory}/{file}" for file in files_to_get]
        
        if background_convert_from != "":
            standard_user_input['bg_from'] = background_color_from
        else:
            standard_user_input['bg_from'] = 'NA'

        if background_convert_to != "":
            standard_user_input['bg_to'] = background_color_to
        else:
            standard_user_input['bg_to'] = 'NA'
        
        standard_user_input['contrast_factor'] = contrast_factor
        standard_user_input['contrast_adjust_order'] = contrast_adjust_order

        standard_user_input['sharpness_factor'] = sharpness_factor
        standard_user_input['sharpness_adjust_order'] = sharpness_adjust_order

        standard_user_input['saturation_factor'] = saturation_factor
        standard_user_input['saturation_adjust_order'] = saturation_adjust_order

        standard_user_input['color_number'] = color_number

        if boundary_color != "":
            standard_user_input['boundary_tracing_color'] = boundary_tracing_color
        else:
            standard_user_input['boundary_tracing_color'] = 'NA'

        standard_user_input['out_dir'] = out_dir
                
        if metadata_file != "":
            standard_user_input['metadata_file'] = metadata_file
        elif metadata_dir != "":
            standard_user_input['new_metadata_dir'] = metadata_dir

        return standard_user_input

    else:
        return 0

def run_clique(image, input, advanced_options):
    #colorSegmentationProgressBar['value'] = 1

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
        sample_name = 'clique_out'

    #set up output
    full_output_path = f"{input['out_dir']}/{sample_name}"
    os.system(f'mkdir {full_output_path}')

    #convert background if input was correctly specified
    if input['bg_from'] != "NA" and input['bg_to'] != "NA":
        log_window.insert(INSERT, f"Converting background...\n")
        log_window.update()
        outfile = f"{full_output_path}/{operation_counter}_{sample_name}_bg.png"
        sutils.background_converter(image=current_file, from_color=input['bg_from'], to_color=input['bg_to'], outfile=outfile)
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
                sutils.contrast_adjuster(image=current_file, factor=operation[1], outfile=outfile)
                log_window.insert(INSERT, f"Contrast adjusted.\n")
                log_window.update()
                current_file = outfile
                operation_counter += 1

            #sharpness adjustment
            elif operation[2] == 'sharpness':
                log_window.insert(INSERT, f"Adjusting Sharpness...\n")
                log_window.update()
                outfile = f"{full_output_path}/{operation_counter}_{sample_name}_shrp.png"
                sutils.contrast_adjuster(image=current_file, factor=operation[1], outfile=outfile)
                log_window.insert(INSERT, f"Sharpness adjusted.\n")
                log_window.update()
                current_file = outfile
                operation_counter += 1

            #saturation adjustment
            elif operation[2] == 'saturation':
                log_window.insert(INSERT, f"Adjusting Saturation...\n")
                log_window.update()
                outfile = f"{full_output_path}/{operation_counter}_{sample_name}_sat.png"
                sutils.contrast_adjuster(image=current_file, factor=operation[1], outfile=outfile)
                log_window.insert(INSERT, f"Saturation adjusted.\n")
                log_window.update()
                current_file = outfile
                operation_counter += 1

    #perform k-means clustering if specified
    if input['color_number'] > 0:
        log_window.insert(INSERT, f"Performing K-means clustering...\n")
        log_window.update()
        outfile = f"{full_output_path}/{operation_counter}_{sample_name}_clst.png"
        sutils.kmeans_transformer(image=current_file, k=input['color_number'], outfile=outfile, iterations=advanced_options['kmeans_iterations'], epsilon=advanced_options['epsilon_input'], attempts=advanced_options['kmeans_attempts'])
        log_window.insert(INSERT, f"Color clustering complete.\n")
        log_window.update()
        current_file = outfile
        operation_counter += 1
    
    #perform boundary tracing
    if input['boundary_tracing_color'] != 'NA':
        log_window.insert(INSERT, f"Tracing color boundaries...\n")
        log_window.update()
        outfile = f"{full_output_path}/{operation_counter}_{sample_name}_bnd.png"
        sutils.boundary_tracer(image=current_file, color=input['boundary_tracing_color'], outfile=outfile)
        log_window.insert(INSERT, f"Boundary tracing complete.\n")
        log_window.update()
        current_file = outfile
        operation_counter += 1


def clique_main():
    #get input
    input = get_input()
    if input != 0:
        log_window.insert(INSERT, f"All input loaded successfully.\n")
        log_window.update()

    #run clique for single input file
    if 'image_file_input' in input:
        log_window.insert(INSERT, f"Working on {input['image_file_input']}.\n")
        log_window.update()
        run_clique(image=input['image_file_input'], input=input, advanced_options=advanced_segmentation_options)

    #run clique for input directory
    elif 'image_dir_input' in input:
        #MAKE INPUT FOR LATER
        file_extensions = ['png', 'jpg']
        for image in input['image_dir_input']:
            image_extension = image.split('/')[-1].split('.')[-1].lower()
            if image_extension in file_extensions:
                log_window.insert(INSERT, f"Working on {image}.\n")
                log_window.update()
                run_clique(image=image, input=input, advanced_options=advanced_segmentation_options)


#button to run clique
runButton = tk.Button(colorSegmentationTab, text="Run", command=clique_main)
runButton.grid(row=6, column=0, sticky = "ew", pady=5, padx=10)



####################   COLOR QUANTIFICATION TAB   ####################

#IMAGE INPUT LABELED FRAME
imageInputFrameQT = tk.LabelFrame(colorQuantificationTab, text="Image Upload")
imageInputFrameQT.grid(row=1, column=0, sticky = "ew", pady=5, padx=10)

#add prompt to select image file
imageSelectPromptQT = tk.Label(imageInputFrameQT, text="Image File:")
imageSelectPromptQT.grid(row=1, column=1, pady=5, padx=10)

#function to select image
def select_image_fileQT():
    filetypes = (('PNG File', '*.png'), ('All files', '*.*'))
    image_file = filedialog.askopenfilename(title="Open Files", initialdir = home_path, filetypes = filetypes)
    image_file_inputQT.delete(0, END)
    image_file_inputQT.insert(0, image_file)

#add entry for image file
image_file_inputQT = tk.Entry(imageInputFrameQT)
image_file_inputQT.grid(row=1, column=2, padx=10, pady=5)

#add button for selecting images
imageFileSelectButtonQT = tk.Button(imageInputFrameQT, text="Select File", command=select_image_fileQT)
imageFileSelectButtonQT.grid(row=1, column=3, padx=10, pady=5, sticky="w")

#add prompt to select directory containing images
imageDirSelectPromptQT = tk.Label(imageInputFrameQT, text="Directory:")
imageDirSelectPromptQT.grid(row=2, column=1, padx=10, pady=5)

#function to select image directory
def select_image_dirQT():
    image_dir = filedialog.askdirectory(title="Open Directories", initialdir = home_path)
    image_dir_inputQT.delete(0, END)
    image_dir_inputQT.insert(0, image_dir)

#add entry for selecting directory containing images
image_dir_inputQT = tk.Entry(imageInputFrameQT)
image_dir_inputQT.grid(row=2, column=2, padx=10, pady=5)

#add button for selecting directory containing images
imageDirSelectButtonQT = tk.Button(imageInputFrameQT, text="Select Folder", command=select_image_dirQT)
imageDirSelectButtonQT.grid(row=2, column=3, padx=10, pady=5, sticky="w")

#COLOR CLASSIFICATION LABELED FRAME
colorClassificationFrame = tk.LabelFrame(colorQuantificationTab, text="Color Classification")
colorClassificationFrame.grid(row=2, column=0, sticky = "ew", pady=5, padx=10)

#add table for specifying colors
colorClassifiersTable = ttk.Treeview(colorClassificationFrame, columns=(1,2), show="headings")
colorClassifiersTable.heading(1, text="RGB")
colorClassifiersTable.column(1, anchor=CENTER, width=208)
colorClassifiersTable.heading(2, text="Name")
colorClassifiersTable.column(2, anchor=CENTER, width=208)
colorClassifiersTable.grid(row=1, column=1, pady=10, padx=10, sticky='new')

#initialize a dictionary to hold color mappings
color_mappings = {}

#cache for added colors
added_colors = []

#function to add color classification
def add_color_classification_entry():
    #initialize error status 
    error = 0
    #collect input
    color_rgb = new_color_rgb_input.get()
    color_name = new_color_name_input.get()
    #check that input was specified
    if color_rgb == '' or color_name == '':
        tk.messagebox.showerror("Input Error", f"Error: Missing RGB value or color designation.")
        error += 1
    #check that rgb value is valid
    if error == 0:
        rgb_value = check_rgb_input(color_rgb)
        if rgb_value == 'Error_RGB_value':
            tk.messagebox.showerror("Input Error", f"Error: ({color_rgb}) is an invalid RGB value.")
            error += 1
        elif rgb_value == 'Error_format':
            tk.messagebox.showerror("Input Error", f"Error: ({color_rgb}) is in an invalid format.")
            error += 1
        elif color_name in added_colors:
            tk.messagebox.showerror("Input Error", f"Error: ({color_name}) has already been added.")
            error += 1
        else:
            color_mappings[color_name] = rgb_value
            added_colors.append(color_name)

#function to delete color classification
def delete_color_classification_entry():
    selected_color = colorClassifiersTable.selection()
    for selection in selected_color:
        delete_color = colorClassifiersTable.item(selection)['values'][1]
        del color_mappings[delete_color]
        try:
            colorClassifiersTable.delete(selection)
            colorQuantificationTableInclude.delete(selection)
        except:
            pass
                
        #remove from recorded colors
        added_colors.remove(delete_color)

#function for delete option popup
def delete_option(event):
    deleteOptionMenu.tk_popup(event.x_root, event.y_root)
    
#add delete option to table window
colorClassifiersTable.bind("<Button-2>", delete_option)
colorClassifiersTable.bind("<Button-3>", delete_option)

#function for adding color classification to table
def update_color_classification_view():
    add_color_classification_entry()
    #clear current entry
    for color in colorClassifiersTable.get_children():
        try:
            colorClassifiersTable.delete(color)
            colorQuantificationTableInclude.delete(color)
        except:
            pass

    #refresh entry
    for color in color_mappings:
        color_name = color
        color_rgb = ",".join([str(value) for value in color_mappings[color]])
        colorClassifiersTable.insert("", 'end', values=(color_rgb, color_name))
        colorQuantificationTableInclude.insert("", 'end', values=(color_name))

#Button for adding color
addColorPrompt = tk.Button(colorClassificationFrame, text="Add Color", command=update_color_classification_view)
addColorPrompt.grid(row=2, column=1, pady=5, padx=10)

#New color adding labels
newColorRGBColumn = tk.Label(colorClassificationFrame, text="RGB")
newColorRGBColumn.grid(row=2, column=1, sticky='w', pady=5, padx=10)

#New color adding labels
newColorNameColumn = tk.Label(colorClassificationFrame, text="Color Designation")
newColorNameColumn.grid(row=2, column=1, sticky='e', pady=5, padx=10)

#entry for specifying color RGB
new_color_rgb_input = tk.Entry(colorClassificationFrame)
new_color_rgb_input.grid(row=4, column=1, sticky='w', pady=5, padx=10)

#entry for specifying color designation
new_color_name_input = tk.Entry(colorClassificationFrame)
new_color_name_input.grid(row=4, column=1, sticky='e', pady=5, padx=10)

#options for deleting colors
deleteOptionMenu = tk.Menu(colorClassificationFrame)
deleteOptionMenu.add_command(label="Delete", command=delete_color_classification_entry)

#COLOR EXCLUSION LABELED FRAME
colorQuantificationFrame = tk.LabelFrame(colorQuantificationTab, text="Color Quantification Parameters")
colorQuantificationFrame.grid(row=3, column=0, sticky = "ew", pady=5, padx=10)

#add prompt for displaying colors to exclude in quantification
colorsToExcludePrompt = tk.Label(colorQuantificationFrame, text="Exclude")
colorsToExcludePrompt.grid(row=1, column=1, pady=5, padx=10)

#add display for selecting colors to include/exclude from quantification
#include display
colorQuantificationTableInclude = ttk.Treeview(colorQuantificationFrame, columns=(1), show="headings")
colorQuantificationTableInclude.heading(1, text="Include")
colorQuantificationTableInclude.column(1, anchor=CENTER, width=208)
colorQuantificationTableInclude.grid(row=1, column=1, pady=10, padx=10, sticky='new')

#exclude display
colorQuantificationTableExclude = ttk.Treeview(colorQuantificationFrame, columns=(1), show="headings")
colorQuantificationTableExclude.heading(1, text="Exclude")
colorQuantificationTableExclude.column(1, anchor=CENTER, width=208)
colorQuantificationTableExclude.grid(row=1, column=2, pady=10, padx=10, sticky='new')

#function to exclude color
def exclude_color_option(event):
    excludeColorOptionMenu.tk_popup(event.x_root, event.y_root)

#add exclude option to table window
colorQuantificationTableInclude.bind("<Button-2>", exclude_color_option)
colorQuantificationTableInclude.bind("<Button-3>", exclude_color_option)

#function to move color from include to exclude
def exclude_color():
    selected_color = colorQuantificationTableInclude.selection()
    for selection in selected_color:
        exclude_color = colorQuantificationTableInclude.item(selection)['values'][0]
        colorQuantificationTableExclude.insert("", 'end', values=(exclude_color))
        colorQuantificationTableInclude.delete(selection)

#option menu for excluding colors
excludeColorOptionMenu = tk.Menu(colorQuantificationFrame)
excludeColorOptionMenu.add_command(label="Exclude", command=exclude_color)

#function to include color
def include_color_option(event):
    includeColorOptionMenu.tk_popup(event.x_root, event.y_root)

#add include option to table window
colorQuantificationTableExclude.bind("<Button-2>", include_color_option)
colorQuantificationTableExclude.bind("<Button-3>", include_color_option)

#function to move color from exclude to include
def include_color():
    selected_color = colorQuantificationTableExclude.selection()
    for selection in selected_color:
        include_color = colorQuantificationTableExclude.item(selection)['values'][0]
        colorQuantificationTableInclude.insert("", 'end', values=(include_color))
        colorQuantificationTableExclude.delete(selection)

#option menu for including colors
includeColorOptionMenu = tk.Menu(colorQuantificationFrame)
includeColorOptionMenu.add_command(label="Include", command=include_color)


#LOGGING
#add progress bar
colorSegmentationProgressBarQT = Progressbar(colorQuantificationTab, orient=HORIZONTAL, mode='indeterminate', length=300)
colorSegmentationProgressBarQT.grid(row=0, column=1, sticky = "sew", pady=0, padx=10)

#LOG WINDOW LABELED FRAME
logWindowFrameQT = tk.LabelFrame(colorQuantificationTab, text="Log Window")
logWindowFrameQT.grid(row=1, column=1, sticky = "new", pady=5, padx=10, rowspan=50)

#add log window
log_window_qt = tk.Text(logWindowFrameQT, width=65, height=30)
log_window_qt.grid(row=0, column=0)


#run app
root.mainloop()