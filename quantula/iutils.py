import tkinter as tk	
from tkinter import *
from tkinter import DISABLED, END, INSERT, filedialog
from PIL import Image
import os

#function to select image
def select_image_file(input_box, home_path):
    filetypes = (('PNG File', '*.png'), ('All files', '*.*'))
    image_file = filedialog.askopenfilename(title="Open Files", initialdir = home_path, filetypes = filetypes)
    input_box.delete(0, END)
    input_box.insert(0, image_file)

#function to select csv file
def select_csv_file(input_box, home_path):
    filetypes = (('CSV File', '*.csv'), ('All files', '*.*'))
    image_file = filedialog.askopenfilename(title="Open Files", initialdir = home_path, filetypes = filetypes)
    input_box.delete(0, END)
    input_box.insert(0, image_file)

#function to select directory
def select_directory(input_box, home_path):
    image_dir = filedialog.askdirectory(title="Open Directories", initialdir = home_path)
    input_box.delete(0, END)
    input_box.insert(0, image_dir)

#function to display color in color box
def display_color_box(input, color_display):
    rgb_values = input.get()
    rgb_values = tuple([int(value) for value in rgb_values.split(',')])
    r,g,b = rgb_values
    converted_values = f'#{r:02x}{g:02x}{b:02x}'
    color_display.configure(bg=converted_values)

def reset_run(image_adjustment_scales, inputs_to_blank, value_resets, operation_boxes, text_resets):
    #reset image adjustment scales
    for adjustment_scale in image_adjustment_scales:
        adjustment_scale.set(0)
    
    #reset inputs that require blanking
    for input in inputs_to_blank:
        input.delete(0, END)

    #reset background color conversions
    for option in value_resets:
        option[0].delete(0, END)
        option[0].insert(0, option[1])
    
    #reset operation order boxes
    for box in operation_boxes:
        box.set(0)
    
    #clear text boxes
    for text_box in text_resets:
        text_box.delete('1.0', END)

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

#function to get and check user input
def get_standard_user_segmentation_input(image_file_input, image_dir_input, background_color_input, color_convert_input, contrast_input, contrast_order_input, sharpness_input, sharpness_order_input, saturation_input, saturation_order_input, color_number_input, boundary_color_input, out_dir_input, rename_input, metadata_file_input, metadata_dir_input):

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
        if color_number != "":
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

    #check that metadata was specified correctly
    if error == 0:
        if metadata_file != "" and metadata_dir == "":
            tk.messagebox.showerror("Input Error", "Error. Metadata file specified but save to location was not.")
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

        if color_number != "":
            standard_user_input['color_number'] = color_number
        elif color_number == "":
            standard_user_input['color_number'] = color_number = 'NA'

        if boundary_color != "":
            standard_user_input['boundary_tracing_color'] = boundary_tracing_color
        else:
            standard_user_input['boundary_tracing_color'] = 'NA'

        standard_user_input['rename'] = rename
        standard_user_input['out_dir'] = out_dir
                
        if metadata_file != "":
            standard_user_input['metadata_file'] = metadata_file
        else:
            standard_user_input['metadata_file'] = 'quantula_metadata'
            
        if metadata_dir != "":
            standard_user_input['metadata_dir'] = metadata_dir
        

        return standard_user_input

    else:
        return 0
    
#function to add color classification
def add_color_classification_entry(added_colors, new_color_rgb_input, new_color_name_input, color_mappings):
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
def delete_color_classification_entry(color_mappings, added_colors, colorClassifiersTable, colorQuantificationTableInclude):
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

#function for adding color classification to table
def update_color_classification_view(added_colors, new_color_rgb_input, new_color_name_input, color_mappings, colorClassifiersTable, colorQuantificationTableInclude):
    add_color_classification_entry(added_colors, new_color_rgb_input, new_color_name_input, color_mappings)
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

#function to move color from include to exclude
def exclude_color(colorQuantificationTableInclude, colorQuantificationTableExclude):
    selected_color = colorQuantificationTableInclude.selection()
    for selection in selected_color:
        exclude_color = colorQuantificationTableInclude.item(selection)['values'][0]
        colorQuantificationTableExclude.insert("", 'end', values=(exclude_color))
        colorQuantificationTableInclude.delete(selection)

#function to move color from exclude to include
def include_color(colorQuantificationTableExclude, colorQuantificationTableInclude):
    selected_color = colorQuantificationTableExclude.selection()
    for selection in selected_color:
        include_color = colorQuantificationTableExclude.item(selection)['values'][0]
        colorQuantificationTableInclude.insert("", 'end', values=(include_color))
        colorQuantificationTableExclude.delete(selection)

#function to get colors to exclude from quantification
def get_colors_to_exclude(colorQuantificationTableExclude):
    colors_to_exclude = []
    for color in colorQuantificationTableExclude.get_children():
        colors_to_exclude.append(colorQuantificationTableExclude.item(color)["values"][0])
    return colors_to_exclude

#function to get a check uder input for quantification
#function to get data for quantification run
def get_quantification_parameters(image_file_inputQT, image_dir_inputQT, colorQuantificationTableExclude, color_mappings, output_file_input, new_output_dir_input):
    
    quantification_parameters = {}

    #get image file
    image_file = image_file_inputQT.get()
    #get image directory
    image_directory = image_dir_inputQT.get()
    #get colors to exclude from fraction calculations
    colors_to_exclude = get_colors_to_exclude(colorQuantificationTableExclude)
    #get output parameters
    new_output = new_output_dir_input.get()
    load_output = output_file_input.get()

    error = 0
    if image_file != "" and image_directory != "":
        tk.messagebox.showerror("Input Error", f"Error: Both image file and directory specified.")
        error += 1
    
    elif image_file == "" and image_directory == "" and error == 0:
        tk.messagebox.showerror("Input Error", f"Error: No input specified.")
        error += 1
    
    elif image_file != "" and image_directory == "" and error == 0:
        #check that image file is readable
        try:
            Image.open(image_file, 'r')
            quantification_parameters['image_file'] = image_file
        except:
            tk.messagebox.showerror("Input Error", f"Error: Could not read image {image_file}")
            error += 1
    
    elif image_directory != "" and image_file == "" and error == 0:
        images = os.listdir(image_directory)
        image_paths = []
        for image in images:
            image_path = f"{image_directory}/{image}"
            image_paths.append(image_path)
        quantification_parameters['image_directory'] = image_paths

    if new_output != "" and load_output != "" and error == 0:
        tk.messagebox.showerror("Input Error", f"Error: Both new output file and load prior output file specified.")
        error += 1

    elif new_output == "" and load_output == "" and error == 0:
        tk.messagebox.showerror("Input Error", f"Error: No output directions specified.")
        error += 1
    
    elif new_output != "" and error == 0:
        quantification_parameters['new_output'] = new_output
    
    elif load_output != "" and error == 0:
        quantification_parameters['load_output'] = load_output
    
    quantification_parameters['colors_to_exclude'] = colors_to_exclude
    quantification_parameters['color_mappings'] = color_mappings

    return quantification_parameters