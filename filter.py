#importing 
# USAGE
# python filter.py --image <image name>.<extention>
# python filter.py --image <image name>.<extention> -k <kernelname>
#if not valid return doesn't exist

import os
dir_path = os.getcwd()
import argparse
from PIL import Image, ImageDraw

#convolution function

def convolve(input_image,kernel):
    input_pixels = input_image.load()
    # Middle of the kernel
    offset = len(kernel) // 2
    # Create output image
    output_image = Image.new("RGB", input_image.size)
    draw = ImageDraw.Draw(output_image)
    for x in range(offset, input_image.width - offset):
        for y in range(offset, input_image.height - offset):
            acc = [0, 0, 0]
            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - offset
                    yn = y + b - offset
                    pixel = input_pixels[xn, yn]
                    acc[0] += pixel[0] * kernel[a][b]
                    acc[1] += pixel[1] * kernel[a][b]
                    acc[2] += pixel[2] * kernel[a][b]

            draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))
    return output_image
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
ap.add_argument("-k", "--kernel",
	help="kernel to be used: sharpen,edge,gaussian_blur")
args = vars(ap.parse_args())
Kernel = args["kernel"]
#Sharpening kernel
sharpen = [[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]]
#Edge 
edge = [[  -1  ,-1 ,    -1 ],
          [-1 ,   8  , -1 ],
         [  -1  , -1,   -1 ]]
# Box Blur kernel
box_kernel = [[1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9]]

# Gaussian kernel
gaussian_kernel = [[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]]
# construct the kernel bank, a list of kernels we're going
# to apply using custom 'convole' function 
kernelBank = (
	("Sharpen", sharpen),
                    ("Edge", edge),
                     ("Gaussian kernel", gaussian_kernel),
            ("Box kernel", box_kernel),
)
kernelBank2 = {"sharpen":sharpen,"edge":edge ,"gaussian_blur": gaussian_kernel,"Box kernel": box_kernel}

# Load image:
input_image = Image.open(args["image"])
# loop over the kernels
if Kernel:
    try:
        kernel=kernelBank2[Kernel]   
        print("[INFO] applying {} kernel".format(Kernel))
        convoleOutput = convolve(input_image,kernel)
        file_path = os.path.join( dir_path, "output\{}.jpg".format(Kernel) )
        convoleOutput.save(file_path)  
        print("Saved at {}".format(file_path))
    except:
        print("Doesn't exist")
else:
    for (kernelName, kernel) in kernelBank:
        print("[INFO] applying {} kernel".format(kernelName))
        convoleOutput = convolve(input_image,kernel)
        file_path = os.path.join( dir_path, "output\{}.jpg".format(kernelName) )
        convoleOutput.save(file_path)  
        print("Saved at {}".format(file_path))
