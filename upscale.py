# USAGE
# python upscale.py --image <<image name>.<extention>

# nearest neighbor algorithm
from PIL import Image, ImageDraw
from math import floor
from PIL import Image, ImageDraw
import os
dir_path = os.getcwd()
import argparse

def upscale(input_image,new_size):
    input_pixels = input_image.load()
    # Create output image
    output_image = Image.new("RGB", new_size)
    draw = ImageDraw.Draw(output_image)

    x_scale = input_image.width / output_image.width
    y_scale = input_image.height / output_image.height

# Copy pixels
    for i in range(output_image.width):
        for j in range(output_image.height):
            xp, yp = floor(i * x_scale), floor(j * y_scale)
            draw.point((i,j), input_pixels[xp, yp])
            
    return output_image

#new_size = (1080, 1080) #upscale position #input argument
#new_size = (300, 300) #downscale position
"""
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True,
	help="path to the input image")
args = vars(ap.parse_args())
# Load image:
input_image =Image.open(args["image"])
#brightness function
output=upscale(input_image,new_size)
#save to output folder
file_path = os.path.join( dir_path, "output\{}.jpg".format("upscaled") )
output.save(file_path)
print("Saved at {}".format(file_path))
"""
