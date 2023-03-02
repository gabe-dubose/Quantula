#Graphical user interface utilities

from tkinter import END, filedialog
import tkinter as tk
import os
from quantula import iutils
from quantula import qcdutils

#function to select directory
def select_directory(input_box):
    home_path = os.path.expanduser('~')
    image_dir = filedialog.askdirectory(title="Open Directories", initialdir = home_path)
    input_box.delete(0, END)
    input_box.insert(0, image_dir)

#function to select csv file
def select_csv_file(input_box):
    home_path = os.path.expanduser('~')
    filetypes = (('CSV File', '*.csv'), ('All files', '*.*'))
    image_file = filedialog.askopenfilename(title="Open Files", initialdir = home_path, filetypes = filetypes)
    input_box.delete(0, END)
    input_box.insert(0, image_file)

#function to select qcd file
def select_qcd_file(input_box):
    home_path = os.path.expanduser('~')
    filetypes = (('qcd File', '*.qcd'), ('All files', '*.*'))
    image_file = filedialog.askopenfilename(title="Open Files", initialdir = home_path, filetypes = filetypes)
    input_box.delete(0, END)
    input_box.insert(0, image_file)

#function to get import information
def get_image_import_information(image_dir_input, sample_metadata_input, output_file_input, output_dir_input):
    image_dir = image_dir_input.get()
    sample_metadata = sample_metadata_input.get()
    output_file = output_file_input.get()
    output_dir = output_dir_input.get()

    image_import_input = {'image_dir' : image_dir, 'sample_metadata' : sample_metadata, 'output_file' : output_file, 'output_dir' : output_dir}
    return image_import_input

#function to load input data
def load_import_input(image_dir_input, sample_metadata_input, output_file_input, output_dir_input):
    #load data
    load_data_input = get_image_import_information(image_dir_input, sample_metadata_input, output_file_input, output_dir_input)
    #check data
    input_check = iutils.check_input(load_data_input)

    if input_check == 0:
        #make qcd
        if output_dir_input.get() == "" or output_file_input == "":
            tk.messagebox.showerror("Import error", 'Output options not specified.')
        else:
            qcdutils.make_import_qcd(load_data_input)
            tk.messagebox.showinfo("Import message", "All data imported successfully.")
    else:
        tk.messagebox.showerror("Import error", input_check)

#function to display color in color box
def display_color_box(input, color_display):
    rgb_values = input.get()
    rgb_values = tuple([int(value) for value in rgb_values.split(',')])
    r,g,b = rgb_values
    converted_values = f'#{r:02x}{g:02x}{b:02x}'
    color_display.configure(bg=converted_values)

#function to get input for pixel conversion
def get_bg_convert_input(image_qcd_input, pixel_color_input, pixel_convert_input, output_file_input, output_dir_input):
    #get input
    qcd_input = image_qcd_input.get()
    pixel_color = pixel_color_input.get()
    pixel_convert = pixel_convert_input.get()
    output_file = output_file_input.get()
    output_dir = output_dir_input.get()
    bg_convert_input = {'qcd_input': qcd_input, 'pixel_color': pixel_color, 'pixel_convert' : pixel_convert, 'output_file': output_file ,'output_dir': output_dir}

    return bg_convert_input

#function to convert pixel
def convert_pixel(image_qcd_input, pixel_color_input, pixel_convert_input, output_file_input, output_dir_input):
    #load input
    input = get_bg_convert_input(image_qcd_input, pixel_color_input, pixel_convert_input, output_file_input, output_dir_input)
    #convert pixel
    iutils.convert_pixel(input)

#function to get contrast adjustment input
def get_image_adjustment_input(image_qcd_input, factor_input, output_file_input, output_dir_input):
    #get input
    qcd_input = image_qcd_input.get()
    factor = factor_input.get()
    output_file = output_file_input.get()
    output_dir = output_dir_input.get()

    image_adjustment_input = {'qcd_input' : qcd_input, 'factor' : factor, 'output_file' : output_file, 'output_dir' : output_dir}

    return image_adjustment_input

#function to run image adjustments
def adjust_image(image_qcd_input, factor_input, output_file_input, output_dir_input, adjust):
    #load input
    image_adjustment_input = get_image_adjustment_input(image_qcd_input, factor_input, output_file_input, output_dir_input)
    #adjust image
    iutils.adjust_image(image_adjustment_input, adjust)

#function to get kmeans clustering input
def get_kmeans_input(image_qcd_input, color_number_input, output_file_input, output_dir_input, epsilon_input, iterations_input, attempts_input):
    #get input
    qcd_input = image_qcd_input.get()
    color_number = color_number_input.get()
    output_file = output_file_input.get()
    output_dir = output_dir_input.get()
    epsilon = epsilon_input.get()
    iterations = iterations_input.get()
    attempts = attempts_input.get()

    kmeans_input = {'qcd_input' : qcd_input, 'k' : int(color_number), 'output_file' : output_file, 'output_dir' : output_dir, 'epsilon' : float(epsilon), 'iterations' : int(iterations), 'attempts' : int(attempts)}

    return kmeans_input

#function to perform kmeans transformation
def kmeans_transform(image_qcd_input, color_number_input, output_file_input, output_dir_input, epsilon_input, iterations_input, attempts_input):
    #load input
    kmeans_input = get_kmeans_input(image_qcd_input, color_number_input, output_file_input, output_dir_input, epsilon_input, iterations_input, attempts_input)
    #transform image
    iutils.kmeans_transform(kmeans_input)

#function to get input for color boundary tracing
def get_boundary_tracing_input(image_qcd_input, pixel_color_input, boundary_threshold_input, output_file_input, output_dir_input):
    #get input
    qcd_input = image_qcd_input.get()
    pixel_color = pixel_color_input.get()
    boundary_threshold = boundary_threshold_input.get()
    output_file = output_file_input.get()
    output_dir = output_dir_input.get()

    boundary_tracing_input = {'qcd_input' : qcd_input, 'pixel_color' : pixel_color, 'boundary_threshold' : boundary_threshold, 'output_file' : output_file, 'output_dir' : output_dir}

    return boundary_tracing_input

#function to perform color boundary tracing
def trace_color_boundaries(image_qcd_input, pixel_color_input, boundary_threshold_input, output_file_input, output_dir_input):
    #load input
    boundary_tracing_input = get_boundary_tracing_input(image_qcd_input, pixel_color_input, boundary_threshold_input, output_file_input, output_dir_input)
    #transform image
    iutils.trace_color_boundaries(boundary_tracing_input)

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
        rgb_value = iutils.check_rgb_input(color_rgb)
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
def delete_color_classification_entry(color_mappings, added_colors, colorClassifiersTable):
    selected_color = colorClassifiersTable.selection()
    for selection in selected_color:
        delete_color = colorClassifiersTable.item(selection)['values'][1]
        del color_mappings[delete_color]
        try:
            colorClassifiersTable.delete(selection)
        except:
            pass
                
        #remove from recorded colors
        added_colors.remove(delete_color)

#function for adding color classification to table
def update_color_classification_view(added_colors, new_color_rgb_input, new_color_name_input, color_mappings, colorClassifiersTable):
    add_color_classification_entry(added_colors, new_color_rgb_input, new_color_name_input, color_mappings)
    #clear current entry
    for color in colorClassifiersTable.get_children():
        try:
            colorClassifiersTable.delete(color)
        except:
            pass

    #refresh entry
    for color in color_mappings:
        color_name = color
        color_rgb = ",".join([str(value) for value in color_mappings[color]])
        colorClassifiersTable.insert("", 'end', values=(color_name, color_rgb))

#function to get euclidian minimization recoloring input
def get_euclidian_minimization_recoloring_input(image_qcd_input, color_mappings, output_file_input, output_dir_input):
    #load input
    qcd_input = image_qcd_input.get()
    output_file = output_file_input.get()
    output_dir = output_dir_input.get()

    euclidian_minimization_recoloring_input = {'qcd_input' : qcd_input, 'color_mappings' : color_mappings, 'output_file' : output_file, 'output_dir' : output_dir}

    return euclidian_minimization_recoloring_input

#function to perform euclidian minimization recoloring
def euclidian_minimization_recoloring(image_qcd_input, color_mappings, output_file_input, output_dir_input):
    #load input
    euclidian_minimization_recoloring_input = get_euclidian_minimization_recoloring_input(image_qcd_input, color_mappings, output_file_input, output_dir_input)
    #transform image
    iutils.euclidian_minimization_recoloring(euclidian_minimization_recoloring_input)