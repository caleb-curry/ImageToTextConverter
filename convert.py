#! /usr/bin/python3
import sys
import numpy
from PIL import Image

img_file = sys.argv[1]
img = Image.open(img_file, 'r')
width, height = 64, 64
# Convert to PNG
img = img.convert("RGBA")
# Change image size
img = img.resize((width, height))
img.save("resize.png")
width, height = img.size
#print(width, height)
pixel_values = list(img.getdata())
img_array = []
for pixel in pixel_values:
    avg = (int(pixel[0]) + int(pixel[1]) + int(pixel[2]) + int(pixel[3]))/4
    if avg == 0:
        img_array.append(" ")
    elif avg > 0 and avg <= 16:
        img_array.append(".")
    elif avg > 16 and avg <= 32:
        img_array.append("+")
    elif avg > 32 and avg <= 48:
        img_array.append("=")
    elif avg > 48 and avg <= 64:
        img_array.append("a")
    elif avg > 64 and avg <= 80:
        img_array.append("f")
    elif avg > 80 and avg <= 96:
        img_array.append("d")
    elif avg > 96 and avg <= 112:
        img_array.append("x")
    elif avg > 112 and avg <= 128:
        img_array.append("e")
    elif avg > 128 and avg <= 144:
        img_array.append("T")
    elif avg > 144 and avg <= 160:
        img_array.append("8")
    elif avg > 160 and avg <= 176:
        img_array.append("0")
    elif avg > 176 and avg <= 192:
        img_array.append("M")
    elif avg > 192 and avg <= 208:
        img_array.append("%")
    elif avg > 208 and avg <= 224:
        img_array.append("$")
    else:
        img_array.append("@")

count = 0
for i in range(0,width*height):
    if(count < width-1):
        print(img_array[i], end=" ")
        count += 1
    else:
        print(img_array[i])
        count = 0
print("\n")