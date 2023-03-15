#!/usr/bin/env python3

import argparse
from quantula.cli import help_messages

#primary parser
main_parser = argparse.ArgumentParser(add_help=False)
main_parser._positionals.title = "Quantula commands"
main_parser.add_argument('--help', required=False, action='store_true', dest="main_help")
#command subparser
command_subparser = main_parser.add_subparsers(dest="command")

###########################
#### DATA MANAGER TOOL ####
###########################

#initialize data-manager command, subparser, and help option
data_manager_command = command_subparser.add_parser('data-manager', add_help=False)
data_manager_parser = data_manager_command.add_subparsers(dest="data_manager")
data_manager_command.add_argument('--help', action='store_true', dest="data_manager_help")

#data-manager:import-data command and subparser
import_data_command = data_manager_parser.add_parser('import-data', add_help=False)
import_data_command.add_subparsers(dest="data_manager_import_data")
#data-manager: import data options
import_data_command.add_argument('--help', action='store_true', dest="import_data_help")
import_data_command.add_argument('--image-directory', dest="import_images_directory")
import_data_command.add_argument('--metadata', dest="import_images_metadata")
import_data_command.add_argument('--output-name', dest="import_images_output_name")
import_data_command.add_argument('--output-directory', dest="import_data_out_dir")

#data-manager:export-images command and subparser
export_images_command = data_manager_parser.add_parser('export-images', add_help=False)
export_images_command.add_subparsers(dest="data_manager_export_images")
#data-manager: export images options
export_images_command.add_argument('--help', action='store_true', dest="export_images_help")
export_images_command.add_argument('--input-images', dest="export_images_input_images")
export_images_command.add_argument('--output-directory', dest="export_images_outdir")

#data-manager:export-table command and subparser
export_table_command = data_manager_parser.add_parser('export-table', add_help=False)
export_table_command.add_subparsers(dest="data_manager_export_table")
#data-manager: export-quantifications options
export_table_command.add_argument('--help', action='store_true', dest="export_table_help")
export_table_command.add_argument('--input-table', dest="export_table_input_table")
export_table_command.add_argument('--output-directory', dest="export_table_outdir")

#############################
#### IMAGE ADJUSTER TOOL ####
#############################

#initialize image-adjuster command, subparser, and help option
image_adjuster_command = command_subparser.add_parser('image-adjuster', add_help=False)
image_adjuster_parser = image_adjuster_command.add_subparsers(dest="image_adjuster")
image_adjuster_command.add_argument('--help', action='store_true')

#image-adjuster:convert-pixels command and subparser
convert_pixels_command = image_adjuster_parser.add_parser('convert-pixels', add_help=False)
convert_pixels_command.add_subparsers(dest="image_adjuster_convert_pixels")
#image-adjuster: convert pixels options
convert_pixels_command.add_argument('--help', action='store_true')
convert_pixels_command.add_argument('--input-images', dest="convert_pixels_input_images")
convert_pixels_command.add_argument('--from', dest="convert_pixels_from_color")
convert_pixels_command.add_argument('--to', dest="convert_pixels_to_color")
convert_pixels_command.add_argument('--output-name', dest="convert_pixels_output_name")
convert_pixels_command.add_argument('--output-directory', dest="import_data_out_dir")

#parse arguments
args = main_parser.parse_args()

#print help options
if args.command == None or args.command != None and args.main_help == True:
    print(help_messages.main_help_message)

#data-manager help options
try:
    if args.data_manager == None or args.data_manager != None and args.data_manager_help == True:
        print(help_messages.data_manager_help)
except:
    pass

#import-data command help message
try:
    if args.data_manager_import_data == None or args.data_manager_import_data != None and args.import_data_help == True:
        print(help_messages.import_data_help) 
except:
    pass

#export-data command help message
try:
    if args.export_images_help == True or args.data_manager_export_images == None:
        print(help_messages.export_images_help)
except:
    pass

#export-table command help message
try:
    if args.export_table_help == True or args.data_manager_export_table == None:
        print(help_messages.export_table_help)
except:
    pass