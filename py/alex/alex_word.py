# pebis
# -*- coding: UTF-8 -*-

# https://github.com/Cornelius-Figgle/other

'''
A random quote generator for Alex

Pulls quotes from `quotes.txt` which is actually a `csv` file
'''

# note: view associated GitHub info as well
__version__ = 'Pre-release'  
__author__ = 'Cornelius-Figgle'
__email__ = 'max@fullimage.net'
__maintainer__ = 'Cornelius-Figgle'
__copyright__ = 'Copyright (c) 2022 Max Harrison'
__license__ = 'MIT'
__status__ = 'Development'
__credits__ = ['Max Harrison', 'Alex Ceaton', 'Ashe~ Ceaton']


import csv
import os
import sys

if hasattr(sys, '_MEIPASS'):
    # source: https://stackoverflow.com/a/66581062/19860022
    file_base_path = sys._MEIPASS
    # source: https://stackoverflow.com/a/36343459/19860022
else:
    file_base_path = os.path.dirname(__file__)



def main() -> None:
    with open(os.path.join(file_base_path, 'quotes.txt')) as file:
        reader = csv.reader(file)
        quotes = list(reader)
    
    print('Hello World')

if __name__ == '__main__':
    main()