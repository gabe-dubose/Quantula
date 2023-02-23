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
from clique import iutils
from clique import windows
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

#add entry for image file
image_file_input = tk.Entry(imageInputFrame)
image_file_input.grid(row=1, column=2, padx=10, pady=5)

#add button for selecting images
imageFileSelectButton = tk.Button(imageInputFrame, text="Select File", command=lambda: iutils.select_image_file(image_file_input, home_path))
imageFileSelectButton.grid(row=1, column=3, padx=10, pady=5, sticky="w")

#add prompt to select directory containing images
imageDirSelectPrompt = tk.Label(imageInputFrame, text="Directory:")
imageDirSelectPrompt.grid(row=2, column=1, padx=10, pady=5)

#add entry for selecting directory containing images
image_dir_input = tk.Entry(imageInputFrame)
image_dir_input.grid(row=2, column=2, padx=10, pady=5)

#add button for selecting directory containing images
imageDirSelectButton = tk.Button(imageInputFrame, text="Select Folder", command=lambda: iutils.select_directory(image_dir_input, home_path))
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

#add background color checker
bgColorDisplay = Canvas(backgroundConversionFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
bgColorDisplay.grid(row=1, column=4, padx=10)

#add button to check color
bgColorViewButton = tk.Button(backgroundConversionFrame, text="View", command=lambda: iutils.display_color_box(background_color_input, bgColorDisplay))
bgColorViewButton.grid(row=1, column=3, pady=10, padx=5)

#prompt for background conversion color specification
backgroundColorPrompt = tk.Label(backgroundConversionFrame, text="Convert to (R,G,B):", padx=10, pady=5)
backgroundColorPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

#Entry box for background color specification
color_convert_input = tk.Entry(backgroundConversionFrame, width=14)
color_convert_input.grid(row=2, column=2, padx=10, pady=5, sticky="w")

#set default background color
color_convert_input.insert(0, '0,0,255')

#add background color checker
bgColorConvertDisplay = Canvas(backgroundConversionFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
bgColorConvertDisplay.grid(row=2, column=4, padx=10)

#add button to check color
bgColorConvertViewButton = tk.Button(backgroundConversionFrame, text="View", command=lambda: iutils.display_color_box(color_convert_input, bgColorConvertDisplay))
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

#add background color checker
boundaryColorConvertDisplay = Canvas(colorSegmentationFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
boundaryColorConvertDisplay.grid(row=2, column=4, padx=10)

#add button to check color
bgColorConvertViewButton = tk.Button(colorSegmentationFrame, text="View", command=lambda: iutils.display_color_box(boundary_color_input, boundaryColorConvertDisplay))
bgColorConvertViewButton.grid(row=2, column=3, pady=10, padx=5)

#OUTPUT LABELED FRAME
outputFrame = tk.LabelFrame(colorSegmentationTab, text="Output Options")
outputFrame.grid(row=5, column=0, sticky = "ew", pady=5, padx=10)

#add prompt to select output directory 
imageDirSelectPrompt = tk.Label(outputFrame, text="Directory:", padx=10, pady=5)
imageDirSelectPrompt.grid(row=1, column=1, padx=10, pady=5)

#add entry for selecting output directory 
out_dir_input = tk.Entry(outputFrame)
out_dir_input.grid(row=1, column=2, padx=10, pady=5)
out_dir_input.insert(0, home_path)

#add button for selecting output directory 
outDirSelectButton = tk.Button(outputFrame, text="Select Folder", command=lambda: iutils.select_directory(out_dir_input, home_path))
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

#add entry for metadata file
metadata_file_input = tk.Entry(metaDataFrame)
metadata_file_input.grid(row=1, column=2, padx=10, pady=5)

#add metadata select button
metadataSelectButton = tk.Button(metaDataFrame, text="Select File", command=lambda: iutils.select_csv_file(metadata_file_input, home_path))
metadataSelectButton.grid(row=1, column=3, pady=10, sticky="w")

#add prompt to select metadata dir
metadataDirSelectPrompt = tk.Label(metaDataFrame, text="New File:")
metadataDirSelectPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

#add entry for image file
metadata_dir_input = tk.Entry(metaDataFrame)
metadata_dir_input.grid(row=2, column=2, padx=10, pady=5)

#add metadata select button
metadataDirSelectButton = tk.Button(metaDataFrame, text="Select Folder", command=lambda: iutils.select_directory(metadata_dir_input, home_path))
metadataDirSelectButton.grid(row=2, column=3, pady=5, padx=(0,10))

#initialize dictionary for advacned segmentaiton options
advanced_segmentation_options = windows.advanced_segmentation_options

#add advanced options
advancedOptionsButton = tk.Button(colorSegmentationTab, text="Advanced options", command=lambda: windows.advanced_segmentation_window(root, advanced_segmentation_options))
advancedOptionsButton.grid(row=5, column=1, sticky = "sew", pady=5, padx=10)

#store sets of common resets
image_adjustment_scales = [contrastAdjustmentScale, sharpnessAdjustmentScale, saturationAdjustmentScale]
inputs_to_blank = [image_file_input, image_dir_input, rename_input, metadata_file_input, metadata_dir_input, out_dir_input]
value_resets = [[background_color_input, '0,0,0'], [color_convert_input, '0,0,255'], [boundary_color_input, '255,0,0'], [color_number_input, 0]]
operation_boxes = [contrast_order_input, sharpness_order_input, saturation_order_input]
text_resets = [log_window]

#add clear run button
clearRunButton = tk.Button(colorSegmentationTab, text="Reset Run", command=lambda: iutils.reset_run(image_adjustment_scales, inputs_to_blank, value_resets, operation_boxes, text_resets))
clearRunButton.grid(row=6, column=1, sticky = "ew", pady=5, padx=10)

def clique_segmentation():
    #get input
    input = iutils.get_standard_user_segmentation_input(image_file_input, image_dir_input, background_color_input, color_convert_input, contrast_input, contrast_order_input, sharpness_input, sharpness_order_input, saturation_input, saturation_order_input, color_number_input, boundary_color_input, out_dir_input, rename_input, metadata_file_input, metadata_dir_input)
    if input != 0:
        log_window.insert(INSERT, f"All input loaded successfully.\n")
        log_window.update()

    #run clique for single input file
    if 'image_file_input' in input:
        log_window.insert(INSERT, f"Working on {input['image_file_input']}.\n")
        log_window.update()
        sutils.segment_colors_ui(image=input['image_file_input'], input=input, advanced_options=advanced_segmentation_options, log_window=log_window)

    #run clique for input directory
    elif 'image_dir_input' in input:
        #MAKE INPUT FOR LATER
        file_extensions = ['png', 'jpg']
        for image in input['image_dir_input']:
            image_extension = image.split('/')[-1].split('.')[-1].lower()
            if image_extension in file_extensions:
                log_window.insert(INSERT, f"Working on {image}.\n")
                log_window.update()
                sutils.segment_colors_ui(image=image, input=input, advanced_options=advanced_segmentation_options, log_window=log_window)


#button to run clique color segmentation
runSegmentationButton = tk.Button(colorSegmentationTab, text="Run", command=clique_segmentation)
runSegmentationButton.grid(row=6, column=0, sticky = "ew", pady=5, padx=10)


####################   COLOR QUANTIFICATION TAB   ####################

#IMAGE INPUT LABELED FRAME
imageInputFrameQT = tk.LabelFrame(colorQuantificationTab, text="Image Upload")
imageInputFrameQT.grid(row=1, column=0, sticky = "ew", pady=5, padx=10)

#add prompt to select image file
imageSelectPromptQT = tk.Label(imageInputFrameQT, text="Image File:")
imageSelectPromptQT.grid(row=1, column=1, pady=5, padx=10)

#add entry for image file
image_file_inputQT = tk.Entry(imageInputFrameQT)
image_file_inputQT.grid(row=1, column=2, padx=10, pady=5)

#add button for selecting imagesselect_image_file
imageFileSelectButtonQT = tk.Button(imageInputFrameQT, text="Select File", command=lambda: iutils.select_image_file(image_file_inputQT, home_path))
imageFileSelectButtonQT.grid(row=1, column=3, padx=10, pady=5, sticky="w")

#add prompt to select directory containing images
imageDirSelectPromptQT = tk.Label(imageInputFrameQT, text="Directory:")
imageDirSelectPromptQT.grid(row=2, column=1, padx=10, pady=5)

#add entry for selecting directory containing images
image_dir_inputQT = tk.Entry(imageInputFrameQT)
image_dir_inputQT.grid(row=2, column=2, padx=10, pady=5)

#add button for selecting directory containing images
imageDirSelectButtonQT = tk.Button(imageInputFrameQT, text="Select Folder", command=lambda: iutils.select_directory(image_dir_inputQT, home_path))
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

#function for delete option popup
def delete_option(event):
    deleteOptionMenu.tk_popup(event.x_root, event.y_root)
    
#add delete option to table window
colorClassifiersTable.bind("<Button-2>", delete_option)
colorClassifiersTable.bind("<Button-3>", delete_option)

#Button for adding color
addColorPrompt = tk.Button(colorClassificationFrame, text="Add Color", command=lambda: iutils.update_color_classification_view(added_colors, new_color_rgb_input, new_color_name_input, color_mappings, colorClassifiersTable, colorQuantificationTableInclude))
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
deleteOptionMenu.add_command(label="Delete", command=lambda: iutils.delete_color_classification_entry(color_mappings, added_colors, colorClassifiersTable, colorQuantificationTableInclude))

#COLOR EXCLUSION LABELED FRAME
colorQuantificationFrame = tk.LabelFrame(colorQuantificationTab, text="Color Quantification Parameters")
colorQuantificationFrame.grid(row=3, column=0, sticky = "ew", pady=5, padx=10)

#add prompt for displaying colors to exclude in quantification
colorsToExcludePrompt = tk.Label(colorQuantificationFrame, text="Exclude")
colorsToExcludePrompt.grid(row=1, column=1, pady=5, padx=10)

#add display for selecting colors to include/exclude from quantification
#include display
colorQuantificationTableInclude = ttk.Treeview(colorQuantificationFrame, columns=(1), show="headings", height=7)
colorQuantificationTableInclude.heading(1, text="Include")
colorQuantificationTableInclude.column(1, anchor=CENTER, width=208)
colorQuantificationTableInclude.grid(row=1, column=1, pady=10, padx=10, sticky='new')

#exclude display
colorQuantificationTableExclude = ttk.Treeview(colorQuantificationFrame, columns=(1), show="headings", height=7)
colorQuantificationTableExclude.heading(1, text="Exclude")
colorQuantificationTableExclude.column(1, anchor=CENTER, width=208)
colorQuantificationTableExclude.grid(row=1, column=2, pady=10, padx=10, sticky='new')

#function to exclude color
def exclude_color_option(event):
    excludeColorOptionMenu.tk_popup(event.x_root, event.y_root)

#add exclude option to table window
colorQuantificationTableInclude.bind("<Button-2>", exclude_color_option)
colorQuantificationTableInclude.bind("<Button-3>", exclude_color_option)

#option menu for excluding colors
excludeColorOptionMenu = tk.Menu(colorQuantificationFrame)
excludeColorOptionMenu.add_command(label="Exclude", command=lambda: iutils.exclude_color(colorQuantificationTableInclude, colorQuantificationTableExclude))

#function to include color
def include_color_option(event):
    includeColorOptionMenu.tk_popup(event.x_root, event.y_root)

#add include option to table window
colorQuantificationTableExclude.bind("<Button-2>", include_color_option)
colorQuantificationTableExclude.bind("<Button-3>", include_color_option)

#option menu for including colors
includeColorOptionMenu = tk.Menu(colorQuantificationFrame)
includeColorOptionMenu.add_command(label="Include", command=lambda: iutils.include_color(colorQuantificationTableExclude, colorQuantificationTableInclude))

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

def clique_quantification():
    input = iutils.get_quantification_parameters(image_file_inputQT, image_dir_inputQT, colorQuantificationTableExclude, color_mappings)
    
    #single image run
    if 'image_file' in input:
        qutils.quantify_colors_ui(image=input['image_file'], input=input)

#button to run quantification
runQuantificationButton = tk.Button(colorQuantificationTab, text="Run", command=clique_quantification)
runQuantificationButton.grid(row=4, column=0, sticky = "ew", pady=5, padx=10)

#run app
root.mainloop()