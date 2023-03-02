#!/usr/bin/env python3

import tkinter as tk	
from tkinter import *				
from tkinter import ttk
from tkinter.ttk import *
from quantula import windows
from PIL import Image, ImageTk

#initialize main window
root = tk.Tk()
root.title("Quantula")
root.geometry("525x535")

style = Style()
style.theme_create("tabformat", settings={
        "TNotebook": {"configure": {"tabmargins": [0, 0, 0, 0]}},
        "TNotebook.Tab": {"configure": {"padding": [2, 2]},
                          "map" : {
                            "background" : [("selected", "#ececec"), ("!disabled", "#ffffff")]
                          }}})

style.theme_use("tabformat")
style.configure('TFrame', background='#ececec')

#set up tab control
tabControl = ttk.Notebook(root, height=415)
#add tabs
tabControl.grid(column=0, row=0, pady=25, padx=25, sticky="nsew")

#set up data management tab
dataManagementTab = ttk.Frame(tabControl)
dataImage=Image.open('../art/file.png')
dataImage=dataImage.resize((35, 35))
dataManagementIcon = ImageTk.PhotoImage(dataImage)
tabControl.add(dataManagementTab, text ='Data Loading', image=dataManagementIcon, compound=TOP)

#set up image adjustment tab
imageAdjustmentTab = ttk.Frame(tabControl)
editImage=Image.open('../art/edit.png')
editImage=editImage.resize((35, 35))
editIcon = ImageTk.PhotoImage(editImage)
tabControl.add(imageAdjustmentTab, text ='Image Adjustment', image=editIcon, compound=TOP)

#set up color segmentation tab
colorSegmentationTab = ttk.Frame(tabControl)
rgbImage=Image.open('../art/rgb.png')
rgbImage=rgbImage.resize((35, 35))
rgbIcon = ImageTk.PhotoImage(rgbImage)
tabControl.add(colorSegmentationTab, text ='Color Segmentation', image=rgbIcon, compound=TOP)

#set up color quantification tab
colorQuantificationTab = ttk.Frame(tabControl)
quantImage=Image.open('../art/quant.png')
quantImage=quantImage.resize((35, 35))
quantIcon = ImageTk.PhotoImage(quantImage)
tabControl.add(colorQuantificationTab, text ='Color Quantification', image=quantIcon, compound=TOP)

#####   DATA UPLOAD LABELED FRAME #####
dataUploadFrame = tk.LabelFrame(dataManagementTab, text="Data Import")
dataUploadFrame.grid(row=0, column=1, padx=10, pady=10, sticky="new")

#Direction for upoading data
dataImportMessage = "Usage: Import directory of images in PNG or JPG format to a Quantula compressed directory (QCD)"
dataImportDirections = tk.Label(dataUploadFrame, text = dataImportMessage, wraplength=400, justify=LEFT)
dataImportDirections.grid(row=1, column=0, padx=10, pady=10)

#Button for importing data window
importDataButton = tk.Button(dataUploadFrame, text="Import Data", width=10, height=2, justify=CENTER, command=lambda: windows.import_data_window(root))
importDataButton.grid(row=2, column=0, padx=10, pady=(5,10), sticky="w")

#####   PIXEL CONVERSION LABELED FRAME #####
pixelConversionFrame = tk.LabelFrame(imageAdjustmentTab, text="Pixel Conversion")
pixelConversionFrame.grid(row=0, column=1, padx=10, pady=10, sticky="new")

#Usage for pixel conversion
pixelConversionMessage = "Usage: Re-color all pixels of a specified (R,G,B) value into another specified (R,G,B) value"
pixelConversionMessage = tk.Label(pixelConversionFrame, text = pixelConversionMessage, wraplength=400, justify=LEFT)
pixelConversionMessage.grid(row=1, column=0, padx=10, pady=10)

#Button for performing pixel conversion
pixelConversionButton = tk.Button(pixelConversionFrame, text="Pixel Conversion", width=10, height=2, justify=CENTER, wraplength=100, command=lambda: windows.convert_pixels_window(root))
pixelConversionButton.grid(row=2, column=0, padx=10, pady=(5,10), sticky="w")


#####   IMAGE ADJUSTMENT LABELED FRAME #####
imageAdjustmentFrame = tk.LabelFrame(imageAdjustmentTab, text="Image Adjustment")
imageAdjustmentFrame.grid(row=1, column=1, padx=10, pady=10, sticky="new")

#Usage for image adjustments
imageAdjustmentsMessage = "Usage: Perform standard contrast, sharpness, and saturation adjustments"
imageAdjustmentsMessage = tk.Label(imageAdjustmentFrame, text = imageAdjustmentsMessage, wraplength=400, justify=LEFT)
imageAdjustmentsMessage.grid(row=1, column=0, padx=10, pady=10)

#Button for performing contrast adjustmnet
contrastAdjustButton = tk.Button(imageAdjustmentFrame, text="Contrast Adjustment", width=10, height=2, justify=CENTER, wraplength=100, command=lambda: windows.contrast_adjustment_window(root))
contrastAdjustButton.grid(row=2, column=0, padx=10, pady=(0,5), sticky="w")

#Button for performing sharpness adjustment
sharpnessAdjustButton = tk.Button(imageAdjustmentFrame, text="Sharpness Adjustment", width=10, height=2, justify=CENTER, wraplength=100, command=lambda: windows.sharpness_adjustment_window(root))
sharpnessAdjustButton.grid(row=3, column=0, padx=10, pady=5, sticky="w")

#Button for performing saturation adjustment
sharpnessAdjustButton = tk.Button(imageAdjustmentFrame, text="Saturation Adjustment", width=10, height=2, justify=CENTER, wraplength=100, command=lambda: windows.saturation_adjustment_window(root))
sharpnessAdjustButton.grid(row=4, column=0, padx=10, pady=(5,10), sticky="w")

#####   COLOR CLUSTERING AND SEGMENTATION FRAME #####
colorClusteringFrame = tk.LabelFrame(colorSegmentationTab, text="Color Clustering")
colorClusteringFrame.grid(row=1, column=1, padx=10, pady=10, sticky="new")

#Usage for color clustering
colorClusteringMessage = "Usage: Perform color clustering using K-means clustering or by Euclidian distance minimization"
colorClusteringMessage = tk.Label(colorClusteringFrame, text = colorClusteringMessage, wraplength=400, justify=LEFT)
colorClusteringMessage.grid(row=1, column=0, padx=10, pady=10)

#Button for k-means clustering
kmeansCluteringButton = tk.Button(colorClusteringFrame, text="K-means clustering", width=10, height=2, justify=CENTER, wraplength=100, command=lambda: windows.k_means_transformation_window(root))
kmeansCluteringButton.grid(row=2, column=0, padx=10, pady=(0,5), sticky="w")

#Button for euclidian minimization
euclidianMinimizationButton = tk.Button(colorClusteringFrame, text="Euclidian minimization", width=10, height=2, justify=CENTER, wraplength=100)
euclidianMinimizationButton.grid(row=3, column=0, padx=10, pady=(5,10), sticky="w")

#####   COLOR BOUNDARY TRACING LABELED FRAME #####
colorBoundaryFrame = tk.LabelFrame(colorSegmentationTab, text="Color Boundary Location")
colorBoundaryFrame.grid(row=2, column=1, padx=10, pady=10, sticky="new")

#Usage for color boundary tracing
colorBoundaryMessage = "Usage: Re-color pixels that were identified within a given threshold of a boundary limit"
colorBoundaryMessage = tk.Label(colorBoundaryFrame, text = colorBoundaryMessage, wraplength=400, justify=LEFT)
colorBoundaryMessage.grid(row=1, column=0, padx=10, pady=10)

#Button for boundary tracing
boundaryTracingButton = tk.Button(colorBoundaryFrame, text="Boundary Tracing", width=10, height=2, justify=CENTER, wraplength=100, command=lambda: windows.color_boundary_tracing(root))
boundaryTracingButton.grid(row=2, column=0, padx=10, pady=(5,10), sticky="w")

#####   COLOR QUANTIFICATION FRAME #####

colorQuantificationFrame = tk.LabelFrame(colorQuantificationTab, text="Color Classification and Quantification")
colorQuantificationFrame.grid(row=2, column=1, pady=10, padx=10, sticky = "new")

#Usage for color quantification
colorQuantMessage = "Usage: Calculate the fraction of each specified pixel value in the input images"
colorQuantMessage = tk.Label(colorQuantificationFrame, text = colorQuantMessage, wraplength=400, justify=LEFT)
colorQuantMessage.grid(row=1, column=0, padx=10, pady=10)

#Button for color quantification
colorQuantificationButton = tk.Button(colorQuantificationFrame, text="Color Quantification", width=10, height=2, justify=CENTER, wraplength=100)
colorQuantificationButton.grid(row=2, column=0, padx=10, pady=(5,10), sticky="w")

#run app
root.mainloop()