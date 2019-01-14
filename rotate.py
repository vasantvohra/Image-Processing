# USAGE
# python rotate.py --image <image name>.<extention> --angle <value>

from PIL import Image, ImageDraw
from math import sin, cos, pi
def rotate(input_image,angle):
    # Create output image
    input_pixels = input_image.load()
    output_image = Image.new("RGB", input_image.size)
    draw = ImageDraw.Draw(output_image)
    center_x = input_image.width / 2
    center_y = input_image.height / 2
    for x in range(input_image.width):
        for y in range(input_image.height):
        # Compute coordinate in input image
            xp = int((x - center_x) * cos(angle) - (y - center_y) * sin(angle) + center_x)
            yp = int((x - center_x) * sin(angle) + (y - center_y) * cos(angle) + center_y)
            if 0 <= xp < input_image.width and 0 <= yp < input_image.height:
                draw.point((x, y), input_pixels[xp, yp])
    return output_image
"""
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
ap.add_argument("-a", "--angle", type=int or float, default=2,
	help="angle for rotate")
args = vars(ap.parse_args())
# Load image:
input_image = Image.open(args["image"])
# get angle:
angle=args["angle"] # angle in radian
output=rotate(input_image,angle)
file_path = os.path.join( dir_path, "output\{}.jpg".format("rotated") )
output.save(file_path)
print("Saved at {}".format(file_path))
"""
