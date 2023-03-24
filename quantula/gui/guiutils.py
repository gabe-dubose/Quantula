#Graphical user interface utilities

from tkinter import END, filedialog
import tkinter as tk
import os
from quantula import iutils
from quantula import qcdutils
import pandas as pd
from pandastable import TableModel
import zipfile
from PIL import ImageTk, Image

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
        delete_color = colorClassifiersTable.item(selection)['values'][0]
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

#function to view color map if available
def view_color_map(image_qcd_input, displayTable):
    #load color map
    color_map = qcdutils.load_color_map(image_qcd_input)
    #if color map was located
    if color_map != 0:
        for color in color_map:
            rgb_value = ",".join([str(value) for value in color_map[color]])
            color_display = f"{color}:{rgb_value}"
            displayTable.insert("", 'end', values=(color_display))
    else:
        tk.messagebox.showerror("Type Error", 'No color map located.')

#function to move color from color map to exclude
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

#function to get the input for counting colors
def get_color_counting_input(image_qcd_input, excludeTable, returnRawColors, returnColorFractions, output_file_input, output_dir_input):
    #get input
    qcd_input = image_qcd_input.get()
    color_map = qcdutils.load_color_map(qcd_input)
    return_raw_colors = returnRawColors.get()
    return_color_fractions = returnColorFractions.get()
    output_file = output_file_input.get()
    output_dir = output_dir_input.get()

    colors_to_exclude = []
    for color in excludeTable.get_children():
        colors_to_exclude.append(excludeTable.item(color)["values"][0])

    color_counting_input = {'qcd_input' : qcd_input, 'color_map' : color_map, 'colors_to_exclude' : colors_to_exclude, 'return_raw_color_counts' : return_raw_colors, 'return_color_fractions' : return_color_fractions, 'output_file' : output_file, 'output_dir' : output_dir}
    
    return color_counting_input

#function to run color counting
def count_colors(image_qcd_input, excludeTable, returnRawColors, returnColorFractions, output_file_input, output_dir_input):
    #load input
    color_counting_input = get_color_counting_input(image_qcd_input, excludeTable, returnRawColors, returnColorFractions, output_file_input, output_dir_input)
    #count pixels colors
    iutils.count_pixel_colors(color_counting_input)   

#function to update pandas table
def update_pandas_table(table_qcd_input, metadata_input, raw_table_view, fraction_tabele_view):
    #load input
    qcd_input = table_qcd_input.get()
    metadata_input = metadata_input.get()
    #get tables
    quantification_tables = qcdutils.get_quantification_tables(qcd_input)
    
    #load raw counts table
    raw_table = quantification_tables['raw_colors_table']
    if raw_table != '':
            #read table as csv
            raw_table_df = pd.read_csv(raw_table)
            raw_table_df.rename(columns={'Unnamed: 0':'sample-data'}, inplace=True)
            raw_table_df.set_index('sample-data')
            #display if metadata not specified
            if metadata_input == "":
                raw_table_view.updateModel(TableModel(raw_table_df))
                raw_table_view.redraw()
    
    #load fraction table
    fraction_table = quantification_tables['fraction_color_table']
    if fraction_table != '':
        #read table as csv
        fraction_table_df = pd.read_csv(fraction_table)
        fraction_table_df.rename(columns={'Unnamed: 0':'sample-data'}, inplace=True)
        fraction_table_df.set_index('sample-data')
        #display if metadata not specified
        if metadata_input == "":
            fraction_tabele_view.updateModel(TableModel(fraction_table_df))
            fraction_tabele_view.redraw()
    
    #if metadata input was provided, read and join with raw table
    if metadata_input != "" and raw_table != "":
        metadata_df = pd.read_csv(metadata_input)
        #perform inner join with metadata and raw table
        total_raw_table_df = pd.merge(raw_table_df, metadata_df, how='inner', on='sample-data')
        sample_ids = total_raw_table_df.pop('sample-id')
        total_raw_table_df.insert(0, 'sample-id', sample_ids)
        total_raw_table_df.drop('sample-data', axis=1, inplace=True)
        raw_table_view.updateModel(TableModel(total_raw_table_df))
        raw_table_view.redraw()
    
    #if metadata input was provided, read and join with fractions table
    if metadata_input != "" and fraction_table != "":
        metadata_df = pd.read_csv(metadata_input)
        #perform inner join with metadata and raw table
        total_fraction_table_df = pd.merge(fraction_table_df, metadata_df, how='inner', on='sample-data')
        sample_ids = total_fraction_table_df.pop('sample-id')
        total_fraction_table_df.insert(0, 'sample-id', sample_ids)
        total_fraction_table_df.drop('sample-data', axis=1, inplace=True)
        fraction_tabele_view.updateModel(TableModel(total_fraction_table_df))
        fraction_tabele_view.redraw()

#function for exporting table
def export_table(table, output_dir_input, out_file_input):
    #load input
    output_dir = output_dir_input.get()
    table_data = table.model.df

    #write output
    file_name = f"{output_dir}/{out_file_input}"
    table_data.to_csv(file_name, index=False)
    
#function for viewing images
def load_image_view(images_qcd, table):
    images_qcd_data = images_qcd.get()
    #check qcd type
    qcd_type = qcdutils.get_qcd_type(images_qcd_data)
    #if qcd is of proper type
    if qcd_type == 'image_data':
        #load image data
        image_data = qcdutils.read_image_data_qcd(images_qcd_data)
        qcd_images = image_data[0]
        qcd = zipfile.ZipFile(images_qcd_data, 'r')
        for i in range(len(qcd_images)):
            image_name = qcd_images[i].split('/')[-1]
            table.insert("", 'end', values=(image_name))

            '''
            if i == 1:
                image = qcd_images[i]
                image_data = qcd.open(image)
                image_load = Image.open(image_data)
                image_load.show()
            '''

#function to open image
def open_image(images_qcd, image_name):
    images_qcd_data = images_qcd.get()
    #load image data
    image_data = qcdutils.read_image_data_qcd(images_qcd_data)
    qcd_images = image_data[0]
    qcd = zipfile.ZipFile(images_qcd_data, 'r')

    #open image
    for i in range(len(qcd_images)):
        image_load_name = qcd_images[i].split('/')[-1]
        if image_load_name == image_name:
            image = qcd_images[i]
            image_data = qcd.open(image)
            image_load = Image.open(image_data)
            image_load.show()

#function to get image resize parameters
def get_image_resize_input(image_qcd_input, size, method, output_file_input, output_dir_input):
    #get input
    qcd_input = image_qcd_input.get()
    size_input = size.get()
    method_input = method.get()
    output_file = output_file_input.get()
    output_dir = output_dir_input.get()

    #split size
    width =  int(size_input.split(',')[0])
    height =  int(size_input.split(',')[1])

    #assemble input
    image_resize_input = {'qcd_input' : qcd_input, 'width' : width, 'height' : height, 'method' : method_input, 'output_file' : output_file, 'output_dir' : output_dir}

    return image_resize_input

#function to resize image
def resize_image(image_qcd_input, size, method, output_file_input, output_dir_input):
    #get input
    input = get_image_resize_input(image_qcd_input, size, method, output_file_input, output_dir_input)
    #resize image
    iutils.resize_image(input)
