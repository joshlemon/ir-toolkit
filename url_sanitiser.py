#!/usr/bin/env python

from __future__ import print_function
import sys


__description__ = "Sanitises URLs so they don't resolve to hrefs when pasted into web apps"
__author__ = 'Josh Lemon'
__version__ = '0.0.2'
__date__ = '2017/08/23'


"""
Source code put in public domain by Josh Lemon
https://www.joshlemon.com.au
Use at your own risk

History:
  2017/08/15: 0.0.1 first release
  2017/08/23: 0.0.2 added the ability to parse the pipe "|" character from the input

Todo:
  add ability to unsanitise a URL with a switch
"""


def sanitiseurl(urls):
    print(urls.replace('.', '[.]').replace('http', 'hxxp').replace(',', '\n').replace('|', '\n').replace(' ', '\n'))

def unsanitiseurl(urls):
    print(urls.replace('[.]', '.').replace('hxxp', 'http').replace(',', '\n').replace('|', '\n').replace(' ', '\n'))


def main():
    try:
        if len(sys.argv) > 1:
            for i in sys.argv:
                if sys.argv.index(i) != 0:
                    sanitiseurl(i)

        elif sys.stdin:
            sanitiseurl(sys.stdin.read())
    except:
        print("Umm....this is embarrassing, I've run into an error")
        exit(-1)


if __name__ == '__main__':
    main()
