import zipfile
import os
import shutil
import pandas as pd
import json
import uuid
from quantula import info

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

    #assemble source info
    source_info = {str(uuid.uuid4()) : {'operation' : 'import', 'operation_order' : 1, 'input' : input, 'quantula_version' : info.version}}

    #add source tracking file
    with open(f"{output_file_dir}/metadata/source_tracker.json", 'w') as file:
        json.dump(source_info, file, indent=6)

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

#function to set up table data qcd
def initialize_quantification_data_qcd(output):
    #set up directory
    output_file_dir = output
    os.makedirs(output_file_dir)
    os.makedirs(f"{output_file_dir}/tables")
    os.makedirs(f"{output_file_dir}/metadata")
    #add qualifier file
    with open(f"{output_file_dir}/metadata/quantification_table", 'w') as file:
        pass

#function to add color map file
def add_color_map(color_map, output):
    output_file = f"{output}/metadata/color_map.json"
    with open(output_file, 'w') as outfile:
        json.dump(color_map, outfile, indent=6)

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
    
def load_source_tracker(qcd):

    qcd_unzip = zipfile.ZipFile(qcd, 'r')
    qcd_contents = []

    for content in qcd_unzip.namelist():
        qcd_contents.append(content)

    main_dir = qcd_contents[0]
    metadata_dir = f"{main_dir}metadata"

    for entry in qcd_unzip.namelist():
        if 'source_tracker.json' in entry:
            source_data = entry
    
    source_data = qcd_unzip.open(source_data)
    source_data = json.load(source_data)
    
    return source_data

#function to add to source tracker
def add_to_source_tracker(source_tracker_dict, input, operation):
    #get operation order
    operation_orders = []
    for operation_id in source_tracker_dict:
        operation_order = source_tracker_dict[operation_id]['operation_order']
        operation_orders.append(operation_order)
    
    operation_order = max(operation_orders) + 1

    #operation_order = source_tracker_dict['operation_order'] + 1
    #assemble output
    source_info = {'operation' : operation, 'operation_order' : operation_order, 'input' : input, 'quantula_version' : info.version}
    #add info to source info
    source_tracker_dict[str(uuid.uuid4())] = source_info

    #write output
    output_file_dir = f"{input['output_dir']}/{input['output_file']}"
    with open(f"{output_file_dir}/metadata/source_tracker.json", 'w') as file:
        json.dump(source_tracker_dict, file, indent=6)

#function to get quantification tables
def get_quantification_tables(qcd):

    #initialize output
    tables = {'raw_colors_table' : '', 'fraction_color_table' : ''}

    qcd_unzip = zipfile.ZipFile(qcd, 'r')
    qcd_contents = []

    for content in qcd_unzip.namelist():
        qcd_contents.append(content)

    for entry in qcd_unzip.namelist():
        if 'raw_color_counts.csv' in entry:
            raw_color_table = qcd_unzip.extract(entry)
            tables['raw_colors_table'] = raw_color_table

        if 'color_fractions.csv' in entry:
            fract_color_table = qcd_unzip.extract(entry)
            tables['fraction_color_table'] = fract_color_table

    return tables

#function to export images from qcd
def export_images(images_qcd, output_dir_input):
    #check qcd type
    qcd_type = get_qcd_type(images_qcd)
    #if qcd is of proper type
    if qcd_type == 'image_data':
        qcd_unzip = zipfile.ZipFile(images_qcd, 'r')
        qcd_contents = []

        for content in qcd_unzip.namelist():
            qcd_contents.append(content)
        
        main_dir = qcd_contents[0]
        images_dir = f"{main_dir}images/"
        images_dir_contents = []
        
        for content in qcd_contents:
            if images_dir in content:
                images_dir_contents.append(content)

        qcd_unzip.extractall(members=images_dir_contents, path=output_dir_input)