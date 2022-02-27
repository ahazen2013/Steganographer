# Steganographer

This program uses a cryptographic technique called steganography to hide an image inside another image, or to find an image hidden using this technique.

A digital image is a collection of pixels. Each pixel in an image has a color, which is represented by an RGB value- the
amount of red, green, and blue in the pixel, each on a scale of 0-255. In binary, these values range from 00000000 to 11111111.
When encrypting an image, this program looks at each color component of each pixel in both images, takes the first four binary digits of each color
component in the image to be hidden, and overwrites the last four digits of the same color component in the corresponding
pixel in the image to be displayed. When decrypting an image, it does the inverse- it looks at each pixel in the image
to be decrypted, takes the last four digits of each color component in the pixel, and changes the color component so
that the value is equal (in binary) to those four digits with four 0s at the end.