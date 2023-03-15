
#main help message
main_help_message = '''
Quantula

Commands:
  data-manager\t\tUsage: import and export data
  image-adjuster\tUsage: standard image color adjustments
  color-segmenter\tUsage: color seqmentation and image re-coloring
  color-quantifier\tUsage: color quantification

To see options for specific commands, run:
Quantula {command} --help
'''

###########################
#### DATA MANAGER HELP ####
###########################

#main help message
data_manager_help = '''
Quantula data-manager

Commands:
  import-data\t\tUsage: import images and metadata into a Quantula compressed directorye (qcd)
  export-images\t\tUsage: export images from a qcd file into a standard folder
  export-table\t\tUsage: export quantification table into a CSV file
'''

#import data help message
import_data_help = '''
Quantula data-manager import-data

Required:
  --image-directory\tDirectory containing images to be imported
  --metadata\t\tMetadata file in csv format
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved
'''

#export images help message
export_images_help = '''
Quantula data-manager export-images

Required:
  --input-images\tqcd file containing images to be exported (type=image_data)
  --output-directory\tPath to the directory for output image directory to be saved
'''

export_table_help = '''
Quantula data-manager export-table

Required:
  --input-table\tqcd file containing quantification tables to be exported (type=table_data)
  --output-directory\tPath to the directory for output image directory to be saved
'''

#############################
#### IMAGE ADJUSTER TOOL ####
#############################

image_adjuster_help = '''
Quantula image-adjuster

Commands:
  recolor-pixels\tUsage: change all pixels of a specified RGB value to a different RGB value
  adjust-contrast\tUsage: increase or decrease contrast
  adjust-sharpness\tUsage: increase or decrease sharpness
  adjust-saturation\tUsage: increase or decrease saturation
'''

recolor_pixels_help = '''
Quantula image-adjuster recolor-pixels

Required:
  --input-images\tqcd file containing images to be exported (type=image_data)
  --from\t\tRBG value of pixels to be recolored
  --to\t\t\tRGB value for pixels to be recolored to
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved
'''

adjust_contrast_help = '''
Quantula image-adjuster adjust-contrast

Required:
  --input-images\tqcd file containing images to be exported (type=image_data)
  --contrast-factor\tFactor to increase or decrease contrast by
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved
'''

adjust_sharpness_help = '''
Quantula image-adjuster adjust-sharpness

Required:
  --input-images\tqcd file containing images to be exported (type=image_data)
  --sharpness-factor\tFactor to increase or decrease sharpness by
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved
'''

adjust_saturation_help = '''
Quantula image-adjuster adjust-saturation

Required:
  --input-images\tqcd file containing images to be exported (type=image_data)
  --saturation-factor\tFactor to increase or decrease saturation by
  --output-name\t\tName of output qcd file
  --output-directory\tPath to directory for output qcd to be saved
'''