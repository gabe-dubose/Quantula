
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