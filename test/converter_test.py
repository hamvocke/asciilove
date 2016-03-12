# -*- coding: utf-8 -*-

from unittest import TestCase
from asciilove import converter

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
        self.assertEqual(converter.char_for_color(Color(1.0, 0.0, 0.0)), " ")
        self.assertEqual(converter.char_for_color(Color(0.923, 0.9, 0.2)), " ")
        self.assertEqual(converter.char_for_color(Color(0.821, 0.4, 0.6)), " ")

    def test_should_return_shade_one(self):
        self.assertEqual(converter.char_for_color(Color(0.799, 0.0, 0.0)), "░")
        self.assertEqual(converter.char_for_color(Color(0.723, 0.0, 0.95)), "░")
        self.assertEqual(converter.char_for_color(Color(0.601, 0.4, 0.6)), "░")

    def test_should_return_shade_two(self):
        self.assertEqual(converter.char_for_color(Color(0.599, 0.0, 0.0)), "▒")
        self.assertEqual(converter.char_for_color(Color(0.501, 1.0, 0.0)), "▒")
        self.assertEqual(converter.char_for_color(Color(0.4, 0.4, 0.6)), "▒")

    def test_should_return_shade_three(self):
        self.assertEqual(converter.char_for_color(Color(0.399, 0.0, 0.0)), "▓")
        self.assertEqual(converter.char_for_color(Color(0.25, 0.0, 0.95)), "▓")
        self.assertEqual(converter.char_for_color(Color(0.2, 0.4, 0.6)), "▓")

    def test_should_return_shade_four(self):
        self.assertEqual(converter.char_for_color(Color(0.199, 0.0, 0.0)), "█")
        self.assertEqual(converter.char_for_color(Color(0.15, 0.0, 0.95)), "█")
        self.assertEqual(converter.char_for_color(Color(0.05, 0.4, 0.6)), "█")

class RoundingTest(TestCase):
    def test_should_round_with_one_decimal_precision(self):
        self.assertEqual(converter.round(0.0124), 0.0)
        self.assertEqual(converter.round(0.243), 0.2)
        self.assertEqual(converter.round(0.899), 0.8)

    def test_should_truncate_negative_numbers(self):
        self.assertEqual(converter.round(-0.0124), 0.0)
        self.assertEqual(converter.round(-0.5), 0.0)
