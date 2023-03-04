import zipfile
import os
import shutil
import pandas as pd
import json

#function to get qcd type
def get_qcd_type(qcd):

    qcd_type = 'not_defined'
    #load qcd contents
    qcd_unzip = zipfile.ZipFile(qcd, 'r')
    qcd_contents = []
    for content in qcd_unzip.namelist():
        qcd_contents.append(content)
    
    main_dir = qcd_contents[0]

    if f"{main_dir}metadata/image_data" in qcd_contents:
        qcd_type = 'image_data'
    
    return qcd_type

def read_image_data_qcd(qcd):
    qcd_unzip = zipfile.ZipFile(qcd, 'r')
    qcd_contents = []
    image_data = []
    sample_metadata = []

    for content in qcd_unzip.namelist():
        qcd_contents.append(content)

    main_dir = qcd_contents[0]
    image_dir = f"{main_dir}images"

    for entry in qcd_unzip.namelist():
        if image_dir in entry:
            image_data.append(entry)
    
    image_data = image_data[1:]

    return [image_data, sample_metadata]

#function to make quantula compressed directory
def make_import_qcd(input):
    #initialize output directory
    output_file_dir = f"{input['output_dir']}/{input['output_file']}"
    os.makedirs(output_file_dir)
    os.makedirs(f"{output_file_dir}/images")
    os.makedirs(f"{output_file_dir}/metadata")

    #add qualifier file
    with open(f"{output_file_dir}/metadata/image_data", 'w') as file:
        pass

    #copy image files
    sample_metadata = pd.read_csv(input['sample_metadata'])
    image_run = []
    for image in sample_metadata['sample-data']:
        image_run.append(image)
    for image in image_run:
        image_file = f"{input['image_dir']}/{image}"
        shutil.copyfile(image_file, f"{output_file_dir}/images/{image}")
    
    #copy metadata file
    metadata_file_name = input['sample_metadata'].split('/')[-1]
    shutil.copyfile(input['sample_metadata'], f"{output_file_dir}/metadata/{metadata_file_name}")

    #compress file and make qcd
    shutil.make_archive(output_file_dir, 'zip', input['output_dir'], input['output_file'])
    os.rename(f"{input['output_dir']}/{input['output_file']}.zip", f"{input['output_dir']}/{input['output_file']}.qcd")
    shutil.rmtree(output_file_dir)

#function to set up image data qcd
def initialize_image_data_qcd(output):
    #set up directory
    output_file_dir = output
    os.makedirs(output_file_dir)
    os.makedirs(f"{output_file_dir}/images")
    os.makedirs(f"{output_file_dir}/metadata")
    #add qualifier file
    with open(f"{output_file_dir}/metadata/image_data", 'w') as file:
        pass

#function to add color map file
def add_color_map(color_map, output):
    output_file = f"{output}/metadata/color_map.json"
    with open(output_file, 'w') as outfile:
        json.dump(color_map, outfile)

#function to zip a directory and make it a qcd
def dir_to_qcd(dir, main, sub):
    #compress
    shutil.make_archive(dir, 'zip', main, sub)
    #rename
    os.rename(f"{main}/{sub}.zip", f"{main}/{sub}.qcd")
    #remove dir
    shutil.rmtree(dir)

#function to load color map (if present)
def load_color_map(qcd):

    color_map_file_check = []
    #read qcd contents
    qcd_unzip = zipfile.ZipFile(qcd, 'r')
    qcd_contents = []
    for content in qcd_unzip.namelist():
        qcd_contents.append(content)

    main_dir = qcd_contents[0]
    color_map_file = f"{main_dir}metadata/color_map.json"

    for entry in qcd_unzip.namelist():
        if color_map_file in entry:
            color_map_file_check.append(color_map_file)

    if len(color_map_file_check) != 0:
        data = qcd_unzip.open(color_map_file_check[0])
        color_map = json.load(data)
        return color_map

    else:
        return 0