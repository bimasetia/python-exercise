#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 08:47:04 2018

@author: dedisetyadi
"""

from screeninfo import get_monitors

width=get_monitors()[0].width
height=get_monitors()[0].height

print("Width: %s,  Height: %s" % (width, height))