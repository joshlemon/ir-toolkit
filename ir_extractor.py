#!/usr/bin/env python

from __future__ import print_function

__description__ = "Python script for pulling common regex information for IR analysts"
__author__ = 'Josh Lemon'
__version__ = '0.0.1'
__date__ = '2017/08/07'

import re, sys, argparse

def findURLs(input_data):
	# = re.findall(r'',args.input_data)
	url_regex = re.compile(
        r'(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)'
        r'(?:[A-Z0-9./?-_=:]*)'
        , re.IGNORECASE)
	
	return(url_regex.findall(input_data))

def findEmails(input_data):
	email_regex = re.compile(
	        r'[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]{2,6}' # quoted-string
	        , re.IGNORECASE)
	
	return(email_regex.findall(input_data))

def outToList(list, sort):
	if list:
		if sort:
			for r in sorted(list):
				print(r)
		else:
			for r in list:
				print(r)
	else:
		print("Nothing find.....sorry")

def Main():
	parser=argparse.ArgumentParser()
	parser.add_argument('-u','--urls',action='store_true',required=False, help='Extract URL address from the data provided')
	parser.add_argument('-e','--emails',action='store_true',required=False,help='Extract email address from the data provided')
	parser.add_argument('-s','--sort',action='store_true',required=False,help='Sort the extracted data')
	parser.add_argument('-c','--count',action='store_true',required=False,help='Perform a count of each item found')
	args=parser.parse_args()

	input_data = sys.stdin.read()

	if not input_data:
		parser.print_help()
		sys.exit(1)

	if args.urls:
		print("----Finding URLs----")
		outToList(findURLs(input_data),args.sort)

	if args.emails:
		print("----Finding Email Addresses----")
		outToList(findEmails(input_data),args.sort)


if __name__ == '__main__':
    Main()