#!/usr/bin/env python

import os
 
path = "/foo/var/"
for root, dirs, files in os.walk(path):
    for file in files:
        print(file)

#
print(__file__)

#
print(os.getcwd())

#
print(os.path.basename(__file__))

#
print(os.path.abspath(__file__))

#
print(os.path.dirname(os.path.abspath(__file__)))
