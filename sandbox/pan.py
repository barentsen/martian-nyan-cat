"""The module provides a function to transform a Mars scan into panning frames.
"""
import PIL
from PIL import Image
import numpy as np
import os
from astropy import log

# Configuration
DATAPATH = 'data'
OUTPUTPATH = 'output'

# Desired resolution for YouTube is 426x240
RES_X = 426
RES_Y = 240

# Pre-load nyan cat
NYANFRAMES = []
for i in range(12):
    NYANFRAMES.append( Image.open('nyanframes/nyanf{0}.gif'.format(i+1)).resize((RES_Y, RES_Y), PIL.Image.ANTIALIAS) )


def animate(prefix, nyan=True, nyancount=0):
    """Animates a Mars image into a panning set of frames."""
    log.info('Processing '+prefix)
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
    pixels_per_step = int(width/200)  # Number of pixels panned per frame
    for i, delta in enumerate(np.arange(0, int(width-cropwidth), pixels_per_step)):
        tmp = im.crop((delta, 0, int(delta + cropwidth), height))
        tmp = tmp.resize((RES_X, RES_Y), PIL.Image.ANTIALIAS)

        if nyan:
            nyancount += 1
            nyanid = nyancount % len(NYANFRAMES)
            nyan = NYANFRAMES[nyanid]
            nyan_width, nyan_height = NYANFRAMES[nyanid].size
            tmp.paste(NYANFRAMES[nyanid],
                      box=(0, 0, nyan_width, nyan_height),
                      mask=NYANFRAMES[nyanid].convert('RGBA').split()[3])

        output_filename = os.path.join(OUTPUTPATH,
                                      '{0}_{1:07d}.jpg'.format(prefix, i))
        tmp.save(output_filename)
    return nyancount

if __name__ == '__main__':
    NYAN = True
    nyancount = -1
    nyancount = animate('H9328_0000', nyan=NYAN, nyancount=nyancount)
    nyancount = animate('H9329_0000', nyan=NYAN, nyancount=nyancount)
    nyancount = animate('H9331_0000', nyan=NYAN, nyancount=nyancount)
    nyancount = animate('H9333_0000', nyan=NYAN, nyancount=nyancount)
    nyancount = animate('H9334_0000', nyan=NYAN, nyancount=nyancount)
    nyancount = animate('H9335_0000', nyan=NYAN, nyancount=nyancount)

