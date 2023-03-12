#!/usr/bin/env python3

import argparse

#primary parser
main_parser = argparse.ArgumentParser(add_help=False)
main_parser._positionals.title = "Quantula commands"
main_parser.add_argument('--help', required=False, action='store_true')

#command subparser
command_subparser = main_parser.add_subparsers(dest="command")
data_manager_command = command_subparser.add_parser('data-manager', add_help=False)
image_adjuster_command = command_subparser.add_parser('image-adjuster', add_help=False)
color_segmenter_command = command_subparser.add_parser('color-segmenter', add_help=False)
color_quantifier_command = command_subparser.add_parser('color-quantifier', add_help=False)

#data manager subparser
data_manager_parser = data_manager_command.add_subparsers(dest="data_manager")
import_data_command = data_manager_parser.add_parser('import-data', add_help=False)
export_images_command = data_manager_parser.add_parser('export-images', add_help=False)
export_quantifications_command = data_manager_parser.add_parser('export-quantifications', add_help=False)

#import data subparser
import_data_command.add_subparsers(dest="data_manager_import_data")
import_data_command.add_argument('--help', action='store_true')
import_data_command.add_argument('--image-directory', dest="import_images_directory")
import_data_command.add_argument('--metadata', dest="import_images_metadata")
import_data_command.add_argument('--output-name', dest="import_images_output_name")
import_data_command.add_argument('--output-directory', dest="import_data_out_dir")

args = main_parser.parse_args()

#help messages
main_help_message = '''
Quantula:

Commands:
data-manager\t\tUsage: import and export data
image-adjuster\t\tUsage: standard image color adjustments
color-segmenter\t\tUsage: color seqmentation and image re-coloring
color-quantifier\tUsage: color quantification

To see options for specific commands, run:
Quantula {command} --help
'''

data_manager_help = '''
Quantula data-manager:

Commands:
import-data\t\tUsage: import images and metadata into a Quantula compressed directorye (qcd)
export-images\t\tUsage: export images from a qcd file into a standard folder
export-quantifications\tUsage: export quantification table into a CSV file
'''

import_data_help = '''
Quantula data-manager import-data:

Required options:
--image-directory\tDirectory containing images to be imported
--metadata\t\tMetadata file in csv format
--output-name\t\tName of output qcd file
--output-directory\tPath to directory for output qcd to be saved
'''

#Print main help message if no commands are specified or if help flag is specified
if args.command == None or args.help == True:
    print(main_help_message)

#Print data manager help message
elif args.data_manager == None or args.data_manager != None and args.help == True:
    print(data_manager_help)

#Print import data help message
elif args.data_manager_import_data == None or args.data_manager_import_data != None and args.help == True:
    print(import_data_help)