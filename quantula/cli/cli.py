#!/usr/bin/env python3

import argparse
from quantula.cli import help_messages

#primary parser
main_parser = argparse.ArgumentParser(add_help=False)
main_parser._positionals.title = "Quantula commands"
main_parser.add_argument('--help', required=False, action='store_true')
#command subparser
command_subparser = main_parser.add_subparsers(dest="command")

#### DATA-MANAGER COMMAND ####

#initialize data-manager command, subparser, and help option
data_manager_command = command_subparser.add_parser('data-manager', add_help=False)
data_manager_parser = data_manager_command.add_subparsers(dest="data_manager")
data_manager_command.add_argument('--help', action='store_true')

#data-manager:import-data command and subparser
import_data_command = data_manager_parser.add_parser('import-data', add_help=False)
import_data_command.add_subparsers(dest="data_manager_import_data")
#data-manager: import data commands
import_data_command.add_argument('--help', action='store_true')
import_data_command.add_argument('--image-directory', dest="import_images_directory")
import_data_command.add_argument('--metadata', dest="import_images_metadata")
import_data_command.add_argument('--output-name', dest="import_images_output_name")
import_data_command.add_argument('--output-directory', dest="import_data_out_dir")

#data-manager:export-images command and subparser
export_images_command = data_manager_parser.add_parser('export-images', add_help=False)
export_images_command.add_subparsers(dest="data_manager_export_images")

#data-manager:export-quantifications command and subparser
export_quantifications_command = data_manager_parser.add_parser('export-quantifications', add_help=False)
export_quantifications_command.add_subparsers(dest="data_manager_export_quantifications")


#parse arguments
args = main_parser.parse_args()

#print help options
if args.command == None and args.help == True:
    print(help_messages.main_help_message)

try:
    #data-manager help options
    if args.data_manager == None or args.data_manager != None and args.help == True:
        print(help_messages.data_manager_help)

    #import-data command help message
    elif args.data_manager_import_data == None or args.data_manager_import_data != None and args.help == True:
        print(help_messages.import_data_help) 
except:
    pass

