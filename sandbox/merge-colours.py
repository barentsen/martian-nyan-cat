from PIL import Image

im_red = Image.open('data/H9328_0000_IR2.JPG')
im_green = Image.open('data/H9328_0000_GR2.JPG')
im_blue = Image.open('data/H9328_0000_BL2.JPG')

im_color = Image.merge('RGB', (im_red.crop((0,0,80,700)), im_green.crop((0,0,80,700)), im_blue.crop((0,0,80,700))))

im_color.save('color.png')
