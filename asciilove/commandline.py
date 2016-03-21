# -*- coding: utf-8 -*-

import converter
import argparse

parser = argparse.ArgumentParser(description='Convert an image to ASCII art')
parser.add_argument('image', help='image path')
parser.add_argument('-n', '--negative', help='print negative version of the input file (useful when using a dark CLI theme)', action='store_true')
args = parser.parse_args()

def main():
    print(converter.convert(args.image, negative=args.negative))

if __name__ == "__main__":
    main()
