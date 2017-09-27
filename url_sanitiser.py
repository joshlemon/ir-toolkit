#!/usr/bin/env python

from __future__ import print_function
import sys, argparse


__description__ = "Sanitises URLs so they don't resolve to hrefs when pasted into web apps"
__author__ = 'Josh Lemon'
__version__ = '0.1.0'
__date__ = '2017/09/28'


"""
Source code put in public domain by Josh Lemon
https://www.joshlemon.com.au
Use at your own risk

History:
  2017/08/15: 0.0.1 first release
  2017/08/23: 0.0.2 added the ability to parse the pipe "|" character from the input
  2017/09/28: 0.1.0 add ability to unsanitise a URL with a switch

Todo:
  clean up STDIN so a switch can be used with STDIN
"""


def sanitiseurl(urls):
    print(urls.replace('.', '[.]').replace('http', 'hxxp').replace(',', '\n').replace('|', '\n').replace(' ', '\n'))

def unsanitiseurl(urls):
    print(urls.replace('[.]', '.').replace('hxxp', 'http').replace(',', '\n').replace('|', '\n').replace(' ', '\n'))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-s','--sanitiseURL',action='store',required=False, default=sys.stdin, help='Sanitise URLs from the data provided')
    parser.add_argument('-u','--unsanitiseURL',action='store',required=False, help='Unsanitise URLs from the data provided')
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)
    args=parser.parse_args()
    
    if args.unsanitiseURL is None:
        try:
            if len(sys.argv) > 1:
                for i in sys.argv:
                    if sys.argv.index(i) >1:
                        sanitiseurl(i)
    
            elif sys.stdin:
                sanitiseurl(sys.stdin.read())
        except:
            parser.print_help()
            exit(-1)
    else:
        try:
            if len(sys.argv) > 1:
                for i in sys.argv:
                    if sys.argv.index(i) > 1:
                        unsanitiseurl(i)
    
            elif sys.stdin:
                unsanitiseurl(sys.stdin.read())
        except:
            parser.print_help()
            exit(-1)

if __name__ == '__main__':
    main()
