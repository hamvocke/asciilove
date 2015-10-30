# -*- coding: utf-8 -*-

import asciilove
import argparse

parser = argparse.ArgumentParser(description='Convert an image to ASCII art')
parser.add_argument('image', help='image path')
args = parser.parse_args()

def main():
    print asciilove.convert(args.image)

