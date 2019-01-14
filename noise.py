import numpy as np
from PIL import Image, ImageDraw
def noise(input_image,mean):
    input_image.load()
    im = np.asarray(input_image, dtype="int32" )
    #mean = 0.0 # some constant
    std = 1    # some constant (standard deviation)
    noisy_img = im + np.random.normal(mean, std, im.shape)
    noisy_img_clipped = np.array(np.clip(noisy_img, 0, 255),dtype=np.uint8)
    img = Image.fromarray( noisy_img_clipped,"RGB" )
    return img
