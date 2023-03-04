from PIL import Image

#function to count pixel colors of input image
def count_pixel_colors(image, color_map, sample, outdict):
    #load image
    image = Image.open(image, 'r').convert('RGB')
    #get pixel data
    pixel_values = list(image.getdata())
    #initialize output
    color_counts = {}
    #iterate through each pixel and add to appopriate count
    # if color map was specified, use it to classify colors
    if color_map != "":
        #reverse color_map to that RGB values are keys
        color_map_reversed = {}
        for color in color_map:
            pixel_str = ','.join(str(value) for value in color_map[color])
            color_map_reversed[pixel_str] = color

        #iterate through all pixels, classify, and add to dictionary
        for pixel in pixel_values:
            #convert pixel value to string so that it can be querried against reversed color map
            pixel_str = ','.join(str(value) for value in pixel)
            #get color value for pixel key
            color = color_map_reversed[pixel_str]
            #if color has not been added to counter add it
            if color not in color_counts:
                color_counts[color] = 1
            #if it has been added, add 1 to counter
            else:
                color_counts[color] += 1

    #add results to dictionary
    if sample not in outdict:
        outdict[sample] = color_counts

#function to get proportions of pixels
def get_color_fractions(pixel_counts, exclude):
    #initialize output
    color_fractions = {}