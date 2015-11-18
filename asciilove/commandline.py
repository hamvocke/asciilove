# -*- coding: utf-8 -*-

from asciilove import converter
import argparse

parser = argparse.ArgumentParser(description='Convert an image to ASCII art')
parser.add_argument('image', help='image path')
args = parser.parse_args()

def main():
    print(converter.convert(args.image))

if __name__ == "__main__":
    main()

