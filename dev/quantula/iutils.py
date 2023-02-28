#Interface utilities

from PIL import Image
import os
import pandas as pd
import shutil
from quantula import qcdutils
import zipfile
from quantula import image_adjuster

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

#function to perform background conversion
def convert_background(input):
    #check qcd type
    qcd_type = qcdutils.get_qcd_type(input['qcd_input'])
    #if qcd is of proper type
    if qcd_type == 'image_data':
        #check rgb inputs
        from_color = check_rgb_input(input['background_color'])
        to_color = check_rgb_input(input['background_convert'])

        if isinstance(from_color, tuple) == True and isinstance(to_color, tuple) == True:
            #initialize output directory
            output_file_dir = f"{input['output_dir']}/{input['output_file']}"
            qcdutils.initialize_image_data_qcd(output=output_file_dir)

            #get image data and load images
            qcd_data = qcdutils.read_image_data_qcd(input['qcd_input'])
            qcd_images = qcd_data[0]
            qcd = zipfile.ZipFile(input['qcd_input'])
            #iterate through images and perform background conversion
            for image in qcd_images:
                #read data
                image_data = qcd.open(image)
                #initilaize output file name
                image_file_name = image.split('/')[-1]
                outfile = f"{output_file_dir}/images/{image_file_name}"
                #perform image adjustment
                image_adjuster.recolor_background(image=image_data, from_color=from_color, to_color=to_color, outfile=outfile)
            
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