# USAGE
# python bright.py --image <<image name>.<extention> --bright <value>

from PIL import Image, ImageDraw
import os
dir_path = os.getcwd()
import argparse

def brightnesss(input_image,luminosity):
    input_pixels = input_image.load()

# Create output image
    output_image = Image.new("RGB", input_image.size)
    draw = ImageDraw.Draw(output_image)

# Generate image
    for x in range(output_image.width):
        for y in range(output_image.height):
            r, g, b = input_pixels[x, y]
            r = int(r * luminosity) #or + luminosity
            g = int(g * luminosity)
            b = int(b * luminosity)
            draw.point((x, y), (r, g, b))
    
    return output_image
"""
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True,
	help="path to the input image")
ap.add_argument("-b", "--bright", type=int or float, default=2,
	help="size of gaussian blur kernel")

args = vars(ap.parse_args())
# Load image:
input_image =Image.open(args["image"])
# get brightness:
brightness =args["bright"]
#brightness function
output=brightnesss(input_image,brightness)
#save to output folder
file_path = os.path.join( dir_path, "output\{}.jpg".format("bright") )
output.save(file_path)
print("Saved at {}".format(file_path))
"""
