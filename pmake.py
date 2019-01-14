#usage
#python pmake.py --image 3d_pokemon.png -o bright -f1 4
from PIL import Image, ImageDraw
from math import sin, cos, pi
import os
import argparse

def save(option,output):
    dir_path = os.getcwd()
    file_path = os.path.join( dir_path, "output\{}.jpg".format(option) ) #./output
    output.save(file_path)
    print("Saved at {}".format(file_path))

#from rotate import rotate
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True,
	help="path to the input image")
ap.add_argument("-o", "--option",
	help="options: bright,contrast,scale,rotate,crop")
ap.add_argument("-oo", "--option2",
	help="options: Dual effect")
ap.add_argument("-f1", "--factor", type=int or float, default=1,
	help="size of gaussian blur kernel")
ap.add_argument("-f2", "--factor2", type=int or float, default=1,
	help="second factor")
#try:
args = vars(ap.parse_args())
#except:
#    print("-i<input_img>.<extention> -o <option1> -f<factor 1>  is reqd ")
option=args['option']
option2=args['option2']
# Load image:
input_image =Image.open(args["image"])
if option or option2:
    if option=="bright" or  option2=="bright":
        from bright import brightnesss
    # get brightness:
        brightness =args["factor"]
    #brightness function
        output=brightnesss(input_image,brightness)
    #save to output folder
        save(option,output)
    elif option=="rotate" or option2 =="rotate":
        from rotate import rotate
        angle=args["factor"] # angle in radian
        output=rotate(input_image,angle)
        save(option,output)
    elif option=="scale" or option2 =="scale":
    # nearest neighbor algorithm
        from upscale import upscale
        p1=args["factor"] # pixel
        p2=args["factor2"]
        new_size = (p1, p2)
        output=upscale(input_image,new_size)
        save(option,output)
    elif option=="crop" or option2 =="crop":
    # cropping
        from crop import crop
        p1=args["factor"] # pos
        p2=args["factor2"]
        pos = (p1, p2) #origin
        #end defined in crop.py
        output=crop(input_image,pos)
        save(option,output)
    elif option=="contrast" or option2 =="contrast":
        from contrast import change_contrast
        factor=args["factor"] # factor
        output=change_contrast(input_image,factor)
        save(option,output)
    elif option=="noise" or option2 =="noise":
        from noise import noise
        factor=args["factor"] # factor
        output=noise(input_image,factor)
        save(option,output)
else:
    print("Usage: python pmake.py o -i<input_img>.<extention> -o <option1> or -oo<option2> -f1<factor 1> -f2 <factor2>")
