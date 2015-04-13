#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create On Sat Apr 11 2015 10:56:03

@author  : Vic Yu(http://vicyu.net)
'''
from os.path import join, getsize
from os import walk


def calcdirsize(directory):
    size = float()
    for root, directorys, files in walk(directory):
        size += sum([getsize(join(root, filename)) for filename in files])
    return size


def transformtoKMG(size):
    fmt = ['B', 'KB', 'M', 'G', 'T']
    time = 0
    while size > 1024:
        size /= 1024
        time += 1
    return str(size) + fmt[time]


def main():
    print transformtoKMG(calcdirsize('C:\windows'))


if __name__ == '__main__':
    main()
