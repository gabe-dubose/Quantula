from quantula.cli import help_messages
from quantula import qcdutils

def data_manager(user_input):
    #print help options if specified or args are blank
    if user_input['data_manager'] == None or user_input['data_manager_help'] == True:
        print(help_messages.data_manager_help)

    #run tools
    else:
        # IMPORT DATA COMMAND
        if user_input['data_manager'] == 'import-data':
            #print help messages if specified
            if user_input['import_data_help'] == True:
                print(help_messages.import_data_help)
            else:
                #try to exceute command
                try:
                    #get input
                    image_dir = user_input['import_images_directory']
                    sample_metadata = user_input['import_images_metadata']
                    output_file = user_input['import_images_output_name']
                    output_dir = user_input['import_data_out_dir']
                    #assemble input
                    import_data_input = {'image_dir' : image_dir, 'sample_metadata' : sample_metadata, 'output_file' : output_file, 'output_dir' : output_dir}
                    #run data import
                    qcdutils.make_import_qcd(import_data_input)
                #if not possible, print error
                except:
                    print(help_messages.import_data_help)
                    print('Error')

        # EXPORT IMAGES COMMAND
        elif user_input['data_manager'] == 'export-images':
            #print help messages if specified
            if user_input['export_images_help'] == True or user_input['data_manager_export_images'] == None:
                print(help_messages.export_images_help)

        # EXPORT TABLE COMMAND
        elif user_input['data_manager'] == 'export-table':
            #print help messages if specified
            if user_input['export_table_help'] == True or user_input['data_manager_export_table'] == None:
                print(help_messages.export_table_help)