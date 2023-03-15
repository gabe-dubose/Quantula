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
image_adjuster_command.add_argument('--help', action='store_true', dest="image_adjuster_help")

#image-adjuster:recolor-pixels command and subparser
recolor_pixels_command = image_adjuster_parser.add_parser('recolor-pixels', add_help=False)
recolor_pixels_command.add_subparsers(dest="image_adjuster_recolor_pixels")
#image-adjuster: recolor pixels options
recolor_pixels_command.add_argument('--help', action='store_true', dest="recolor_pixels_help")
recolor_pixels_command.add_argument('--input-images', dest="recolor_pixels_input_images")
recolor_pixels_command.add_argument('--from', dest="recolor_pixels_from_color")
recolor_pixels_command.add_argument('--to', dest="recolor_pixels_to_color")
recolor_pixels_command.add_argument('--output-name', dest="recolor_pixels_output_name")
recolor_pixels_command.add_argument('--output-directory', dest="import_data_out_dir")

#image-adjuster: adjust-contrast command and subparser
adjust_contrast_command = image_adjuster_parser.add_parser('adjust-contrast', add_help=False)
adjust_contrast_command.add_subparsers(dest="image_adjuster_adjust_contrast")
#image-adjuster: adjust contrast
adjust_contrast_command.add_argument('--help', action='store_true', dest="adjust_contrast_help")
adjust_contrast_command.add_argument('--input-images', dest="adjust_contrast_input_images")
adjust_contrast_command.add_argument('--contrast-factor', dest="contrast_factor")
adjust_contrast_command.add_argument('--output-name', dest="adjust_contrast_output_name")
adjust_contrast_command.add_argument('--output-directory', dest="adjust_contrast_out_dir")

#image-adjuster: adjust-sharpness command and subparser
adjust_sharpness_command = image_adjuster_parser.add_parser('adjust-sharpness', add_help=False)
adjust_sharpness_command.add_subparsers(dest="image_adjuster_adjust_sharpness")
#image-adjuster: adjust sharpness
adjust_sharpness_command.add_argument('--help', action='store_true', dest="adjust_sharpness_help")
adjust_sharpness_command.add_argument('--input-images', dest="adjust_sharpness_input_images")
adjust_sharpness_command.add_argument('--sharpness-factor', dest="sharpness_factor")
adjust_sharpness_command.add_argument('--output-name', dest="adjust_sharpness_output_name")
adjust_sharpness_command.add_argument('--output-directory', dest="adjust_sharpness_out_dir")

#image-adjuster: adjust-saturation command and subparser
adjust_saturation_command = image_adjuster_parser.add_parser('adjust-saturation', add_help=False)
adjust_saturation_command.add_subparsers(dest="image_adjuster_adjust_saturation")
#image-adjuster: adjust saturation
adjust_saturation_command.add_argument('--help', action='store_true', dest="adjust_saturation_help")
adjust_saturation_command.add_argument('--input-images', dest="adjust_saturation_input_images")
adjust_saturation_command.add_argument('--saturation-factor', dest="saturation_factor")
adjust_saturation_command.add_argument('--output-name', dest="adjust_saturation_output_name")
adjust_saturation_command.add_argument('--output-directory', dest="adjust_saturation_out_dir")

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

#image-adjuster help options
try:
    if args.image_adjuster_help == True or args.image_adjuster == None:
        print(help_messages.image_adjuster_help)
except:
    pass

#recolor-pixels command help message
try:
    if args.recolor_pixels_help == True or args.image_adjuster_recolor_pixels == None:
        print(help_messages.recolor_pixels_help)
except:
    pass

#adjust-contrast command help message
try:
    if args.adjust_contrast_help == True or args.image_adjuster_adjust_contrast == None:
        print(help_messages.adjust_contrast_help)
except:
    pass

#adjust-sharpness command help message
try:
    if args.adjust_sharpness_help == True or args.image_adjuster_adjust_sharpness == None:
        print(help_messages.adjust_sharpness_help)
except:
    pass

#adjust-saturation command help message
try:
    if args.adjust_saturation_help == True or args.image_adjuster_adjust_saturation == None:
        print(help_messages.adjust_saturation_help)
except:
    pass