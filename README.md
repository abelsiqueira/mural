# Mural

This is a python script to generate a montage of pictures.  Defining a width W
and number of columns NC, this generates an image with width _W*NC_, such that
every image passed as argument is in it, and all are scaled to have width W.
This algorithm does not leave unused width space, but can leave height space at
the bottom. It does not look to minimize the amount of white space left in the
bottom.

## Requirement

This script needs the package `pillow` and Image Magick.

## Usage

Modify the script to define your width and number of columns.

    ./mural.py FILES
