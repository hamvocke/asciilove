# -*- coding: utf-8 -*-
from unittest import TestCase
from asciilove import asciilove

class Color():
    red = 0.0
    green = 0.0
    blue = 0.0

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

class ColorCharTest(TestCase):

    def test_char_for_color_should_return_blank_character(self):
        self.assertEqual(asciilove.char_for_color(Color(1.0, 0.0, 0.0)), " ")
        self.assertEqual(asciilove.char_for_color(Color(0.99, 1.0, 0.7)), " ")
        self.assertEqual(asciilove.char_for_color(Color(0.89, 0.9, 0.2)), " ")
        self.assertEqual(asciilove.char_for_color(Color(0.86, 0.2, 0.4)), " ")

    def test_should_return_shade_one(self):
        self.assertEqual(asciilove.char_for_color(Color(0.80, 0.0, 0.0)), "░")
        self.assertEqual(asciilove.char_for_color(Color(0.66, 1.0, 0.0)), "░")
        self.assertEqual(asciilove.char_for_color(Color(0.799, 0.0, 0.95)), "░")
        self.assertEqual(asciilove.char_for_color(Color(0.65, 0.4, 0.6)), "░")

