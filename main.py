from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()

red_coordinates1 = (101, 0, red.width, red.height)
red_coordinates2 = (50, 0, 645, red.height)
blue_coordinates1 = (50, 0, 645, blue.height)
blue_coordinates2 = (0, 0, 595, blue.height)
green_coordinates = (50, 0, 645, green.height)

red_left = red.crop(red_coordinates1)
red_middle = red.crop(red_coordinates2)
complete_red = Image.blend(red_left, red_middle, 0.5)

blue_middle = blue.crop(blue_coordinates1)
blue_right = blue.crop(blue_coordinates2)
complete_blue = Image.blend(blue_middle, blue_right, 0.5)
complete_green = green.crop(green_coordinates)

complete_monro = Image.merge('RGB', (complete_red, complete_green, complete_blue))
complete_monro.save('complete_monro.jpg')

monro_image = Image.open("complete_monro.jpg")
monro_image.thumbnail((80, 80))
monro_image.save('monro_avatar.jpg')
