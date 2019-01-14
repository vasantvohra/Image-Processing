# Image Processing
Princeton University ASSIGNMENT - https://www.cs.princeton.edu/courses/archive/spring14/cos426/assignment1/examples.html
<p align="center">
    <img src="https://github.com/vasantvohra/Image-Processing/blob/master/output2.png?raw=true" alt="Output"/>
</p>
*!!! PYTHON CODE !!!*

File Structure

output/ - Empty to start.  Automatically writes the output images produced by the program into this folder with filter or option used.
 *Do have a look before start*

src/ - Directory with source code.
<p align="center">
    <img src="https://github.com/vasantvohra/image-processing/blob/master/cmd.PNG?raw=true" alt="CMD"/>
</p>
		#COMMANDLINE ARGUMENTS

	1. pmake.py - Python file to run the functions like:
	USAGE: python pmake.py -i<image_path>.<extention> -o <option> -f1<int_factor> -f2 <factor2>
	to run	bright : python pmake.py --image 3d_pokemon.png -o bright -f1 4
		scale : python pmake.py --image 3d_pokemon.png -o scale -f1 1080 -f2 1080 
		rotate: python pmake.py --image 3d_pokemon.png -o bright -f1 2 
		contrast: python pmake.py --image input.png -o contrast -f1 -1 
		Or
		python pmake.py -i input.png

	2. filter.py - Python file for convolution functions
	USAGE: python filter.py --image <image name>.<extention> -k <kernelname>
	or
	# python filter.py --image <image name>.<extention>
	Example: SHARPEN: python filter.py --image input.png -k sharpen
		Gaussian blur: python filter.py --image input.png -k gaussian blur
		EDGE: python filter.py --image input.png -k edge
	or
	python filter.py --image input.png - for running all the filters
	or
	python filter.py --image input.png -kernel sharpen

HELP:
python filter.py --help
python pmake.py --help

HOW to PROCEED
==============
1. install python! version=3.6
2. library install  : Python imaging library

pip install -r requirements.txt or pip install pillow , pip install numpy


3.In windows :
Command prompt:
Cd- change directory to python installation : python36\scripts
then, step 2.

After library installation:
Extract this zip to python installation //python.exe and py files are in same directory.

4.RUN ARGUMENTS:
 
if Linux or Mac OSX 
--Run above mentioned commands on pmake and filter
#Warning: Output folder images will change automatically with change in input image
After extracting anywhere.

5. Hope all the codes work!

UPDATE:
---To run alpha composite:
In Windows, pip install opencv
Linux, browse WEB!
CMD: python alpha.py
<p>
    <img src="https://github.com/vasantvohra/image-processing/blob/master/1.jpg?raw=true" alt="Original"/>
	<img src="https://github.com/vasantvohra/image-processing/blob/master/2.jpg?raw=true" alt="alpha"/>
	<img src="https://github.com/vasantvohra/image-processing/blob/master/alpha composite.jpg?raw=true" alt="Alpha composite"/>
</p>
Waiting for a positive response!