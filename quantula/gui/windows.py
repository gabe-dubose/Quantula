import tkinter as tk
from tkinter import ttk	
from tkinter.ttk import *
from tkinter import *
from tkinter import INSERT
from pandastable import Table
from quantula.gui import guiutils
from quantula import iutils
from quantula import qcdutils

#window for importing data
def import_data_window(parent):
    window = Toplevel(parent)
    window.title("Import Data")
    window.geometry('510x280')

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
    imageDirSelectButton = tk.Button(dataUploadFrame, text="Select Directory", command=lambda: guiutils.select_directory(image_dir_input))
    imageDirSelectButton.grid(row=1, column=3, padx=10, pady=5, sticky="w")

    #add prompt to select sample metadata file
    sampleMetadataSelectPrompt = tk.Label(dataUploadFrame, text="Metadata:")
    sampleMetadataSelectPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #add entry for sample metadata file
    sample_metadata_input = tk.Entry(dataUploadFrame)
    sample_metadata_input.grid(row=2, column=2, padx=10, pady=5)

    #add button for selecting sample metadata
    sampleMetadataSelectButton = tk.Button(dataUploadFrame, text="Select File", command=lambda: guiutils.select_csv_file(sample_metadata_input))
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
    outputDirSelectButton = tk.Button(dataUploadFrame, text="Select Directory", command=lambda: guiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=4, column=3, padx=10, pady=5, sticky="w")

    #add button to import images
    runImportButton = tk.Button(window, text="Import Data", command=lambda: guiutils.load_import_input(image_dir_input, sample_metadata_input, output_file_input, output_dir_input))
    runImportButton.grid(row=2, column=0, padx=10, pady=5, sticky='ew')

#window for viewing images
def view_images_window(parent):
    window = Toplevel(parent)
    window.title("Image Viewer")
    window.geometry('560x600')

    #INPUT OPTIONS FRAME
    inputFrame = tk.LabelFrame(window, text="Input options")
    inputFrame.grid(row=1, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(inputFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(inputFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(inputFrame, text="Select File", command=lambda: guiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #add button for viewing images
    viewImagesButton = tk.Button(window, text="Show Image List", command=lambda: guiutils.load_image_view(image_qcd_input, imageListTable))
    viewImagesButton.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    #IMAGE LIST FRAME
    imageListFrame = tk.LabelFrame(window, text="Loaded Images")
    imageListFrame.grid(row=3, column=1, sticky = "ew", pady=5, padx=10)

    #set style
    style = ttk.Style(imageListFrame)
    style.configure("Treeview.Heading", background="#ececec", foreground="black")
    style.map('Treeview', background=[('selected', '#BFBFBF')])
    
    #add table for specifying colors
    imageListTable = ttk.Treeview(imageListFrame, columns=(1), show="headings")
    imageListTable.heading(1, text="Image Files")
    imageListTable.column(1, anchor=CENTER, width=270)
    imageListTable.grid(row=1, column=1, pady=10, padx=10, sticky='new')

    #function to open image
    def open_image(event):
        selection = imageListTable.focus()
        items = imageListTable.item(selection)
        image_to_open = items["values"][0]
        guiutils.open_image(image_qcd_input, image_to_open)
        
    #add delete option to table window
    imageListTable.bind("<Double-Button-1>", open_image)

    #EXPORT IMAGES FRAME
    exportImagesFrame = tk.LabelFrame(window, text="Export Images")
    exportImagesFrame.grid(row=4, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to save output file
    exportImagesPrompt = tk.Label(exportImagesFrame, text="Export:")
    exportImagesPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for output directory
    output_dir_input = tk.Entry(exportImagesFrame)
    output_dir_input.grid(row=1, column=1, padx=100, pady=5, sticky='w')

    #add button for output
    outputDirSelectButton = tk.Button(exportImagesFrame, text="Select Directory", command=lambda: guiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=1, column=1, padx=(300,10), pady=5, sticky="w")

    #add button for exporting raw table
    exportRawTableButton = tk.Button(exportImagesFrame, text="Export", command=lambda: qcdutils.export_images(image_qcd_input.get(), output_dir_input.get()))
    exportRawTableButton.grid(row=1, column=1, padx=(435,10), pady=5, sticky="w")

#window for viewing tables
def view_tables_window(parent):
    window = Toplevel(parent)
    window.title("Pixel Conversion")
    window.geometry('610x770')

    #INPUT OPTIONS FRAME
    inputFrame = tk.LabelFrame(window, text="Input options")
    inputFrame.grid(row=1, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to select table qcd
    tableQCDSelectPrompt = tk.Label(inputFrame, text="Quantification table(s) (qcd):")
    tableQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    table_qcd_input = tk.Entry(inputFrame)
    table_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    tableQCDSelectButton = tk.Button(inputFrame, text="Select File", command=lambda: guiutils.select_qcd_file(table_qcd_input))
    tableQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #add prompt to select metadata
    metadataSelectPrompt = tk.Label(inputFrame, text="Metadata (csv):")
    metadataSelectPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    metadata_input = tk.Entry(inputFrame)
    metadata_input.grid(row=2, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    metadataSelectButton = tk.Button(inputFrame, text="Select File", command=lambda: guiutils.select_csv_file(metadata_input))
    metadataSelectButton.grid(row=2, column=3, padx=5, pady=5, sticky="w")

    #add button for showing table
    viewTableButton = tk.Button(window, text="Show Tables", command=lambda: guiutils.update_pandas_table(table_qcd_input, metadata_input, raw_table_view, fract_table_view))
    viewTableButton.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    #RAW TABLE VIEW FRAME
    rawTableFrame = tk.LabelFrame(window, text="Raw Counts")
    rawTableFrame.grid(row=3, column=1, sticky = "ew", pady=5, padx=10)

    raw_table_view = Table(rawTableFrame)
    raw_table_view.show()

    #add prompt to save output file
    rawOutputFilePrompt = tk.Label(window, text="Export Table:")
    rawOutputFilePrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    #add entry for output directory
    raw_output_dir_input = tk.Entry(window)
    raw_output_dir_input.grid(row=4, column=1, padx=100, pady=5, sticky='w')

    #add button for output
    outputDirSelectButton = tk.Button(window, text="Select Directory", command=lambda: guiutils.select_directory(raw_output_dir_input))
    outputDirSelectButton.grid(row=4, column=1, padx=(300,10), pady=5, sticky="w")

    #add button for exporting raw table
    exportRawTableButton = tk.Button(window, text="Export", command=lambda: guiutils.export_table(raw_table_view, raw_output_dir_input, 'raw_pixel_color_counts.csv'))
    exportRawTableButton.grid(row=4, column=1, padx=(435,10), pady=5, sticky="w")


    #FRACTIONS TABLE VIEW FRAME
    fractionsTableFrame = tk.LabelFrame(window, text="Color Fractions")
    fractionsTableFrame.grid(row=5, column=1, sticky = "ew", pady=5, padx=10)

    fract_table_view = Table(fractionsTableFrame)
    fract_table_view.show()

    #add prompt to save output file
    rawOutputFilePrompt = tk.Label(window, text="Export Table:")
    rawOutputFilePrompt.grid(row=6, column=1, pady=5, padx=10, sticky="w")

    #add entry for output directory
    fract_output_dir_input = tk.Entry(window)
    fract_output_dir_input.grid(row=6, column=1, padx=100, pady=5, sticky='w')

    #add button for output
    outputDirSelectButton = tk.Button(window, text="Select Directory", command=lambda: guiutils.select_directory(fract_output_dir_input))
    outputDirSelectButton.grid(row=6, column=1, padx=(300,10), pady=5, sticky="w")

    #add button for exporting raw table
    exportFractTableButton = tk.Button(window, text="Export", command=lambda: guiutils.export_table(fract_table_view, fract_output_dir_input, 'color_fractions.csv'))
    exportFractTableButton.grid(row=6, column=1, padx=(435,10), pady=5, sticky="w")


#window for converting pixels
def convert_pixels_window(parent):
    window = Toplevel(parent)
    window.title("Pixel Conversion")
    window.geometry('525x400')

    #INPUT OPTIONS FRAME
    inputFrame = tk.LabelFrame(window, text="Input options")
    inputFrame.grid(row=1, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(inputFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(inputFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(inputFrame, text="Select File", command=lambda: guiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #PARAMETERS FRAME
    pixelConversionParametersFrame = tk.LabelFrame(window, text="Pixel conversion parameters")
    pixelConversionParametersFrame.grid(row=2, column=1, sticky = "ew", pady=5, padx=10)

    #prompt for pixel color specification
    pixelColorPrompt = tk.Label(pixelConversionParametersFrame, text="Color (R,G,B):")
    pixelColorPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #Entry box for pixel color specification
    pixel_color_input = tk.Entry(pixelConversionParametersFrame)
    pixel_color_input.grid(row=2, column=2, padx=10, pady=5, sticky="w")

    #add pixel color checker
    bgColorFromDisplay = Canvas(pixelConversionParametersFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
    bgColorFromDisplay.grid(row=2, column=4, padx=10, sticky="e")

    #add button to check color
    bgColorFromViewButton = tk.Button(pixelConversionParametersFrame, text="View", command=lambda: guiutils.display_color_box(pixel_color_input, bgColorFromDisplay))
    bgColorFromViewButton.grid(row=2, column=3, pady=10, padx=5, sticky="w")

    #prompt for pixel color conversion specification
    pixelColorToPrompt = tk.Label(pixelConversionParametersFrame, text="Convert to (R,G,B):")
    pixelColorToPrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

    #Entry box for pixel color specification
    pixel_convert_input = tk.Entry(pixelConversionParametersFrame)
    pixel_convert_input.grid(row=3, column=2, padx=10, pady=5, sticky="w")

    #add pixel color checker
    bgColorToDisplay = Canvas(pixelConversionParametersFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
    bgColorToDisplay.grid(row=3, column=4, padx=10, sticky="e")

    #add button to check color
    bgColorFromViewButton = tk.Button(pixelConversionParametersFrame, text="View", command=lambda: guiutils.display_color_box(pixel_convert_input, bgColorToDisplay))
    bgColorFromViewButton.grid(row=3, column=3, pady=10, padx=5, sticky="w")

    #OUTPUT OPTIONS FRAME
    outputFrame = tk.LabelFrame(window, text="Output Options")
    outputFrame.grid(row=3, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to save output file
    outputFilePrompt = tk.Label(outputFrame, text="Output Name:")
    outputFilePrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(outputFrame)
    output_file_input.grid(row=4, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(outputFrame, text="Save To:")
    outputDirPrompt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

    #add entry for output directory
    output_dir_input = tk.Entry(outputFrame)
    output_dir_input.grid(row=5, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(outputFrame, text="Select Directory", command=lambda: guiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=5, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Convert Pixels", command=lambda: guiutils.convert_pixel(image_qcd_input, pixel_color_input, pixel_convert_input, output_file_input, output_dir_input))
    runButton.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

def image_resizing_window(parent):
    window = Toplevel(parent)
    window.title("Image Resizing")
    window.geometry('525x400')

    #INPUT OPTIONS FRAME
    inputFrame = tk.LabelFrame(window, text="Input options")
    inputFrame.grid(row=1, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(inputFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(inputFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(inputFrame, text="Select File", command=lambda: guiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #RESIZING PARAMETERS INPUT FRAME
    resizingParametersFrame = tk.LabelFrame(window, text="Image Resizing Parameters")
    resizingParametersFrame.grid(row=2, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt for size
    resizeSizePrompt = tk.Label(resizingParametersFrame, text="Size (w,h):")
    resizeSizePrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #add entry for resizing size
    resize_size_input = tk.Entry(resizingParametersFrame)
    resize_size_input.grid(row=2, column=2, padx=10, pady=5, sticky="w")

    #add prompt for algorithm
    resizeAlgorithmPrompt = tk.Label(resizingParametersFrame, text="Method:")
    resizeAlgorithmPrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

    #specify options for resizing method
    resizing_methods = ['Nearest Neighbor', 'Linear Interpolation', 'Cubic Spline Interpolation', 'Lanczos']
    #add ooptions menu
    resizeMethod = StringVar()
    resizeMethod.set("Nearest Neighbor")
    resizeMethodsOptionMenu = OptionMenu(resizingParametersFrame, resizeMethod, *resizing_methods)
    resizeMethodsOptionMenu.grid(row=3, column=2, pady=5, padx=10, sticky="w")

    #OUTPUT OPTIONS FRAME
    outputFrame = tk.LabelFrame(window, text="Output Options")
    outputFrame.grid(row=3, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to save output file
    outputFilePrompt = tk.Label(outputFrame, text="Output Name:")
    outputFilePrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(outputFrame)
    output_file_input.grid(row=4, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(outputFrame, text="Save To:")
    outputDirPrompt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

    #add entry for output directory
    output_dir_input = tk.Entry(outputFrame)
    output_dir_input.grid(row=5, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(outputFrame, text="Select Directory", command=lambda: guiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=5, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Resize Image", command=lambda: guiutils.resize_image(image_qcd_input, resize_size_input, resizeMethod, output_file_input, output_dir_input))
    runButton.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

#contrast adjustmnet window
def contrast_adjustment_window(parent):
    window = Toplevel(parent)
    window.title("Contrast Adjustment")
    window.geometry('500x350')

    #INPUT OPTIONS FRAME
    inputFrame = tk.LabelFrame(window, text="Input options")
    inputFrame.grid(row=1, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(inputFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(inputFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(inputFrame, text="Select File", command=lambda: guiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #CONTRAST ADJUSTMENT PARAMETERS FRAME
    contrastAdjustmentParametersFrame = tk.LabelFrame(window, text="Contrast Adjustment Parameters")
    contrastAdjustmentParametersFrame.grid(row=2, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt 
    contrastPrompt = tk.Label(contrastAdjustmentParametersFrame, text="Contrast Factor:")
    contrastPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #add scale to select contrast adjustment
    contrast_input = IntVar()
    contrastAdjustmentScale = tk.Scale(contrastAdjustmentParametersFrame, variable = contrast_input, from_ = -10, to = 10, orient = HORIZONTAL, width=20, sliderlength=20, length=185)
    contrastAdjustmentScale.grid(row=2, column=2, pady=(0,10), padx=13, sticky="w")

    #OUTPUT OPTIONS FRAME
    outputFrame = tk.LabelFrame(window, text="Output Options")
    outputFrame.grid(row=3, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to save output file
    outputFilePrompt = tk.Label(outputFrame, text="Output Name:")
    outputFilePrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(outputFrame)
    output_file_input.grid(row=4, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(outputFrame, text="Save To:")
    outputDirPrompt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

    #add entry for output directory
    output_dir_input = tk.Entry(outputFrame)
    output_dir_input.grid(row=5, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(outputFrame, text="Select Directory", command=lambda: guiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=5, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Adjust Contrast", command=lambda: guiutils.adjust_image(image_qcd_input, contrast_input, output_file_input, output_dir_input, 'contrast'))
    runButton.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

#sharpness adjustmnet window
def sharpness_adjustment_window(parent):
    window = Toplevel(parent)
    window.title("Sharpness Adjustment")
    window.geometry('500x350')

    #INPUT OPTIONS FRAME
    inputFrame = tk.LabelFrame(window, text="Input options")
    inputFrame.grid(row=1, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(inputFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(inputFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(inputFrame, text="Select File", command=lambda: guiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #SHARPNESS ADJUSTMENT PARAMETERS FRAME
    sharpnessAdjustmentParametersFrame = tk.LabelFrame(window, text="Sharpness Adjustment Parameters")
    sharpnessAdjustmentParametersFrame.grid(row=2, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt 
    sharpnessPrompt = tk.Label(sharpnessAdjustmentParametersFrame, text="Sharpness Factor:")
    sharpnessPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #add scale to select sharpness adjustment
    sharpness_input = IntVar()
    sharpnessAdjustmentScale = tk.Scale(sharpnessAdjustmentParametersFrame, variable = sharpness_input, from_ = -10, to = 10, orient = HORIZONTAL, width=20, sliderlength=20, length=185)
    sharpnessAdjustmentScale.grid(row=2, column=2, pady=(0,10), padx=13, sticky="w")

    #OUTPUT OPTIONS FRAME
    outputFrame = tk.LabelFrame(window, text="Output Options")
    outputFrame.grid(row=3, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to save output file
    outputFilePrompt = tk.Label(outputFrame, text="Output Name:")
    outputFilePrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(outputFrame)
    output_file_input.grid(row=4, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(outputFrame, text="Save To:")
    outputDirPrompt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

    #add entry for output directory
    output_dir_input = tk.Entry(outputFrame)
    output_dir_input.grid(row=5, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(outputFrame, text="Select Directory", command=lambda: guiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=5, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Adjust Sharpness", command=lambda: guiutils.adjust_image(image_qcd_input, sharpness_input, output_file_input, output_dir_input, 'sharpness'))
    runButton.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

#saturation adjustmnet window
def saturation_adjustment_window(parent):
    window = Toplevel(parent)
    window.title("Saturation Adjustment")
    window.geometry('500x350')

    #INPUT OPTIONS FRAME
    inputFrame = tk.LabelFrame(window, text="Input options")
    inputFrame.grid(row=1, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(inputFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(inputFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(inputFrame, text="Select File", command=lambda: guiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #SATURATION ADJUSTMENT PARAMETERS FRAME
    saturationAdjustmentParametersFrame = tk.LabelFrame(window, text="Saturation Adjustment Parameters")
    saturationAdjustmentParametersFrame.grid(row=2, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt 
    saturationPrompt = tk.Label(saturationAdjustmentParametersFrame, text="Saturation Factor:")
    saturationPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #add scale to select saturation adjustment
    saturation_input = IntVar()
    saturationAdjustmentScale = tk.Scale(saturationAdjustmentParametersFrame, variable = saturation_input, from_ = -10, to = 10, orient = HORIZONTAL, width=20, sliderlength=20, length=185)
    saturationAdjustmentScale.grid(row=2, column=2, pady=(0,10), padx=13, sticky="w")

    #OUTPUT OPTIONS FRAME
    outputFrame = tk.LabelFrame(window, text="Output Options")
    outputFrame.grid(row=3, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to save output file
    outputFilePrompt = tk.Label(outputFrame, text="Output Name:")
    outputFilePrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(outputFrame)
    output_file_input.grid(row=4, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(outputFrame, text="Save To:")
    outputDirPrompt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

    #add entry for output directory
    output_dir_input = tk.Entry(outputFrame)
    output_dir_input.grid(row=5, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(outputFrame, text="Select Directory", command=lambda: guiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=5, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Adjust Saturation", command=lambda: guiutils.adjust_image(image_qcd_input, saturation_input, output_file_input, output_dir_input, 'saturation'))
    runButton.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

#kmeans transformation window
def k_means_transformation_window(parent):
    window = Toplevel(parent)
    window.title("K-means Transformation")
    window.geometry('500x475')

    #INPUT OPTIONS FRAME
    inputFrame = tk.LabelFrame(window, text="Input options")
    inputFrame.grid(row=1, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(inputFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(inputFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(inputFrame, text="Select File", command=lambda: guiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #KMEANS PARAMETERS FRAME
    kmeansParametersFrame = tk.LabelFrame(window, text="K-means clustering parameters")
    kmeansParametersFrame.grid(row=2, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt 
    colorCountPrompt = tk.Label(kmeansParametersFrame, text="K (n colors):")
    colorCountPrompt.grid(row=1, column=1, pady=5, padx=(10,0), sticky="w")

    #add entry for k
    color_number_input = tk.Entry(kmeansParametersFrame)
    color_number_input.grid(row=1, column=1, padx=120, pady=5, sticky="w")

    #ADVANCED K-MEANS FRAME
    kmeansAdvancedFrame = tk.LabelFrame(kmeansParametersFrame, text="Advanced Parameters")
    kmeansAdvancedFrame.grid(row=2, column=1, sticky = "ew", pady=(5, 10), padx=10)

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

    #OUTPUT OPTIONS FRAME
    outputFrame = tk.LabelFrame(window, text="Output Options")
    outputFrame.grid(row=3, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to save output file
    outputFilePrompt = tk.Label(outputFrame, text="Output Name:")
    outputFilePrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(outputFrame)
    output_file_input.grid(row=4, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(outputFrame, text="Save To:")
    outputDirPrompt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

    #add entry for output directory
    output_dir_input = tk.Entry(outputFrame)
    output_dir_input.grid(row=5, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(outputFrame, text="Select Directory", command=lambda: guiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=5, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Perform K-means Clustering", command=lambda: guiutils.kmeans_transform(image_qcd_input, color_number_input, output_file_input, output_dir_input, epsilon_input, iterations_input, attempts_input))
    runButton.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

#re-coloring with euclidian minimization window
def euclidian_minimization_recoloring_window(parent):
    window = Toplevel(parent)
    window.title("Euclidian Minimization Re-coloring")
    window.geometry('500x600')

    #EUCLIDIAN MINIMIZATION RECOLORING FRAME
    euclidianMinimizationFrame = tk.LabelFrame(window, text="Input options")
    euclidianMinimizationFrame.grid(row=1, column=0, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(euclidianMinimizationFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(euclidianMinimizationFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(euclidianMinimizationFrame, text="Select File", command=lambda: guiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w") 

    #COLOR CLASSIFICATION LABELED FRAME
    colorClassificationFrame = tk.LabelFrame(window, text="Color Classifications")
    colorClassificationFrame.grid(row=2, column=0, sticky = "ew", pady=5, padx=10)

    #set style
    style = ttk.Style(colorClassificationFrame)
    style.configure("Treeview.Heading", background="#ececec", foreground="black")
    style.map('Treeview', background=[('selected', '#BFBFBF')])
    
    #add table for specifying colors
    colorClassifiersTable = ttk.Treeview(colorClassificationFrame, columns=(1,2), show="headings")
    colorClassifiersTable.heading(1, text="Color")
    colorClassifiersTable.column(1, anchor=CENTER, width=208)
    colorClassifiersTable.heading(2, text="RGB Value")
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
    addColorPrompt = tk.Button(colorClassificationFrame, text="Add Color", command=lambda: guiutils.update_color_classification_view(added_colors, new_color_rgb_input, new_color_name_input, color_mappings, colorClassifiersTable))
    addColorPrompt.grid(row=2, column=1, pady=5, padx=10)

    #New color adding labels
    newColorRGBColumn = tk.Label(colorClassificationFrame, text="Color")
    newColorRGBColumn.grid(row=2, column=1, sticky='w', pady=5, padx=10)

    #New color adding labels
    newColorNameColumn = tk.Label(colorClassificationFrame, text="RGB Value")
    newColorNameColumn.grid(row=2, column=1, sticky='e', pady=5, padx=10)

    #entry for specifying color RGB
    new_color_rgb_input = tk.Entry(colorClassificationFrame)
    new_color_rgb_input.grid(row=4, column=1, sticky='e', pady=5, padx=10)

    #entry for specifying color designation
    new_color_name_input = tk.Entry(colorClassificationFrame)
    new_color_name_input.grid(row=4, column=1, sticky='w', pady=5, padx=10)

    #options for deleting colors
    deleteOptionMenu = tk.Menu(colorClassificationFrame)
    deleteOptionMenu.add_command(label="Delete", command=lambda: guiutils.delete_color_classification_entry(color_mappings, added_colors, colorClassifiersTable))

    #EUCLIDIAN MINIMIZATION OUTPUT FRAME
    euclidianMinimizationOutputFrame = tk.LabelFrame(window, text="Output options")
    euclidianMinimizationOutputFrame.grid(row=3, column=0, sticky = "ew", pady=5, padx=10)

    #add prompt to save output file
    outputFilePrompt = tk.Label(euclidianMinimizationOutputFrame, text="Output Name:")
    outputFilePrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(euclidianMinimizationOutputFrame)
    output_file_input.grid(row=1, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(euclidianMinimizationOutputFrame, text="Save To:")
    outputDirPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")
    
    #add entry for output directory
    output_dir_input = tk.Entry(euclidianMinimizationOutputFrame)
    output_dir_input.grid(row=2, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(euclidianMinimizationOutputFrame, text="Select Directory", command=lambda: guiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=2, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Perform Euclidian Minimization Re-coloring", command=lambda: guiutils.euclidian_minimization_recoloring(image_qcd_input, color_mappings, output_file_input, output_dir_input))
    runButton.grid(row=4, column=0, padx=10, pady=5, sticky='ew')

#color boundary tracing window
def color_boundary_tracing_window(parent):
    window = Toplevel(parent)
    window.title("Color Boundary Tracing")
    window.geometry('525x400')

    #INPUT OPTIONS FRAME
    inputFrame = tk.LabelFrame(window, text="Input options")
    inputFrame.grid(row=1, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(inputFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(inputFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(inputFrame, text="Select File", command=lambda: guiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #BOUNDARY TRACING PARAMETERS FRAME
    boundaryTracingParametersFrame = tk.LabelFrame(window, text="Boundary tracing parameters")
    boundaryTracingParametersFrame.grid(row=2, column=1, sticky = "ew", pady=5, padx=10)

    #prompt for pixel color specification
    pixelColorPrompt = tk.Label(boundaryTracingParametersFrame, text="Color (R,G,B):")
    pixelColorPrompt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    #Entry box for pixel color specification
    pixel_color_input = tk.Entry(boundaryTracingParametersFrame)
    pixel_color_input.grid(row=2, column=2, padx=(10,0), pady=5, sticky="w")

    #add pixel color checker
    ColorDisplay = Canvas(boundaryTracingParametersFrame, highlightthickness=1, highlightbackground="black", width=40, height=10)
    ColorDisplay.grid(row=2, column=4, pady=10, padx=(5,20), sticky="e")

    #add button to check color
    ColorViewButton = tk.Button(boundaryTracingParametersFrame, text="View", command=lambda: guiutils.display_color_box(pixel_color_input, ColorDisplay))
    ColorViewButton.grid(row=2, column=3, pady=10, padx=0, sticky="w")

    #add prompt 
    boundaryThresholdPrompt = tk.Label(boundaryTracingParametersFrame, text="Boundary Threshold:")
    boundaryThresholdPrompt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

    #add scale to select contrast adjustment
    boundary_threshold_input = IntVar()
    boundaryThresholdScale = tk.Scale(boundaryTracingParametersFrame, variable = boundary_threshold_input, from_ = 1, to = 8, orient = HORIZONTAL, width=20, sliderlength=20, length=185)
    boundaryThresholdScale.grid(row=3, column=2, pady=(0,10), padx=13, sticky="w")
    boundaryThresholdScale.set(8)

    #OUTPUT OPTIONS FRAME
    outputFrame = tk.LabelFrame(window, text="Output Options")
    outputFrame.grid(row=3, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to save output file
    outputFilePrompt = tk.Label(outputFrame, text="Output Name:")
    outputFilePrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(outputFrame)
    output_file_input.grid(row=4, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(outputFrame, text="Save To:")
    outputDirPrompt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

    #add entry for output directory
    output_dir_input = tk.Entry(outputFrame)
    output_dir_input.grid(row=5, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(outputFrame, text="Select Directory", command=lambda: guiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=5, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Trace Color Boundaries", command=lambda: guiutils.trace_color_boundaries(image_qcd_input, pixel_color_input, boundary_threshold_input, output_file_input, output_dir_input))
    runButton.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

def color_quantification_window(parent):
    window = Toplevel(parent)
    window.title("Color Quantification")
    window.geometry('525x700')

    #INPUT OPTIONS FRAME
    inputFrame = tk.LabelFrame(window, text="Input options")
    inputFrame.grid(row=1, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to select image qcd
    imageQCDSelectPrompt = tk.Label(inputFrame, text="Images (qcd):")
    imageQCDSelectPrompt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    #add entry for image qcd
    image_qcd_input = tk.Entry(inputFrame)
    image_qcd_input.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    #add button for selecting images qcd
    imageQCDSelectButton = tk.Button(inputFrame, text="Select File", command=lambda: guiutils.select_qcd_file(image_qcd_input))
    imageQCDSelectButton.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    #COLOR QUANTIFICATION PARAMETERS FRAME
    colorQuantificationParametersFrame = tk.LabelFrame(window, text="Color quantification parameters")
    colorQuantificationParametersFrame.grid(row=2, column=1, sticky = "ew", pady=5, padx=10)

    #COLOR MAP VIEWING FRAME
    colorMapFrame = tk.LabelFrame(colorQuantificationParametersFrame, text="Color parameters")
    colorMapFrame.grid(row=1, column=1, sticky = "ew", pady=(10,5), padx=10)

    #add button to view color map
    viewColorMapButton = tk.Button(colorMapFrame, text="View Color Map", command=lambda: guiutils.view_color_map(image_qcd_input.get(), colorMapTable))
    viewColorMapButton.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    #set style
    style = ttk.Style(colorMapFrame)
    style.configure("Treeview.Heading", background="#ececec", foreground="black")
    style.map('Treeview', background=[('selected', '#BFBFBF')])
    
    #add table for viewing color map
    colorMapTable = ttk.Treeview(colorMapFrame, columns=(1), show="headings")
    colorMapTable.heading(1, text="Color:RGB")
    colorMapTable.column(1, anchor=CENTER, width=208)
    colorMapTable.grid(row=2, column=1, pady=10, padx=10, sticky='w')

    #add table for specifying colors to exclude
    colorExcludeTable = ttk.Treeview(colorMapFrame, columns=(1), show="headings")
    colorExcludeTable.heading(1, text="Exclude")
    colorExcludeTable.column(1, anchor=CENTER, width=208)
    colorExcludeTable.grid(row=2, column=2, pady=10, padx=10, sticky='e')

    #function to exclude color
    def exclude_color_option(event):
        excludeColorOptionMenu.tk_popup(event.x_root, event.y_root)

    #add exclude option to table window
    colorMapTable.bind("<Button-2>", exclude_color_option)
    colorMapTable.bind("<Button-3>", exclude_color_option)

    #option menu for excluding colors
    excludeColorOptionMenu = tk.Menu(colorMapFrame)
    excludeColorOptionMenu.add_command(label="Exclude", command=lambda: guiutils.exclude_color(colorMapTable, colorExcludeTable))

    #function to include color
    def include_color_option(event):
        includeColorOptionMenu.tk_popup(event.x_root, event.y_root)

    #add include option to table window
    colorExcludeTable.bind("<Button-2>", include_color_option)
    colorExcludeTable.bind("<Button-3>", include_color_option)

    #option menu for including colors
    includeColorOptionMenu = tk.Menu(colorMapFrame)
    includeColorOptionMenu.add_command(label="Include", command=lambda: guiutils.include_color(colorExcludeTable, colorMapTable))

    #RETURN OPTIONS FRAME
    returnFrame = tk.LabelFrame(colorQuantificationParametersFrame, text="Return options")
    returnFrame.grid(row=2, column=1, sticky = "ew", pady=5, padx=10)

    #add checkbutton for returning raw colors
    returnRawColors = IntVar()
    returnColorFraction = IntVar()

    #return raw colors button
    returnRawColorsButton = Checkbutton(returnFrame, text = 'Raw color counts', variable=returnRawColors, onvalue = 1, offvalue = 0)
    returnRawColorsButton.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    #return color fractions button
    returnColorFractionButton = Checkbutton(returnFrame, text = 'Color fractions', variable=returnColorFraction, onvalue = 1, offvalue = 0)
    returnColorFractionButton.grid(row=1, column=2, padx=10, pady=10, sticky="w")

    #OUTPUT OPTIONS FRAME
    outputFrame = tk.LabelFrame(window, text="Output Options")
    outputFrame.grid(row=3, column=1, sticky = "ew", pady=5, padx=10)

    #add prompt to save output file
    outputFilePrompt = tk.Label(outputFrame, text="Output Name:")
    outputFilePrompt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

    #add entry for output file
    output_file_input = tk.Entry(outputFrame)
    output_file_input.grid(row=4, column=2, padx=10, pady=5)

    #add prompt for output directory
    outputDirPrompt = tk.Label(outputFrame, text="Save To:")
    outputDirPrompt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

    #add entry for output directory
    output_dir_input = tk.Entry(outputFrame)
    output_dir_input.grid(row=5, column=2, padx=10, pady=5)

    #add button for output
    outputDirSelectButton = tk.Button(outputFrame, text="Select Directory", command=lambda: guiutils.select_directory(output_dir_input))
    outputDirSelectButton.grid(row=5, column=3, padx=5, pady=5, sticky="w")

    #add run button
    runButton = tk.Button(window, text="Quantify colors", command=lambda: guiutils.count_colors(image_qcd_input, colorExcludeTable, returnRawColors, returnColorFraction, output_file_input, output_dir_input))
    runButton.grid(row=4, column=1, padx=10, pady=5, sticky='ew')