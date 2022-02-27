
from PIL import Image


def crop(bigimage, smallsize, wider, taller):
    w, h = bigimage.size
    if wider:
        w -= smallsize[0]
    if taller:
        h -= smallsize[1]

    left = 0        # Setting the points for cropped image
    right = bigimage.size[0]-1
    top = 0
    bottom = bigimage.size[1]-1
    if wider:
        left = w//2
        right = left + smallsize[0]
    if taller:
        top = h//2
        bottom = top + smallsize[1]

    return bigimage.crop((left, top, right, bottom))


# TODO
# if images are not the same size
#   if hiding image is wider, but not taller
#   if hiding image is not wider, but is taller
#   if displayed image is wider and taller
# artificially brighten/darken images?
# output more than 1 decrypted image, looking at different numbers of least significant bits
# recommend darker displayed images
if __name__ == '__main__':
    op = input('Are you encrypting or decrypting a photo?\n').lower()
    if op[0] == 'e':
        fname = input('What is the name of the photo you are hiding?\n')
        imh = Image.open(fname)
        hiding = imh.load()
        hsize = imh.size
        fname = input('What is the name of the photo you are hiding it in?\n')
        im = Image.open(fname)
        displayed = im.load()
        width, height = im.size
        if hsize[0] > width or hsize[1] > height:
            hiding = crop(imh, im.size, imh.size[0] > im.size[0], imh.size[1] > im.size[1]).load()
        for i in range(width):
            for j in range(height):
                hpixel = hiding[i, j]
                dpixel = displayed[i, j]
                R = (dpixel[0] & 240) + ((hpixel[0]) >> 4)
                G = (dpixel[1] & 240) + ((hpixel[1]) >> 4)
                B = (dpixel[2] & 240) + ((hpixel[2]) >> 4)
                # R = (dpixel[0] & 248) + ((hpixel[0]) >> 5) for very hidden
                # G = (dpixel[1] & 248) + ((hpixel[1]) >> 5)
                # B = (dpixel[2] & 248) + ((hpixel[2]) >> 5)
                displayed[i, j] = (R, G, B)
        im.save('hidden.png')
    elif op[0] == 'd':
        fname = input('What is the name of the photo you are decrypting?\n')
        im = Image.open(fname)
        hidden = im.load()
        width, height = im.size
        for i in range(width):
            for j in range(height):
                pixel = hidden[i, j]
                hidden[i, j] = ((pixel[0] & 15) << 4, (pixel[1] & 15) << 4, (pixel[2] & 15) << 4)
                # hidden[i, j] = ((pixel[0] & 7) << 5, (pixel[1] & 7) << 5, (pixel[2] & 7) << 5) for very hidden
        im.save('found.png')
