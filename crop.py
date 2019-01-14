from PIL import Image, ImageDraw
# Cropped area
origin = (130, 150)
def crop(input_image,origin=origin):
    input_pixels = input_image.load()
    end = (400, 320)
    # Create output image
    output_image = Image.new("RGB", (end[0] - origin[0], end[1] - origin[1]))
    draw = ImageDraw.Draw(output_image)
    for x in range(output_image.width):
        for y in range(output_image.height):
            xp, yp = x + origin[0], y + origin[1]
            draw.point((x, y), input_pixels[xp, yp])
    return output_image
