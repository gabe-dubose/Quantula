from random import sample
from quantula.cli import help_messages
from quantula import iutils

def image_adjuster(user_input):
    #print help options if specified or args are blank
    if user_input['image_adjuster'] == None or user_input['image_adjuster_help'] == True:
        print(help_messages.image_adjuster_help)

    #run tools
    else:
        #RECOLOR PIXELS COMMAND
        if user_input['image_adjuster'] == 'recolor-pixels':
            if user_input['recolor_pixels_help'] == True:
                print(help_messages.recolor_pixels_help)
            else:
                #try to execut command

                #get input
                qcd_input = user_input['recolor_pixels_input_images']
                from_color = user_input['recolor_pixels_from_color']
                to_color = user_input['recolor_pixels_to_color']
                output_file = user_input['recolor_pixels_output_name']
                output_dir = user_input['recolor_pixels_out_dir']
                #assemble input
                recolor_pixels_input = {'qcd_input' : qcd_input, 'pixel_color' : from_color, 'pixel_convert' : to_color, 'output_file' : output_file, 'output_dir' : output_dir}
                #run recolor pixel
                iutils.convert_pixel(recolor_pixels_input)

        #ADJUST CONTRAST COMMAND
        elif user_input['image_adjuster'] == 'adjust-contrast':
            pass

        #ADJUST SHARPNESS COMMAND
        elif user_input['image_adjuster'] == 'adjust-sharpness':
            pass

        #ADJUST SATURATION COMMAND
        elif user_input['image_adjuster'] == 'adjust-saturation':
            pass

    