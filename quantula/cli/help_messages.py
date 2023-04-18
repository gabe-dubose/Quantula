
#main help message
main_help_message = '''
quantula

Commands:
  data-manager\t\tUsage: import and export data
  image-adjuster\tUsage: standard image color adjustments
  color-partitioner\tUsage: color seqmentation and image re-coloring
  color-quantifier\tUsage: color quantification

To see options for specific commands, run:
quantula {command} --help
'''

###########################
#### DATA MANAGER HELP ####
###########################

#main help message
data_manager_help = '''
quantula data-manager

Commands:
  import-data\t\tUsage: import images and metadata into a Quantula compressed directorye (qcd)
  export-images\t\tUsage: export images from a qcd file into a standard folder
  export-table\t\tUsage: export quantification table into a CSV file
'''

#import data help message
import_data_help = '''
quantula data-manager import-data

Required:
  --image-directory\tDirectory containing images to be imported
  --metadata\t\tMetadata file in csv format
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved
'''

#export images help message
export_images_help = '''
quantula data-manager export-images

Required:
  --input-images\tqcd file containing images to be exported (type=image_data)
  --output-directory\tPath to the directory for output image directory to be saved
'''

export_table_help = '''
quantula data-manager export-table

Required:
  --input-table\tqcd file containing quantification tables to be exported (type=table_data)
  --output-directory\tPath to the directory for output image directory to be saved
'''

#############################
#### IMAGE ADJUSTER TOOL ####
#############################

image_adjuster_help = '''
quantula image-adjuster

Commands:
  recolor-pixels\tUsage: change all pixels of a specified RGB value to a different RGB value
  adjust-contrast\tUsage: increase or decrease contrast
  adjust-sharpness\tUsage: increase or decrease sharpness
  adjust-saturation\tUsage: increase or decrease saturation
'''

recolor_pixels_help = '''
quantula image-adjuster recolor-pixels

Required:
  --input-images\tqcd file containing images (type=image_data)
  --from\t\tRBG value of pixels to be recolored
  --to\t\t\tRGB value for pixels to be recolored to
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved
'''

adjust_contrast_help = '''
quantula image-adjuster adjust-contrast

Required:
  --input-images\tqcd file containing images to be exported (type=image_data)
  --contrast-factor\tFactor to increase or decrease contrast by
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved
'''

adjust_sharpness_help = '''
quantula image-adjuster adjust-sharpness

Required:
  --input-images\tqcd file containing images to be exported (type=image_data)
  --sharpness-factor\tFactor to increase or decrease sharpness by
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved
'''

adjust_saturation_help = '''
quantula image-adjuster adjust-saturation

Required:
  --input-images\tqcd file containing images to be exported (type=image_data)
  --saturation-factor\tFactor to increase or decrease saturation by
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved
'''

################################
#### COLOR PARTITIONER TOOL ####
################################

color_partitioner_help = '''
quantula color-partitioner

Commands:
  k-means-recolor\t\tUsage: recolor images using k-means clustering
  euclidian-recolor\t\tUsage: recolor images by calculating color proximities to a specified color map
  trace-color-boundaries\tUsage: recolor all pixels that are on the boundary between colors
'''

k_means_recolor_help = '''
quantula color-partitioner k-means-recolor

Required:
  --input-images\tqcd file containing images to be exported (type=image_data)
  --k\t\t\tnumber of colors to cluster into
  --epsilon\t\tdistance to define neighbors, default=0.85
  --iterations\t\tnumber time to perform re-clustering, default=100
  --attempts\t\tnumber of times to perform clustering with different labels, default=10
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved
'''

euclidian_recolor_help = '''
quantula color-partitioner euclidian-recolor

Required:
  --input-images\tqcd file containing images to be exported (type=image_data)
  --color-names\t\tcolor names in a comma separated list (e.g. red,yellow,blue)
  --color-values\tRGB values corresponding to color-names (e.g. (255,0,0),(255,255,0),(0,0,255))
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved
'''

trace_color_boundaries_help = '''
quantula color-partitioner trace-color-boundaries

Required:
  --input-images\tqcd file containing images to be exported (type=image_data)
  --boundary-color\tRGB value to recolor boundary pixels
  --threshold\t\tThreshold to define color boundaries (1-8)
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved
'''

###############################
#### COLOR QUANTIFIER TOOL ####
###############################

color_partitioner_help = '''
quantula color-quantifier

Commands:
  quantify-colors\tUsage: quantify the abundance or proportions of each color in an image
'''

quantify_colors_help = '''
quantula color-partitioner trace-color-boundaries

Required:
  --input-images\tqcd file containing images to be exported (type=image_data)
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved

Options:
  --color-map\t\tColor map designating color names and RGB values, formatted as: red:(255,0,0),yellow:(255,255,0)
    Note: --color-map input is not required if euclidian recoloring was performed 
  --return\t\tspecify which color quantifications to return (raw-counts, color-fractions)
    Note: both options can be specified
'''