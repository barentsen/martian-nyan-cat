"""The module provides a function to transform a Mars scan into panning frames.

Desired resolution for YouTube is 426x240
"""
import PIL
from PIL import Image
import numpy as np
import os

RES_X = 426
RES_Y = 240
DATAPATH = 'data'
OUTPUTPATH = 'output'

def animate(prefix):
    """Animates a Mars image into a panning set of frames."""
    images = []
    for suffix in ['_RE2.JPG', '_GR2.JPG', '_BL2.JPG']:
        filename = os.path.join(DATAPATH, prefix + suffix)
        images.append(Image.open(filename).transpose(Image.ROTATE_90))

    width, height = images[0].size
    im = Image.merge('RGB', (images[0].crop((0, 0, width, height)),
                             images[1].crop((0, 0, width, height)),
                             images[2].crop((0, 0, width, height))))

    resolution = height / float(RES_Y)

    cropwidth = RES_X * resolution
    for i, delta in enumerate(np.arange(0, int(width-cropwidth))):
        tmp = im.crop((delta, 0, int(delta + cropwidth), height))
        tmp = tmp.resize((RES_X, RES_Y), PIL.Image.ANTIALIAS)
        output_filename = os.path.join(OUTPUTPATH,
                                      '{0}_{1:04d}.jpg'.format(prefix, i))
        tmp.save(output_filename)

if __name__ == '__main__':
   animate('H9328_0000')
