# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 17:35:31 2025

@author: HITS
"""
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
    
