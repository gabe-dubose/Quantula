
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
