#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2015 Vic Yu.
# This file is coming from python-script
# - https://github.com/Vic020/python-script
# See the file 'LICENSE' for copying permission.
import os
import sys
import math
import getopt
from PIL import Image

MODE = 'RGBA'
LIMIT = 4


def usage():
    print """
Everything2Image
========================================
This script make a (any) file to a image.
This file is coming from python-script - https://github.com/Vic020/python-script
                        --Vic Yu

options:
    -h --help help
    -e encrypt a file(s).[Default:You will get the same-name image file(s)]
    -d decrypt a image file(s).
    """


def encryToImage(filename):
    with open(filename, 'rb') as f:
        filesize = os.path.getsize(filename)
        filesizesqrt = int(math.ceil(math.sqrt(filesize / LIMIT)))
        imageSize = (filesizesqrt, filesizesqrt)
        newImage = Image.new(MODE, imageSize)
        pixels = newImage.load()
        i = 0
        x = 0
        y = 0
        for c in f.read():
            if i == LIMIT:
                i %= LIMIT
                y += 1
                if y == filesizesqrt:
                    y %= filesizesqrt
                    x += 1
            tmp = list(pixels[x, y])
            tmp[i] = ord(c)
            pixels[x, y] = tuple(tmp)
            i += 1
        tmpname, tmpext = os.path.splitext(filename)

        pixels[filesizesqrt - 1,
               filesizesqrt - 1] = tuple([ord(s) for s in tmpext[1:]])
        imageName = tmpname + '.png'
        imageDir = os.path.split(os.path.abspath(filename))[0]
        newImage.save(os.path.join(imageDir, imageName))
        print 'Encrypt successfully: \n\t%s -> %s' % (filename,
                                                      os.path.join(imageDir,
                                                      imageName))


def decryToNormal(filename):
    outfilename, tmpext = os.path.splitext(filename)
    outfilename = os.path.join(os.path.split(os.path.abspath(filename))[0],
                               outfilename)
    image = Image.open(filename)
    pixels = image.load()
    x, y = image.size
    outfileext = '.' + \
                 ''.join([chr(z) for z in list(pixels[x - 1,
                                                      y - 1]) if z != 255])
    with open(outfilename+outfileext, 'wb') as f:
        for i in xrange(x):
            for j in xrange(y):
                tmp = ''.join([chr(z) for z in list(pixels[i, j])])
                f.write(tmp)
        print 'Decrypt successfully: \n\t%s -> %s' % (filename,
                                                      outfilename+outfileext
                                                      )


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hed", ["help"])
    except getopt.GetoptError, e:
        usage()
        print e
        sys.exit(2)
    print
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o == "-e":
            for filename in args:
                encryToImage(filename)
            sys.exit()
        elif o == "-d":
            for filename in args:
                decryToNormal(filename)
            sys.exit()
    usage()


if __name__ == '__main__':
    main()
