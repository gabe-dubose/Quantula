#Interface utilities

from PIL import Image
import os
import pandas as pd
import shutil
from quantula import qcdutils
import zipfile
from quantula import image_adjuster
from quantula import color_quantifier

#function to check import
def check_input(input):
    #load metadata
    try:
        sample_metadata = pd.read_csv(input['sample_metadata'])
        try:
            sample_data = sample_metadata['sample-data']
        except:
            return 'Error: sample-data field must be present'
            exit()
    except:
        return 'Error: could not load sample metadata'
        exit()

    #check image metadata
    image_run = []
    images = os.listdir(input['image_dir'])
    for image in sample_metadata['sample-data']:
        if image not in images:
            return 'Error: all images specified in mapping file must be present in the uploaded directory'
            exit()
        else:
            image_run.append(image)

    #check image format
    image_failed = 0
    for image in image_run:
        image_file = f"{input['image_dir']}/{image}"
        try:
            Image.open(image_file, 'r').convert('RGB')
        except:
            image_failed += 1
            return 'Error: could not read some or all images'
            exit()
        
    if image_failed == 0:
        return 0

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

#function to perform pixel conversion
def convert_pixel(input):
    #check qcd type
    qcd_type = qcdutils.get_qcd_type(input['qcd_input'])
    #if qcd is of proper type
    if qcd_type == 'image_data':
        #check rgb inputs
        from_color = check_rgb_input(input['pixel_color'])
        to_color = check_rgb_input(input['pixel_convert'])

        if isinstance(from_color, tuple) == True and isinstance(to_color, tuple) == True:
            #initialize output directory
            output_file_dir = f"{input['output_dir']}/{input['output_file']}"
            qcdutils.initialize_image_data_qcd(output=output_file_dir)

            #get image data and load images
            qcd_data = qcdutils.read_image_data_qcd(input['qcd_input'])
            qcd_images = qcd_data[0]
            qcd = zipfile.ZipFile(input['qcd_input'])
            #iterate through images and perform pixel conversion
            for image in qcd_images:
                #read data
                image_data = qcd.open(image)
                #initilaize output file name
                image_file_name = image.split('/')[-1]
                outfile = f"{output_file_dir}/images/{image_file_name}"
                #perform image adjustment
                image_adjuster.recolor_pixels(image=image_data, from_color=from_color, to_color=to_color, outfile=outfile)
            
            #add source tracker
            source_info = qcdutils.load_source_tracker(input['qcd_input'])
            qcdutils.add_to_source_tracker(source_tracker_dict=source_info, input=input, operation='convert_pixel')
    
            #compress file and make qcd
            qcdutils.dir_to_qcd(dir=output_file_dir, main=input['output_dir'], sub=input['output_file'])

#function to perform image adjustment
def adjust_image(input, adjust):
    #check qcd type
    qcd_type = qcdutils.get_qcd_type(input['qcd_input'])
    #if qcd is of proper type
    if qcd_type == 'image_data':
        #initialize output directory
        output_file_dir = f"{input['output_dir']}/{input['output_file']}"
        qcdutils.initialize_image_data_qcd(output=output_file_dir)
        #get image data and load images
        qcd_data = qcdutils.read_image_data_qcd(input['qcd_input'])
        qcd_images = qcd_data[0]
        qcd = zipfile.ZipFile(input['qcd_input'])
        #iterate through images and perform adjustment
        for image in qcd_images:
            #read data
            image_data = qcd.open(image)
            #initilaize output file name
            image_file_name = image.split('/')[-1]
            outfile = f"{output_file_dir}/images/{image_file_name}"
            #perform adjustments
            if adjust == 'contrast':
                image_adjuster.adjust_contrast(image=image_data, factor=input['factor'], outfile=outfile)
            elif adjust == 'sharpness':
                image_adjuster.adjust_sharpness(image=image_data, factor=input['factor'], outfile=outfile)
            elif adjust == 'saturation':
                image_adjuster.adjust_saturation(image=image_data, factor=input['factor'], outfile=outfile)

        #compress file and make qcd
        qcdutils.dir_to_qcd(dir=output_file_dir, main=input['output_dir'], sub=input['output_file'])

#function to perform kmeans clustering
def kmeans_transform(input):
    #check qcd type
    qcd_type = qcdutils.get_qcd_type(input['qcd_input'])
    #if qcd is of proper type
    if qcd_type == 'image_data':
        #initialize output directory
        output_file_dir = f"{input['output_dir']}/{input['output_file']}"
        qcdutils.initialize_image_data_qcd(output=output_file_dir)
        #get image data and load images
        qcd_data = qcdutils.read_image_data_qcd(input['qcd_input'])
        qcd_images = qcd_data[0]
        qcd = zipfile.ZipFile(input['qcd_input'])
        #iterate through images and perform kmeans clustering
        for image in qcd_images:
            #read data
            image_data = qcd.open(image)
            #initilaize output file name
            image_file_name = image.split('/')[-1]
            outfile = f"{output_file_dir}/images/{image_file_name}"
            #perform adjustments
            image_adjuster.kmeans_transform(image=image_data, k=input['k'], outfile=outfile, iterations=input['iterations'], epsilon=input['epsilon'], attempts=input['attempts'])

        #compress file and make qcd
        qcdutils.dir_to_qcd(dir=output_file_dir, main=input['output_dir'], sub=input['output_file'])

#function to perform color boundary tracing
def trace_color_boundaries(input):
    #check qcd type
    qcd_type = qcdutils.get_qcd_type(input['qcd_input'])
    #if qcd is of proper type
    if qcd_type == 'image_data':
        #check pixel color
        boundary_color = check_rgb_input(input['pixel_color'])
        #initialize output directory
        output_file_dir = f"{input['output_dir']}/{input['output_file']}"
        qcdutils.initialize_image_data_qcd(output=output_file_dir)
        #get image data and load images
        qcd_data = qcdutils.read_image_data_qcd(input['qcd_input'])
        qcd_images = qcd_data[0]
        qcd = zipfile.ZipFile(input['qcd_input'])
        #iterate through images and perform color boundary tracing
        for image in qcd_images:
            #read data
            image_data = qcd.open(image)
            #initilaize output file name
            image_file_name = image.split('/')[-1]
            outfile = f"{output_file_dir}/images/{image_file_name}"
            #perform adjustments
            image_adjuster.trace_color_boundaries(image=image_data, threshold=input['boundary_threshold'], color=boundary_color, outfile=outfile)

        #compress file and make qcd
        qcdutils.dir_to_qcd(dir=output_file_dir, main=input['output_dir'], sub=input['output_file'])

#function to perform re-coloring using euclidian distance minimization
def euclidian_minimization_recoloring(input):
    #check qcd type
    qcd_type = qcdutils.get_qcd_type(input['qcd_input'])
    #if qcd is of proper type
    if qcd_type == 'image_data':
        #initialize output directory
        output_file_dir = f"{input['output_dir']}/{input['output_file']}"
        qcdutils.initialize_image_data_qcd(output=output_file_dir)
        #get image data and load images
        qcd_data = qcdutils.read_image_data_qcd(input['qcd_input'])
        qcd_images = qcd_data[0]
        qcd = zipfile.ZipFile(input['qcd_input'])
        #iterate through images and perform kmeans clustering
        for image in qcd_images:
            #read data
            image_data = qcd.open(image)
            #initilaize output file name
            image_file_name = image.split('/')[-1]
            outfile = f"{output_file_dir}/images/{image_file_name}"
            #perform adjustments
            image_adjuster.euclidian_minimization_recoloring(image=image_data, color_map=input['color_mappings'], outfile=outfile)

        #save color map to json
        qcdutils.add_color_map(color_map=input['color_mappings'], output=output_file_dir)

        #compress file and make qcd
        qcdutils.dir_to_qcd(dir=output_file_dir, main=input['output_dir'], sub=input['output_file'])

#function to get raw color counts
def count_pixel_colors(input):
    #initialize output
    color_counts = {}
    #check qcd type
    qcd_type = qcdutils.get_qcd_type(input['qcd_input'])
    #if qcd is of proper type
    if qcd_type == 'image_data':
        #initialize output directory
        output_file_dir = f"{input['output_dir']}/{input['output_file']}"
        qcdutils.initialize_quantification_data_qcd(output=output_file_dir)
        #get image data and load images
        qcd_data = qcdutils.read_image_data_qcd(input['qcd_input'])
        qcd_images = qcd_data[0]
        qcd = zipfile.ZipFile(input['qcd_input'])
        #iterate through images and perform kmeans clustering
        for image in qcd_images:
            #read data
            image_data = qcd.open(image)
            #initilaize output file name
            image_file_name = image.split('/')[-1]
            #count pixels
            color_quantifier.count_pixel_colors(image=image_data, color_map=input['color_map'], sample=image_file_name, outdict=color_counts)
    
    #if return raw counts is specified, write raw counts to csv
    if input['return_raw_color_counts'] == 1:
        raw_color_counts_df = pd.DataFrame.from_dict(color_counts).T
        raw_color_counts_outfile = f"{output_file_dir}/tables/raw_color_counts.csv"
        raw_color_counts_df.to_csv(raw_color_counts_outfile)

    #if return color fractions is specified, calculate fraction
    if input['return_color_fractions'] == 1:
        #load exclude input
        colors_to_exclude = [color.split(':')[0] for color in input['colors_to_exclude']]
        #get pixel fractions
        pixel_fractions = color_quantifier.get_color_fractions(pixel_counts=color_counts, exclude=colors_to_exclude)
        #convert to dataframe and write
        color_fractions_df = pd.DataFrame.from_dict(pixel_fractions).T
        color_fractions_outfile = f"{output_file_dir}/tables/color_fractions.csv"
        color_fractions_df.to_csv(color_fractions_outfile)

    #compress file and make qcd
    qcdutils.dir_to_qcd(dir=output_file_dir, main=input['output_dir'], sub=input['output_file'])
