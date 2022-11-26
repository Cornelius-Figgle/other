# pebis
# -*- coding: UTF-8 -*-

# https://github.com/Cornelius-Figgle/other

'''
A random quote generator for Alex

Pulls quotes from `quotes.txt` or `sys.argv[1]`, which is actually a `csv` file
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


def loader(path_to_use: str) -> List:
    '''
    loads `quotes` from `path_to_use`
    '''

    with open(path_to_use) as file:
        reader = csv.reader(file)
        quotes = list(reader)

        quotes = sum(quotes, [])
        for quote in quotes:
            quotes[quotes.index(quote)] = quote.strip()
    
    return quotes

def selector(quotes: list) -> None:
    ...


def main() -> None:
    '''
    The main function that handles passing or args and return values.
    Also handles the application loop and errors from functions
    '''

    if (sys.argv[1] and os.path.exists(sys.argv[1]) 
    and os.access(sys.argv[1], os.X_OK | os.W_OK)):
        path_to_use = sys.argv[1]
    else:
        path_to_use = os.path.join(file_base_path, 'quotes.txt') 

    quotes = loader(path_to_use)

if __name__ == '__main__':
    main()
