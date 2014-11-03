#!/usr/bin/python

from math import floor
from operator import itemgetter
import os
from PIL import Image
import subprocess
import sys

files = sys.argv[1:]
width = 300
columns = 6

data = []
for file in files:
    im = Image.open(file)
    w, h = im.size
    data.append({"name":file, "height": floor(h*width/w), "x": -1, "y": -1})

data.sort(key=itemgetter("height"), reverse=True)

imgs_per_col = [[x] for x in range(columns)]
size_of_cols = [data[x]["height"] for x in range(columns)]
min_col = columns-1
for i in range(columns):
    data[i]["x"] = i*width
    data[i]["y"] = 0

k = columns
while k < len(data):
    imgs_per_col[min_col].append(k)
    data[k]["x"] = min_col*width
    data[k]["y"] = size_of_cols[min_col]
    size_of_cols[min_col] += data[k]["height"]
    min_col = min(enumerate(size_of_cols), key=itemgetter(1))[0]
    k += 1

subprocess.call("rm -f collage.png", shell=True)
subprocess.call("convert -size {}x{} xc:white collage.png".\
        format(columns*width, max(size_of_cols)), shell=True)
for i in range(len(data)):
    x = data[i]["x"]
    y = data[i]["y"]
    file = data[i]["name"]
    subprocess.call("composite -geometry {}x+{}+{} {} collage.png collage.png".\
            format(width, x, y, file), shell=True)
