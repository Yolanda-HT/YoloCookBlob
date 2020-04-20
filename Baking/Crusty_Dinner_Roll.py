#!/usr/bin/env python
# -*- coding: utf-8 -*-

class flour():
    def __init__(self, f_type, **kwargs):
        self.type = f_type
        self.scale_and_quantity = {}
        for key, value in kwargs.items():
            self.scale_and_quantity[key] = value
        

class bread():
    def __init__(self, flour, water, sugar, salt, yeast, butter, starter=None, **kwargs):
        self.flour = flour
        self.water = water
        self.sugar = sugar
        self.salt = salt
        self.yeast = yeast
        self.butter = butter
        



weight_dict = {'gram': 100}
hf = flour("all_purpose", gram=100)
hf.scale_and_quantity
