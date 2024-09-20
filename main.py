from PIL import Image

image = Image.open('monro.jpg')
print(image.mode) 
red, green, blue = image.split()

new_image = Image.merge("RGB", (red, green, blue))
red_coordinates = (50, 0, red.width, red.height)
blue_coordinates = (-50, 0, blue.width, blue.height)
red_cropped = new_image.crop(red_coordinates)