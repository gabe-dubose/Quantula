import tkinter as tk	
from tkinter import *
from tkinter import INSERT
from quantula import uiutils
from quantula import iutils

#window for importing data
def import_data_window(parent):
    window = Toplevel(parent)
    window.title("Import Data")
    window.geometry('500x250')

    #IMAGE DIRECTORY LABELED FRAME
    dataUploadFrame = tk.LabelFrame(window, text="Upload Data")
    dataUploadFrame.grid(row=1, column=0, sticky = "ew", pady=5, padx=10)

    #add prompt to select image file
    imageDirSelectPrompt = tk.Label(dataUploadFrame, text="Images:")
    imageDirSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image file
    image_dir_input = tk.Entry(dataUploadFrame)
    image_dir_input.grid(row=1, column=2, padx=10, pady=5)

    #add button for selecting images
    imageDirSelectButton = tk.Button(dataUploadFrame, text="Select Directory", command=lambda: uiutils.select_directory(image_dir_input))
    imageDirSelectButton.grid(row=1, column=3, padx=10, pady=5, sticky="w")

    #add prompt to select sample metadata file
    sampleMetadataSelectPrompt = tk.Label(dataUploadFrame, text="Metadata:")
    sampleMetadataSelectPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #add entry for sample metadata file
    sample_metadata_input = tk.Entry(dataUploadFrame)
    sample_metadata_input.grid(row=2, column=2, padx=10, pady=5)

    #add button for selecting sample metadata
    sampleMetadataSelectButton = tk.Button(dataUploadFrame, text="Select File", command=lambda: uiutils.select_csv_file(sample_metadata_input))
    sampleMetadataSelectButton.grid(row=2, column=3, padx=10, pady=5, sticky="w")

    #add prompt to save output file
    outputFilePrompt = tk.Label(dataUploadFrame, text="Output Name:")
    outputFilePrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(dataUploadFrame)
    output_file_input.grid(row=3, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(dataUploadFrame, text="Save To:")
    outputDirPrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    #add entry for output directory
    output_dir_input = tk.Entry(dataUploadFrame)
    output_dir_input.grid(row=4, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(dataUploadFrame, text="Select Directory", command=lambda: uiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=4, column=3, padx=10, pady=5, sticky="w")

    #add button to import images
    runImportButton = tk.Button(window, text="Import Data", command=lambda: uiutils.load_import_input(image_dir_input, sample_metadata_input, output_file_input, output_dir_input))
    runImportButton.grid(row=2, column=0, padx=10, pady=5, sticky='ew')


def convert_pixels_window(parent):
    window = Toplevel(parent)
    window.title("Pixel Conversion")
    window.geometry('530x300')

    #PIXEL CONVERSION LABELED FRAME
    bgConversionFrame = tk.LabelFrame(window, text="Pixel conversion parameters")
    bgConversionFrame.grid(row=1, column=0, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(bgConversionFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(bgConversionFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(bgConversionFrame, text="Select File", command=lambda: uiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #prompt for pixel color specification
    pixelColorPrompt = tk.Label(bgConversionFrame, text="Color (R,G,B):")
    pixelColorPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #Entry box for pixel color specification
    pixel_color_input = tk.Entry(bgConversionFrame)
    pixel_color_input.grid(row=2, column=2, padx=10, pady=5, sticky="w")

    #add pixel color checker
    bgColorFromDisplay = Canvas(bgConversionFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
    bgColorFromDisplay.grid(row=2, column=3, padx=10, sticky="e")

    #add button to check color
    bgColorFromViewButton = tk.Button(bgConversionFrame, text="View", command=lambda: uiutils.display_color_box(pixel_color_input, bgColorFromDisplay))
    bgColorFromViewButton.grid(row=2, column=3, pady=10, padx=5, sticky="w")

    #prompt for pixel color conversion specification
    pixelColorToPrompt = tk.Label(bgConversionFrame, text="Convert to (R,G,B):")
    pixelColorToPrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

    #Entry box for pixel color specification
    pixel_convert_input = tk.Entry(bgConversionFrame)
    pixel_convert_input.grid(row=3, column=2, padx=10, pady=5, sticky="w")

    #add pixel color checker
    bgColorToDisplay = Canvas(bgConversionFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
    bgColorToDisplay.grid(row=3, column=3, padx=10, sticky="e")

    #add button to check color
    bgColorFromViewButton = tk.Button(bgConversionFrame, text="View", command=lambda: uiutils.display_color_box(pixel_convert_input, bgColorToDisplay))
    bgColorFromViewButton.grid(row=3, column=3, pady=10, padx=5, sticky="w")

    #add prompt to save output file
    outputFilePrompt = tk.Label(bgConversionFrame, text="Output Name:")
    outputFilePrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(bgConversionFrame)
    output_file_input.grid(row=4, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(bgConversionFrame, text="Save To:")
    outputDirPrompt.grid(row=5, column=1, pady=5, padx=10, sticky="w")
    #add entry for output directory
    output_dir_input = tk.Entry(bgConversionFrame)
    output_dir_input.grid(row=5, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(bgConversionFrame, text="Select Directory", command=lambda: uiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=5, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Convert Pixels", command=lambda: uiutils.convert_pixel(image_qcd_input, pixel_color_input, pixel_convert_input, output_file_input, output_dir_input))
    runButton.grid(row=2, column=0, padx=10, pady=5, sticky='ew')

#contrast adjustmnet window
def contrast_adjustment_window(parent):
    window = Toplevel(parent)
    window.title("Contrast Adjustment")
    window.geometry('530x300')

    #CONTRAST ADJUSTMENT LABELED FRAME
    contrastAdjustmentFrame = tk.LabelFrame(window, text="Contrast Adjustment Parameters")
    contrastAdjustmentFrame.grid(row=1, column=0, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(contrastAdjustmentFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(contrastAdjustmentFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(contrastAdjustmentFrame, text="Select File", command=lambda: uiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #add prompt 
    contrastPrompt = tk.Label(contrastAdjustmentFrame, text="Contrast Factor:")
    contrastPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #add scale to select contrast adjustment
    contrast_input = IntVar()
    contrastAdjustmentScale = tk.Scale(contrastAdjustmentFrame, variable = contrast_input, from_ = -10, to = 10, orient = HORIZONTAL, width=20, sliderlength=20, length=185)
    contrastAdjustmentScale.grid(row=2, column=2, pady=(0,10), padx=13, sticky="w")

    #add prompt to save output file
    outputFilePrompt = tk.Label(contrastAdjustmentFrame, text="Output Name:")
    outputFilePrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(contrastAdjustmentFrame)
    output_file_input.grid(row=3, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(contrastAdjustmentFrame, text="Save To:")
    outputDirPrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")
    #add entry for output directory
    output_dir_input = tk.Entry(contrastAdjustmentFrame)
    output_dir_input.grid(row=4, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(contrastAdjustmentFrame, text="Select Directory", command=lambda: uiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=4, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Adjust Contrast", command=lambda: uiutils.adjust_image(image_qcd_input, contrast_input, output_file_input, output_dir_input, 'contrast'))
    runButton.grid(row=4, column=0, padx=10, pady=5, sticky='ew')

#sharpness adjustmnet window
def sharpness_adjustment_window(parent):
    window = Toplevel(parent)
    window.title("Sharpness Adjustment")
    window.geometry('530x300')

    #SHARPNESS ADJUSTMENT LABELED FRAME
    sharpnessAdjustmentFrame = tk.LabelFrame(window, text="Sharpness Adjustment Parameters")
    sharpnessAdjustmentFrame.grid(row=1, column=0, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(sharpnessAdjustmentFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(sharpnessAdjustmentFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(sharpnessAdjustmentFrame, text="Select File", command=lambda: uiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #add prompt 
    sharpnessPrompt = tk.Label(sharpnessAdjustmentFrame, text="Sharpness Factor:")
    sharpnessPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #add scale to select sharpness adjustment
    sharpness_input = IntVar()
    sharpnessAdjustmentScale = tk.Scale(sharpnessAdjustmentFrame, variable = sharpness_input, from_ = -10, to = 10, orient = HORIZONTAL, width=20, sliderlength=20, length=185)
    sharpnessAdjustmentScale.grid(row=2, column=2, pady=(0,10), padx=13, sticky="w")

    #add prompt to save output file
    outputFilePrompt = tk.Label(sharpnessAdjustmentFrame, text="Output Name:")
    outputFilePrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(sharpnessAdjustmentFrame)
    output_file_input.grid(row=3, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(sharpnessAdjustmentFrame, text="Save To:")
    outputDirPrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")
    #add entry for output directory
    output_dir_input = tk.Entry(sharpnessAdjustmentFrame)
    output_dir_input.grid(row=4, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(sharpnessAdjustmentFrame, text="Select Directory", command=lambda: uiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=4, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Adjust Sharpness", command=lambda: uiutils.adjust_image(image_qcd_input, sharpness_input, output_file_input, output_dir_input, 'sharpness'))
    runButton.grid(row=4, column=0, padx=10, pady=5, sticky='ew')

#saturation adjustmnet window
def saturation_adjustment_window(parent):
    window = Toplevel(parent)
    window.title("Saturation Adjustment")
    window.geometry('530x300')

    #SATURATION ADJUSTMENT LABELED FRAME
    saturationAdjustmentFrame = tk.LabelFrame(window, text="Saturation Adjustment Parameters")
    saturationAdjustmentFrame.grid(row=1, column=0, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(saturationAdjustmentFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(saturationAdjustmentFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(saturationAdjustmentFrame, text="Select File", command=lambda: uiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #add prompt 
    saturationPrompt = tk.Label(saturationAdjustmentFrame, text="Saturation Factor:")
    saturationPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #add scale to select saturation adjustment
    saturation_input = IntVar()
    saturationAdjustmentScale = tk.Scale(saturationAdjustmentFrame, variable = saturation_input, from_ = -10, to = 10, orient = HORIZONTAL, width=20, sliderlength=20, length=185)
    saturationAdjustmentScale.grid(row=2, column=2, pady=(0,10), padx=13, sticky="w")

    #add prompt to save output file
    outputFilePrompt = tk.Label(saturationAdjustmentFrame, text="Output Name:")
    outputFilePrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(saturationAdjustmentFrame)
    output_file_input.grid(row=3, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(saturationAdjustmentFrame, text="Save To:")
    outputDirPrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    #add entry for output directory
    output_dir_input = tk.Entry(saturationAdjustmentFrame)
    output_dir_input.grid(row=4, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(saturationAdjustmentFrame, text="Select Directory", command=lambda: uiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=4, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Adjust Saturation", command=lambda: uiutils.adjust_image(image_qcd_input, saturation_input, output_file_input, output_dir_input, 'saturation'))
    runButton.grid(row=4, column=0, padx=10, pady=5, sticky='ew')

#kmeans transformation window
def k_means_transformation_window(parent):
    window = Toplevel(parent)
    window.title("K-means Transformation")
    window.geometry('495x400')

    #GENERAL K-MEANS FRAME
    kmeansAdjustmentFrame = tk.LabelFrame(window, text="K-means Clustering Parameters")
    kmeansAdjustmentFrame.grid(row=1, column=0, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(kmeansAdjustmentFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(kmeansAdjustmentFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(kmeansAdjustmentFrame, text="Select File", command=lambda: uiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #add prompt 
    colorCountPrompt = tk.Label(kmeansAdjustmentFrame, text="K (n colors):")
    colorCountPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #add entry for k
    color_number_input = tk.Entry(kmeansAdjustmentFrame)
    color_number_input.grid(row=2, column=2, padx=10, pady=5, sticky="w")

    #add prompt to save output file
    outputFilePrompt = tk.Label(kmeansAdjustmentFrame, text="Output Name:")
    outputFilePrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(kmeansAdjustmentFrame)
    output_file_input.grid(row=3, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(kmeansAdjustmentFrame, text="Save To:")
    outputDirPrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")
    
    #add entry for output directory
    output_dir_input = tk.Entry(kmeansAdjustmentFrame)
    output_dir_input.grid(row=4, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(kmeansAdjustmentFrame, text="Select Directory", command=lambda: uiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=4, column=3, padx=5, pady=5, sticky="w")

    #ADVANCED K-MEANS FRAME
    kmeansAdvancedFrame = tk.LabelFrame(window, text="Advanced K-means Clustering Parameters")
    kmeansAdvancedFrame.grid(row=2, column=0, sticky = "ew", pady=5, padx=10)

    #add prompt for epsilon 
    colorCountPrompt = tk.Label(kmeansAdvancedFrame, text="ε (neighbor distance):")
    colorCountPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for ε
    epsilon_input = tk.Entry(kmeansAdvancedFrame)
    epsilon_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    epsilon_input.insert(INSERT, "0.85")

    #add prompt for iterations
    iterationsPrompt = tk.Label(kmeansAdvancedFrame, text="Iterations:")
    iterationsPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #add entry for iterations
    iterations_input = tk.Entry(kmeansAdvancedFrame)
    iterations_input.grid(row=2, column=2, padx=10, pady=5, sticky="w")
    iterations_input.insert(INSERT, "100")

    #add prompt for attempts
    iterationsPrompt = tk.Label(kmeansAdvancedFrame, text="Attempts:")
    iterationsPrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

    #add entry for iterations
    attempts_input = tk.Entry(kmeansAdvancedFrame)
    attempts_input.grid(row=3, column=2, padx=10, pady=5, sticky="w")
    attempts_input.insert(INSERT, "10")

    #add run button
    runButton = tk.Button(window, text="Perform K-means Clustering", command=lambda: uiutils.kmeans_transform(image_qcd_input, color_number_input, output_file_input, output_dir_input, epsilon_input, iterations_input, attempts_input))
    runButton.grid(row=4, column=0, padx=10, pady=5, sticky='ew')

#color boundary tracing window
def color_boundary_tracing(parent):
    window = Toplevel(parent)
    window.title("Color Boundary Tracing")
    window.geometry('560x300')

    #GENERAL COLOR BOUNDARY TRACING WINDOW
    colorBoundaryTracingFrame = tk.LabelFrame(window, text="Color Boundary Tracing Parameters")
    colorBoundaryTracingFrame.grid(row=1, column=0, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(colorBoundaryTracingFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(colorBoundaryTracingFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(colorBoundaryTracingFrame, text="Select File", command=lambda: uiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #prompt for pixel color specification
    pixelColorPrompt = tk.Label(colorBoundaryTracingFrame, text="Color (R,G,B):")
    pixelColorPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #Entry box for pixel color specification
    pixel_color_input = tk.Entry(colorBoundaryTracingFrame)
    pixel_color_input.grid(row=2, column=2, padx=10, pady=5, sticky="w")

    #add pixel color checker
    ColorDisplay = Canvas(colorBoundaryTracingFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
    ColorDisplay.grid(row=2, column=3, pady=10, padx=(0,10), sticky="e")

    #add button to check color
    ColorViewButton = tk.Button(colorBoundaryTracingFrame, text="View", command=lambda: uiutils.display_color_box(pixel_color_input, ColorDisplay))
    ColorViewButton.grid(row=2, column=3, pady=10, padx=(10,0), sticky="w")

    #add prompt 
    boundaryThresholdPrompt = tk.Label(colorBoundaryTracingFrame, text="Boundary Threshold:")
    boundaryThresholdPrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

    #add scale to select contrast adjustment
    boundary_threshold_input = IntVar()
    boundaryThresholdScale = tk.Scale(colorBoundaryTracingFrame, variable = boundary_threshold_input, from_ = 1, to = 8, orient = HORIZONTAL, width=20, sliderlength=20, length=185)
    boundaryThresholdScale.grid(row=3, column=2, pady=(0,10), padx=13, sticky="w")
    boundaryThresholdScale.set(8)

    #add prompt to save output file
    outputFilePrompt = tk.Label(colorBoundaryTracingFrame, text="Output Name:")
    outputFilePrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(colorBoundaryTracingFrame)
    output_file_input.grid(row=4, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(colorBoundaryTracingFrame, text="Save To:")
    outputDirPrompt.grid(row=5, column=1, pady=5, padx=10, sticky="w")
    
    #add entry for output directory
    output_dir_input = tk.Entry(colorBoundaryTracingFrame)
    output_dir_input.grid(row=5, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(colorBoundaryTracingFrame, text="Select Directory", command=lambda: uiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=5, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Trace Color Boundaries", command=lambda: uiutils.trace_color_boundaries(image_qcd_input, pixel_color_input, boundary_threshold_input, output_file_input, output_dir_input))
    runButton.grid(row=6, column=0, padx=10, pady=5, sticky='ew')