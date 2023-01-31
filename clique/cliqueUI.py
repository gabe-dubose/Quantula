#!/usr/bin/env python3

import tkinter as tk
from tkinter import DISABLED, END, INSERT, filedialog
from tkinter import *
import os
from clique import utils

class CLIQUE(tk.Tk):
    #initialize with variable positional and key arguments
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #create container for frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        #initialize dictionary to store frames
        self.frames = {}
        #set up main frames
        self.title("CLIQUE")
        self.geometry("835x835")
        #iterate through frames and add to frames dictionary
        for P in (cliqueMain, helpPage):
            frame = P(container, self)
            self.frames[P] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(cliqueMain)
        #function to call frames
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class cliqueMain(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        #get home directory
        home_path = os.path.expanduser('~')

        #add program option buttons
        colorSegmentationButton = tk.Button(self, text="Color Segmentation", command = lambda: controller.show_frame(cliqueMain))
        colorSegmentationButton.grid(row=1, column=2, padx=0, pady=(10,2), sticky=E)
        colorQuantificationButton = tk.Button(self, text="Color Quantification", command = lambda: controller.show_frame(cliqueMain))
        colorQuantificationButton.grid(row=1, column=3, padx=0, pady=(10,2), sticky=W)

        #set up image input labeled frame
        image_input_frame = tk.LabelFrame(self, text="Image Upload")
        image_input_frame.grid(row=2, column=2, rowspan=5, columnspan=3, padx=10, pady=10)

        #prompt to select an image file
        image_select_prompt = tk.Label(image_input_frame, text="Image File:", padx=10, pady=10)
        image_select_prompt.grid(row=2, column=1)
        #function to select image
        def select_image_file():
            filetypes = (('PNG File', '*.png'), ('All files', '*.*'))
            image_file = filedialog.askopenfilename(title="Open Files", initialdir = home_path, filetypes = filetypes)
            image_file_input.delete(0, END)
            image_file_input.insert(0, image_file)
        #add entry for image file
        image_file_input = tk.Entry(image_input_frame)
        image_file_input.grid(row=2, column=2, padx=0, pady=10)
        #add button for selecting images
        image_file_select_button = tk.Button(image_input_frame, text="Select File", command=select_image_file)
        image_file_select_button.grid(row=2, column=3, padx=10, pady=10)

        #prompt to select an directory of images
        imagedir_select_prompt = tk.Label(image_input_frame, text="Directory:   ", padx=10, pady=10)
        imagedir_select_prompt.grid(row=3, column=1)
        #function to select image
        def select_image_dir():
            image_dir = filedialog.askdirectory(title="Open Directories", initialdir = home_path)
            image_dir_input.delete(0, END)
            image_dir_input.insert(0, image_dir)
        #add entry for image file
        image_dir_input = tk.Entry(image_input_frame)
        image_dir_input.grid(row=3, column=2, padx=0, pady=10)
        #add button for selecting images
        image_dir_select_button = tk.Button(image_input_frame, text="Select Folder", command=select_image_dir)
        image_dir_select_button.grid(row=3, column=3, padx=(0,2), pady=10)

        #set up run parameters labeled frame
        parameters_input_frame = tk.LabelFrame(self, text="Background Conversion")
        parameters_input_frame.grid(row=7, column=1, rowspan=5, columnspan=3, padx=10, pady=10)

        #prompt for background color specification
        background_color_prompt = tk.Label(parameters_input_frame, text="Color: (R,G,B)         ", padx=10, pady=10)
        background_color_prompt.grid(row=3, column=1)
        #Entry box for background color specification
        background_color_input = tk.Entry(parameters_input_frame, width=14)
        background_color_input.grid(row=3, column=2, padx=(3,3), pady=10)
        #set default background color
        background_color_input.insert(0, '0,0,0')
        #function to convert RGB values to tkinter-readable values
        def convert_rgb(rgb_values):
            r,g,b = rgb_values
            return f'#{r:02x}{g:02x}{b:02x}'
        
        #add function to check background color
        def display_bg_from_color():
            rgb_values = background_color_input.get()
            rgb_values = tuple([int(value) for value in rgb_values.split(',')])
            rgb_values = convert_rgb(rgb_values)
            bg_color_display.configure(bg=rgb_values)

        #add background color checker
        bg_color_display = Canvas(parameters_input_frame, highlightthickness=1, highlightbackground="black", width=20, height=10)
        bg_color_display.grid(row=3, column=4, padx=(2,10))

        #add button to check color
        bg_color_view_button = tk.Button(parameters_input_frame, text="View", command=display_bg_from_color)
        bg_color_view_button.grid(row=3, column=3, padx=(0,10), pady=10)

        #prompt for background color conversion specification
        color_convert_prompt = tk.Label(parameters_input_frame, text="Convert to: (R,G,B)", padx=10, pady=10, anchor='w')
        color_convert_prompt.grid(row=4, column=1)
        #Entry box for background color specification
        color_convert_input = tk.Entry(parameters_input_frame, width=14)
        color_convert_input.grid(row=4, column=2, padx=(10,3), pady=10)
        #set default background color
        color_convert_input.insert(0, '0,0,255')
        
        #add function to check background color
        def display_bg_to_color():
            rgb_values = color_convert_input.get()
            rgb_values = tuple([int(value) for value in rgb_values.split(',')])
            rgb_values = convert_rgb(rgb_values)
            color_convert_display.configure(bg=rgb_values)

        #add background color checker
        color_convert_display = Canvas(parameters_input_frame, highlightthickness=1, highlightbackground="black", width=20, height=10)
        color_convert_display.grid(row=4, column=4, padx=(2,10))

        #add button to check color
        color_convert_view_button = tk.Button(parameters_input_frame, text="View", command=display_bg_to_color)
        color_convert_view_button.grid(row=4, column=3, padx=(0,10), pady=10)

        #add image alteration labeled frame
        image_adjust_frame = tk.LabelFrame(self, text="Image Adjustments")
        image_adjust_frame.grid(row=12, column=1, rowspan=7, columnspan=3, padx=10, pady=10)

        #prompt for contrast adjustments
        contrast_prompt = tk.Label(image_adjust_frame, text="Contrast:", padx=10, pady=10)
        contrast_prompt.grid(row=3, column=1)
        #Entry box for background color specification
        contrast_input = tk.Entry(image_adjust_frame, width=10)
        contrast_input.grid(row=3, column=2, padx=(3,3), pady=10)
        #add prompt to specify order of operation
        contrast_order_prompt = tk.Label(image_adjust_frame, text="Operation #:", padx=10, pady=10)
        contrast_order_prompt.grid(row=3, column=3)
        #add input box to specify order of operation
        contrast_order_input = tk.Entry(image_adjust_frame, width=10)
        contrast_order_input.grid(row=3, column=4, padx=(3,10), pady=10)

        #prompt for sharpness adjustments
        sharpen_prompt = tk.Label(image_adjust_frame, text="Sharpen:", padx=10, pady=10)
        sharpen_prompt.grid(row=4, column=1)
        #Entry box for sharpness specification
        sharpen_input = tk.Entry(image_adjust_frame, width=10)
        sharpen_input.grid(row=4, column=2, padx=(3,3), pady=10)
        #add prompt to specify order of operation
        sharpen_order_prompt = tk.Label(image_adjust_frame, text="Operation #:", padx=10, pady=10)
        sharpen_order_prompt.grid(row=4, column=3)
        #add input box to specify order of operation
        sharpen_order_input = tk.Entry(image_adjust_frame, width=10)
        sharpen_order_input.grid(row=4, column=4, padx=(3,10), pady=10)  

        #prompt for saturation adjustments
        saturate_prompt = tk.Label(image_adjust_frame, text="Saturate:", padx=10, pady=10)
        saturate_prompt.grid(row=5, column=1)
        #Entry box for sharpness specification
        saturate_input = tk.Entry(image_adjust_frame, width=10)
        saturate_input.grid(row=5, column=2, padx=(3,3), pady=10)
        #add prompt to specify order of operation
        saturate_order_prompt = tk.Label(image_adjust_frame, text="Operation #:", padx=10, pady=10)
        saturate_order_prompt.grid(row=5, column=3)
        #add input box to specify order of operation
        saturate_order_input = tk.Entry(image_adjust_frame, width=10)
        saturate_order_input.grid(row=5, column=4, padx=(3,10), pady=10)  

        #add color clustering parameters labeled frame
        color_clustering_frame = tk.LabelFrame(self, text="Color Clustering and Segmentation")
        color_clustering_frame.grid(row=19, column=1, rowspan=5, columnspan=3, padx=10, pady=10)

        #prompt for color count specification
        color_number_prompt = tk.Label(color_clustering_frame, text="Number of colors:               ", padx=10, pady=10)
        color_number_prompt.grid(row=3, column=1)
        #Entry box for color number specification
        color_number_input = tk.Entry(color_clustering_frame, width=10)
        color_number_input.grid(row=3, column=2, padx=(3,3), pady=10)

        #prompt for specifying pixel boundaries recoloring
        pixel_boundary_color_prompt = tk.Label(color_clustering_frame, text="Boundary Color: (R,G,B)     ", padx=10, pady=10)
        pixel_boundary_color_prompt.grid(row=4, column=1)
        #Entry box for background color specification
        pixel_boundary_color_input = tk.Entry(color_clustering_frame, width=10)
        pixel_boundary_color_input.grid(row=4, column=2, padx=(3,3), pady=10)
        #set default background color
        pixel_boundary_color_input.insert(0, '0,0,255')
        #function to convert RGB values to tkinter-readable values
        def convert_rgb(rgb_values):
            r,g,b = rgb_values
            return f'#{r:02x}{g:02x}{b:02x}'
        
        #add function to check background color
        def display_boundary_color():
            rgb_values = pixel_boundary_color_input.get()
            rgb_values = tuple([int(value) for value in rgb_values.split(',')])
            rgb_values = convert_rgb(rgb_values)
            pixel_boundary_color_display.configure(bg=rgb_values)

        #add background color checker
        pixel_boundary_color_display = Canvas(color_clustering_frame, highlightthickness=1, highlightbackground="black", width=20, height=10)
        pixel_boundary_color_display.grid(row=4, column=4, padx=(2,10))

        #add button to check color
        color_boundary_view_button = tk.Button(color_clustering_frame, text="View", command=display_boundary_color)
        color_boundary_view_button.grid(row=4, column=3, padx=(0,10), pady=10)
        
        #add output alteration labeled frame
        output_frame = tk.LabelFrame(self, text="Output Options")
        output_frame.grid(row=30, column=1, rowspan=5, columnspan=3, padx=10, pady=10)

        #prompt to select an directory of images
        outdir_select_prompt = tk.Label(output_frame, text="Directory:   ", padx=10, pady=10)
        outdir_select_prompt.grid(row=3, column=1)
        #function to select image
        def select_out_dir():
            out_dir = filedialog.askdirectory(title="Open Directories", initialdir = home_path)
            out_dir_input.delete(0, END)
            out_dir_input.insert(0, out_dir)
        #add entry for image file
        out_dir_input = tk.Entry(output_frame)
        out_dir_input.grid(row=3, column=2, padx=0, pady=10)
        #add button for selecting images
        out_dir_select_button = tk.Button(output_frame, text="Select Folder", command=select_out_dir)
        out_dir_select_button.grid(row=3, column=3, padx=(0,3), pady=10)

        #add option for global renaiming of output files
        rename_prompt = tk.Label(output_frame, text="Rename:     ", padx=10, pady=10)
        rename_prompt.grid(row=4, column=1)
        #add entry for rename file
        rename_input = tk.Entry(output_frame)
        rename_input.grid(row=4, column=2, padx=0, pady=10)

        #create frame for displaying log
        log_viewer_frame = tk.LabelFrame(self, text="Log Window")
        log_viewer_frame.grid(row=0, column=20, rowspan=20, columnspan=20, padx=20, pady=(19,0))
        #test canvas
        log_window = tk.Text(log_viewer_frame, width=52, height=31.4)
        log_window.grid(row=0, column=0)

        #add metadata frame
        metadata_frame = tk.LabelFrame(self, text="Metadata Options")
        metadata_frame.grid(row=19, column=20, rowspan=5, columnspan=3, padx=(20,0), pady=(0,0))

        #add metadata prompt and input
        metadata_prompt = tk.Label(metadata_frame, text="Metadata File:", padx=10, pady=10)
        metadata_prompt.grid(row=1, column=1)
        #Entry box for background color specification
        metadata_file_input = tk.Entry(metadata_frame, width=14)
        metadata_file_input.grid(row=1, column=2, padx=(3,3), pady=10)
        
        #add metadata prompt and input
        metadata_create_prompt = tk.Label(metadata_frame, text="Save to:", padx=10, pady=10)
        metadata_create_prompt.grid(row=2, column=1)
        #Entry box for metadata specification
        metadata_create_input = tk.Entry(metadata_frame, width=14)
        metadata_create_input.grid(row=2, column=2, padx=(3,3), pady=10)

        #function to select metadata
        def select_metadata_dir():
            metadata_dir = filedialog.askdirectory(title="Open Directories", initialdir = home_path)
            metadata_create_input.delete(0, END)
            metadata_create_input.insert(0, metadata_dir)

        #add button for selecting images
        metadata_dir_select_button = tk.Button(metadata_frame, text="Select Folder", command=select_metadata_dir)
        metadata_dir_select_button.grid(row=2, column=3, padx=(0,2), pady=10)

        #add function and button for clearing run
        def clear_run():
            image_file_input.delete(0, END)
            image_dir_input.delete(0, END)
            background_color_input.delete(0, END)
            color_convert_input.delete(0, END)
            contrast_input.delete(0, END)
            contrast_order_input.delete(0, END)
            sharpen_input.delete(0, END)
            sharpen_order_input.delete(0, END)
            saturate_input.delete(0, END)
            saturate_order_input.delete(0, END)
            color_number_input.delete(0, END)
            pixel_boundary_color_input.delete(0, END)
            out_dir_input.delete(0, END)
            rename_input.delete(0, END)
            metadata_file_input.delete(0, END)
            metadata_create_input.delete(0, END)

        #add clear run button
        clear_run_button = tk.Button(self, text="Clear Run", command=clear_run)
        clear_run_button.grid(row=1, column=21, padx=0, pady=0, sticky=W) 
    
        #function to get input data
        def get_input_data():
            image_data = []
            #get input file
            image_file = image_file_input.get()
            #get input directory
            image_directory = image_dir_input.get()
            if image_file == '' and image_directory == '':
                image_data.append('No_files')
            elif image_file != '' and image_directory != '':
                image_data.append('2_files')
            elif image_file != '' and image_directory == '':
                image_data.append('File')
                image_data.append(image_file)
            elif image_directory != '' and image_file == '':
                image_data.append('Directory')
                image_data.append(image_directory)
            
            return image_data
            
        def check_input_data(input_data):
            if input_data[0] == 'No_files':
                log_window.insert(INSERT, 'Error: No input data specified\n')
                return 0
            elif input_data[0] == '2_files':
                log_window.insert(INSERT, 'Error: File and directory specified\n')
                return 0
            
        def get_background_data():
            background_colors = []
            background_data = background_color_input.get()
            background_color = tuple([int(value) for value in background_data.split(',')])
            background_colors.append(background_color)

            convert_to_color = color_convert_input.get()
            convert_to = tuple([int(value) for value in convert_to_color.split(',')])
            background_colors.append(convert_to)
            
            return background_colors

        def set_up_output(infile):
            output_directory = out_dir_input.get()
            output_rename = rename_input.get()
            
            if output_rename != '':
                outdir = f"{output_directory}/{output_rename}"
                os.system(f"mkdir {outdir}")
            else:
                image_file_name = infile.split('/')[-1].replace('.png', '')
                outdir = f"{output_directory}/{image_file_name}"
                os.system(f"mkdir {outdir}")
            
            log_window.insert(INSERT, f"Created output directory: {outdir}\n")
            return outdir


        def get_image_adjustments():
            #initialize list to store image adjustment values
            image_adjustments = []
            #get contrast
            contrast_adjustment = contrast_input.get()
            contrast_adjustment_order = contrast_order_input.get()
            #get sharpness
            sharpness_adjustment = sharpen_input.get()
            sharpness_adjustment_order = sharpen_order_input.get()
            #get saturation adjustment
            saturation_adjustment = saturate_input.get()
            saturation_adjustment_order = saturate_order_input.get()
            #add values to list if they were specified
            if contrast_adjustment != '' and contrast_adjustment_order != '':
                image_adjustments.append([int(contrast_adjustment_order), int(contrast_adjustment), 'Contrast'])
            if sharpness_adjustment != '' and sharpness_adjustment_order != '':
                image_adjustments.append([int(sharpness_adjustment_order), int(sharpness_adjustment), 'Sharpness'])
            if saturation_adjustment != '' and saturation_adjustment_order != '':
                image_adjustments.append([int(saturation_adjustment_order), int(saturation_adjustment), 'Saturation'])
            
            #sort adjustments list
            image_adjustments.sort(key=lambda x: x[0])
            
            return image_adjustments

        #function to get color segmentation parameters
        def get_segmentation_parameters():
            k = int(color_number_input.get())
            boundary_color = pixel_boundary_color_input.get()
            boundary_color = tuple([int(value) for value in boundary_color.split(',')])
            
            return [k, boundary_color]

        #add function for writing metadata
        def write_metadata(infile, metadata_file):
            
            #if create == True:
                #with open(metadata_file, 'a') as outfile:
                    #outfile.write(f"Sample,File,Background Conversion,Image Adjustment,Color Clusters,Boundary Color")
            sample = infile.split('/')[-1].replace('.png', '')
            sample_rename = rename_input.get()
            if sample_rename != '':
                sample = sample_rename
            
            file = infile
            background_conversion_from = background_color_input.get()
            background_conversion_to = color_convert_input.get()
            image_adjustments = get_image_adjustments()
            color_clusters = color_number_input.get()
            boundary_color = pixel_boundary_color_input.get()

            with open(metadata_file, 'a') as outfile:
                outfile.write(f"{sample}\t{file}\t({background_conversion_from}) -> ({background_conversion_to})\t{image_adjustments}\t{color_clusters}\t({boundary_color})\n")

        #function to write metadata header line
        def add_metadata_header(metadata_file):
            with open(metadata_file, 'r') as infile:
                lines = infile.readlines()
            if lines[0] != "Sample\tFile\tBackground Conversion\tImage Adjustment\tColor Clusters\tBoundary Color\n":
                new_metadata_page = ["Sample\tFile\tBackground Conversion\tImage Adjustment\tColor Clusters\tBoundary Color\n"] + lines
            with open(metadata_file, 'w') as outfile:
                for line in new_metadata_page:
                    outfile.write(line)

        def run_clique(infile):
            log_window.insert(INSERT, f"Working on: {infile}\n")
            #set up output directory
            outdir = set_up_output(infile)
            #convert background
            file_name = infile.split('/')[-1]
            bg_convert_file = f"{outdir}/1_{file_name.replace('.png', '')}_bg.png"
            background_data = get_background_data()
            log_window.insert(INSERT, f"Converting background...\n")
            utils.background_converter(infile, background_data[0], background_data[1], bg_convert_file)
            log_window.insert(INSERT, f"Background converted: {bg_convert_file}\n")

            #perform image adjustments
            image_adjustments = get_image_adjustments()

            previous_file = ''
            for parameter in image_adjustments:
                operation_order = parameter[0]
                factor = parameter[1]
                operation = parameter[2]
                
                if previous_file == '':
                    previous_file = bg_convert_file

                if operation == 'Contrast':
                    outfile = f"{outdir}/{operation_order+1}_{file_name.replace('.png', '')}_cont.png"
                    utils.contrast_adjuster(previous_file, factor, outfile)
                    previous_file = outfile
                    log_window.insert(INSERT, f"Adjusting Contrast...\n")
                
                if operation == 'Sharpness':
                    outfile = f"{outdir}/{operation_order+1}_{file_name.replace('.png', '')}_shrp.png"
                    utils.sharpness_adjuster(previous_file, factor, outfile)
                    previous_file = outfile
                    log_window.insert(INSERT, f"Adjusting Sharpness...\n")
                
                if operation == 'Saturation':
                    outfile = f"{outdir}/{operation_order+1}_{file_name.replace('.png', '')}_satu.png"
                    utils.sharpness_adjuster(previous_file, factor, outfile)
                    previous_file = outfile
                    log_window.insert(INSERT, f"Adjusting Saturation...\n")
            
            #get segmentation parameters
            segmentation_parameters = get_segmentation_parameters()
            #perform K-means clustering
            k = segmentation_parameters[0]
            outfile = f"{outdir}/5_{file_name.replace('.png', '')}_kmc.png"
            utils.kmeans_transformer(previous_file, k, outfile)
            previous_file = outfile

            #draw segmentation boundaries
            boundary_color = segmentation_parameters[1]
            outfile = f"{outdir}/6_{file_name.replace('.png', '')}_bnd.png"
            utils.boundary_tracer(previous_file, boundary_color, outfile)
            previous_file = outfile

            #get metadata file location
            metadata_file_name = metadata_file_input.get()
            metadata_file_path = metadata_create_input.get()
            metadata_file = f"{metadata_file_path}/{metadata_file_name}"
            #write metadata
            write_metadata(infile, metadata_file)

        #function to run clique given input     
        def clique_main():
            #get and check input 
            input_data = get_input_data()
            input_check = check_input_data(input_data)

            #get input
            if input_check != 0:
                #if input is a file, run clique directly
                if input_data[0] == 'File':
                    run_clique(input_data[1])
                #if input is a directory, loop through all files
                elif input_data[0] == 'Directory':
                    files = os.listdir(input_data[1])
                    for file in files:
                        if file[-4:] == '.png':
                            run_clique(f"{input_data[1]}/{file}")
            
            #add metadata header line if not present
            #get metadata file location
            metadata_file_name = metadata_file_input.get()
            metadata_file_path = metadata_create_input.get()
            metadata_file = f"{metadata_file_path}/{metadata_file_name}"
            add_metadata_header(metadata_file)

        #create button to execute program
        run_button = tk.Button(self, text="Run", command=clique_main)
        run_button.grid(row=1, column=20, padx=(20,0), pady=10) 


class helpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        help_frame = tk.LabelFrame(self, text="Clique help")
        help_frame.grid(row=0, column=0, rowspan=5, columnspan=3, padx=10, pady=10)


app = CLIQUE()
app.mainloop()