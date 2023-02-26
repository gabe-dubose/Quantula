from PIL import Image
import pandas as pd
from tkinter import DISABLED, END, INSERT, filedialog

#function to load image and return pixel values
def load_pixels(image):
    #read image
    image = Image.open(image, 'r').convert('RGB')
    #get pixel values
    pixels = list(image.getdata())

    return pixels

#function to calculate euclidean distance between two colors
def calculate_euclidean_distance(ps, qs):
    #map RGB values to each other
    cartesian_coordinates = list(zip(ps,qs))
    #intiailize list to store ditances for each value
    coordinate_distances = []
    #iterate through each value and calculate distance between value coordinates
    for p,q in cartesian_coordinates:
        coordinate_distance = (p-q)**2
        coordinate_distances.append(coordinate_distance)
    #calculate euclidian distance
    euclidean_distance = sum(coordinate_distances)**0.5

    return euclidean_distance

#function to calculate closest input color using euclidean distances
def classify_color(pixel_map, pixel):
    #initialize list for storing each distance pair
    color_distances = []
    #iterate through all colors in input pixel map and calculate euclidean distance
    for reference_color in pixel_map:
        reference_pixel = pixel_map[reference_color]
        euclidean_distance = calculate_euclidean_distance(reference_pixel, pixel)
        color_distances.append([euclidean_distance, reference_color])
    
    #return color with smallest euclidean distance
    nearest_color = min(color_distances)

    return nearest_color

#function to recalssify and count colors in input image
def color_counter(pixel_values, color_mapping):

    #initialize dictionary to hold counts for each color, initialize with 0 values
    color_counts = {}
    for color in color_mapping:
        color_counts[color] = 0
    
    #cache to hold pixel - classification pairings that have already been encountered
    pixel_classifications = {}

    #iterate through all pixels, perform classification and counting
    for pixel in pixel_values:

        #check if pixel has already been cached
        pixel_str = ','.join(str(value) for value in pixel)
        #if so, use cache to designate pixel color
        if pixel_str in pixel_classifications:
            pixel_color = pixel_classifications[pixel_str]
            #add 1 to pixel counts
            color_counts[pixel_color] += 1
        
        #if not, find closest color (smallest euclidean distance)
        elif pixel_str not in pixel_classifications:
            closest_color = classify_color(color_mapping, pixel)
            color = closest_color[1]

            #add newly classified color to cache
            pixel_str = ','.join(str(value) for value in pixel)
            pixel_classifications[pixel_str] = color

            #update counter
            color_counts[color] += 1
    
    return [color_counts, pixel_classifications]

#function to get color fractions based on specified input of colors to quantify
def get_color_fractions(color_counts, exclude):
    #initialize dictionary to hold output
    color_fractions = {'fractions' : {}}

    #calculate total pixels to count in fraction calculations
    fractioning_total = 0
    for color in color_counts:
        if color not in exclude:
            fractioning_total += color_counts[color]
    
    #calculate color fractions
    for color in color_counts:
        if color not in exclude:
            color_fractions['fractions'][color] = color_counts[color] / fractioning_total
    
    #add fractioned pixels counter to output
    color_fractions['fractioning_pixel_count'] = fractioning_total

    #add raw counts to output
    color_fractions['raw_pixel_counts'] = color_counts

    return color_fractions

#function to write new quantification output file
def write_new_quantification_output(sample, quantifications, fract_outfile):
    pixel_fractions = quantifications['fractions']
    pixel_fractions['sample'] = sample
    outdf = pd.DataFrame([pixel_fractions])
    sample_column = outdf.pop('sample')
    outdf.insert(0, 'sample', sample_column)
    outdf.to_csv(fract_outfile, index=False)

#function to add to previous quantification output file
def add_to_quantification_output(sample, quantifications, previous_output_file):
    pixel_fractions = quantifications['fractions']
    pixel_fractions['sample'] = sample
    outdf = pd.DataFrame([pixel_fractions])
    sample_column = outdf.pop('sample')
    outdf.insert(0, 'sample', sample_column)

    prev_outdf = pd.read_csv(previous_output_file)
    new_outdf = pd.concat([prev_outdf, outdf])
    new_outdf.to_csv(previous_output_file, index=False)

#function to quantify colors
def quantify_colors_ui(image, input, log_window):
    #load data
    log_window.insert(INSERT, f"Loading image...\n")
    log_window.update()
    color_data = load_pixels(image)
    log_window.insert(INSERT, f"Done.\n")
    log_window.insert(INSERT, f"Quantifying pixel values...\n")
    log_window.update()
    #get color quantification
    color_counts = color_counter(color_data, input['color_mappings'])
    log_window.insert(INSERT, f"Done.\n")
    log_window.insert(INSERT, f"Calculating color fractions...\n")
    log_window.update()
    #get color fractions
    color_fractions = get_color_fractions(color_counts[0], exclude=input['colors_to_exclude'])
    log_window.insert(INSERT, f"Done.\n")
    log_window.update()

    return color_fractions