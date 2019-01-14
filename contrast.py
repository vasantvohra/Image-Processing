from PIL import Image

def change_contrast(input_image,factor1=1, level=200):
    factor = (259 * (level + 255)) / (255 * (259 + level))
    def contrast(c):
        value = 128 + factor1 * (c - 128)
        return max(0, min(255, value))
    return input_image.point(contrast)
"""
# Load image:
input_image = Image.open("input.png")
input_image.load()
c=change_contrast(input_image,2.0)
c.save("cntrst.png")
"""
