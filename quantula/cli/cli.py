#!/usr/bin/env python3

import argparse
from quantula.cli import help_messages
from quantula import iutils
from quantula import qcdutils
from quantula.cli.tools import data_manager

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
data_manager_command.add_argument('--help', action='store_true', dest="data_manager_help", default=False)

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
recolor_pixels_command.add_argument('--output-directory', dest="recolor_pixels_out_dir")

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

##############################
#### COLOR SEGMENTER TOOL ####
##############################

#initialize color-segmenter command, subparser, and help option
color_segmenter_command = command_subparser.add_parser('color-segmenter', add_help=False)
color_segmenter_parser = color_segmenter_command.add_subparsers(dest="color_segmenter")
color_segmenter_command.add_argument('--help', action='store_true', dest="color_segmenter_help")

#color-segmenter:k-means-recolor command and subparser
k_means_recolor_command = color_segmenter_parser.add_parser('k-means-recolor', add_help=False)
k_means_recolor_command.add_subparsers(dest="color_segmenter_k_means_recolor")
#color-segmenter: k-means-recolor options
k_means_recolor_command.add_argument('--help', action='store_true', dest="k_means_recolor_help")
k_means_recolor_command.add_argument('--input-images', dest="k_means_recolor_input_images")
k_means_recolor_command.add_argument('--k', dest="k_means_k_input")
k_means_recolor_command.add_argument('--epsilon', dest="k_means_epsilon")
k_means_recolor_command.add_argument('--iterations', dest="k_means_iterations")
k_means_recolor_command.add_argument('--attempts', dest="k_means_attempts")
k_means_recolor_command.add_argument('--output-name', dest="k_means_output_name")
k_means_recolor_command.add_argument('--output-directory', dest="k_means_out_dir")

#color-segmenter:euclidian-recolor command and subparser
euclidian_recolor_command = color_segmenter_parser.add_parser('euclidian-recolor', add_help=False)
euclidian_recolor_command.add_subparsers(dest="color_segmenter_euclidian_recolor")
#color-segmenter: euclidian-recolor options
euclidian_recolor_command.add_argument('--help', action='store_true', dest="euclidian_recolor_help")
euclidian_recolor_command.add_argument('--input-images', dest="euclidian_recolor_input_images")
euclidian_recolor_command.add_argument('--color-names', dest="euclidian_recolor_names")
euclidian_recolor_command.add_argument('--color-values', dest="euclidian_recolor_values")
euclidian_recolor_command.add_argument('--output-name', dest="euclidian_recolor_output_name")
euclidian_recolor_command.add_argument('--output-directory', dest="euclidian_recolor_out_dir")

#color-segmenter:trace-color-boundaries command and subparser
trace_color_boundaries_command = color_segmenter_parser.add_parser('trace-color-boundaries', add_help=False)
trace_color_boundaries_command.add_subparsers(dest="color_segmenter_trace_color_boundaries")
#color-segmenter: trace-color-boundaries options
trace_color_boundaries_command.add_argument('--help', action='store_true', dest="trace_color_boundaries_help")
trace_color_boundaries_command.add_argument('--input-images', dest="trace_color_boundaries_input_images")
trace_color_boundaries_command.add_argument('--boundary-color', dest="boundary_color")
trace_color_boundaries_command.add_argument('--threshold', dest="boundary_threshold")
trace_color_boundaries_command.add_argument('--output-name', dest="trace_color_boundaries_output_name")
trace_color_boundaries_command.add_argument('--output-directory', dest="trace_color_boundaries_out_dir")

###############################
#### COLOR QUANTIFIER TOOL ####
###############################

#initialize color-quantifier command, subparser, and help option
color_quantifier_command = command_subparser.add_parser('color-quantifier', add_help=False)
color_quantifier_parser = color_quantifier_command.add_subparsers(dest="color_quantifier")
color_quantifier_command.add_argument('--help', action='store_true', dest="color_quantifier_help")

#color-quantifier:quantify-colors command and subparser
quantify_colors_command = color_quantifier_parser.add_parser('quantify-colors', add_help=False)
quantify_colors_command.add_subparsers(dest="color_quantifier_quantify_colors")
#color-segmenter: trace-color-boundaries options
quantify_colors_command.add_argument('--help', action='store_true', dest="quantify_colors_help")
quantify_colors_command.add_argument('--input-images', dest="quantify_colors_input_images")
quantify_colors_command.add_argument('--color-map', dest="color_map")
quantify_colors_command.add_argument('--return', dest="return_tables")
quantify_colors_command.add_argument('--output-name', dest="quantify_colors_output_name")
quantify_colors_command.add_argument('--output-directory', dest="quantify_colors_out_dir")

#parse arguments
args = main_parser.parse_args()
user_input = vars(args)
print(user_input)

#print main help options
if user_input['command'] == None or user_input['main_help'] == True:
    print(help_messages.main_help_message)

###########################
#### DATA MANAGER TOOL ####
###########################

if user_input['command'] == 'data-manager':
    data_manager.data_manager(user_input)


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

#color-segmenter help options
try:
    if args.color_segmenter_help == True or args.color_segmenter == None:
        print(help_messages.color_segmenter_help)
except:
    pass

#kmeans-recolor help options
try:
    if args.k_means_recolor_help == True or args.color_segmenter_k_means_recolor == None:
        print(help_messages.k_means_recolor_help)
except:
    pass

#euclidian-recolor help options
try:
    if args.euclidian_recolor_help == True or args.color_segmenter_euclidian_recolor == None:
        print(help_messages.euclidian_recolor_help)
except:
    pass

#trace-color-boundaries help options
try:
    if args.trace_color_boundaries_help == True or args.color_segmenter_trace_color_boundaries == None:
        print(help_messages.trace_color_boundaries_help)
except:
    pass

#color-quantifier help options
try:
    if args.color_quantifier_help == True or args.color_quantifier == None:
        print(help_messages.color_segmenter_help)
except:
    pass

#quantify-colors help options
try:
    if args.quantify_colors_help == True or args.color_quantifier_quantify_colors == None:
        print(help_messages.quantify_colors_help)
except:
    pass