import tkinter as tk	
from tkinter import *
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


def convert_background_window(parent):
    window = Toplevel(parent)
    window.title("Background Conversion")
    window.geometry('530x300')

    #BACKGROUND CONVERSION LABELED FRAME
    bgConversionFrame = tk.LabelFrame(window, text="Background conversion parameters")
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

    #prompt for background color specification
    backgroundColorPrompt = tk.Label(bgConversionFrame, text="Color (R,G,B):")
    backgroundColorPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #Entry box for background color specification
    background_color_input = tk.Entry(bgConversionFrame)
    background_color_input.grid(row=2, column=2, padx=10, pady=5, sticky="w")

    #add background color checker
    bgColorFromDisplay = Canvas(bgConversionFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
    bgColorFromDisplay.grid(row=2, column=3, padx=10, sticky="e")

    #add button to check color
    bgColorFromViewButton = tk.Button(bgConversionFrame, text="View", command=lambda: uiutils.display_color_box(background_color_input, bgColorFromDisplay))
    bgColorFromViewButton.grid(row=2, column=3, pady=10, padx=5, sticky="w")

    #prompt for background color conversion specification
    backgroundColorToPrompt = tk.Label(bgConversionFrame, text="Convert to (R,G,B):")
    backgroundColorToPrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

    #Entry box for background color specification
    background_convert_input = tk.Entry(bgConversionFrame)
    background_convert_input.grid(row=3, column=2, padx=10, pady=5, sticky="w")

    #add background color checker
    bgColorToDisplay = Canvas(bgConversionFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
    bgColorToDisplay.grid(row=3, column=3, padx=10, sticky="e")

    #add button to check color
    bgColorFromViewButton = tk.Button(bgConversionFrame, text="View", command=lambda: uiutils.display_color_box(background_convert_input, bgColorToDisplay))
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
    runButton = tk.Button(window, text="Convert Pixels", command=lambda: uiutils.convert_background(image_qcd_input, background_color_input, background_convert_input, output_file_input, output_dir_input))
    runButton.grid(row=2, column=0, padx=10, pady=5, sticky='ew')

#contrast adjustmnet window
def contrast_adjustment_window(parent):
    window = Toplevel(parent)
    window.title("Background Conversion")
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
    contrastAdjustmentScale.grid(row=2, column=2, pady=5, padx=10, sticky="w")

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