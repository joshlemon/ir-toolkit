#!/usr/bin/env python

from __future__ import print_function
from datetime import datetime, timedelta
import optparse, time

__description__ = "Displays current, timeshifted and converts time commonly used by Incident Responders"
__author__ = 'Josh Lemon'
__version__ = '0.0.1'
__date__ = '2017/11/13'

"""
Source code put in public domain by Josh Lemon
https://www.joshlemon.com.au
Use at your own risk

History:
  2017/11/13: 0.0.1 first release

Todo:
  Allow for multipue time zones to be printed out.
  Acccept a timezone and print out the current time in that timezone.
"""

def currenttime(convertepochtime=time.time()):
    print(time.ctime(convertepochtime))
    

def currentutctime():
    print(str(datetime.utcnow()) + " UTC")

def epochtime():
    print(time.time())
    
def timeshift(shifted, printutctime, printepoch):
    hrs = int(shifted[0])
    mins = int(shifted[1])
    
    if printutctime:
        printtime = datetime.utcnow()
    else:
        printtime = datetime.now()
    
    timeshifted = printtime + timedelta(hours=+hrs, minutes=+mins)
    
    if printepoch:
        print(time.mktime(timeshifted.timetuple()))
    else:
        print(timeshifted)

def main():
    parser=optparse.OptionParser(usage='usage: %prog [options]\n' + __description__, version='%prog ' + __version__)
    parser.add_option('-m', '--man', action='store_true', default=False, help='Print manual')
    parser.add_option('-u','--utctime',action='store_true',default=False, help='Print time output as UTC time')
    parser.add_option('-e','--epochtime',action='store_true',default=False, help='Print time output in Unix Epoch time')
    parser.add_option('-E','--ConvertEpochTime',action='store',default=False, help='Converts Unix Epoch time to human readable time')
    parser.add_option('-s','--TimeShift',action='store',default=False, help='Prints the current time plus/minus the given hours:mins')
    (options, args)=parser.parse_args()
    
    if options.man:
        parser.print_help()
        return
    
    if options.TimeShift:
        timeshift(options.TimeShift.split(':'), options.utctime, options.epochtime)
    elif options.epochtime:
        epochtime()
    elif options.ConvertEpochTime:
        currenttime(float(options.ConvertEpochTime))
    elif options.utctime:
        currentutctime()
    else:
        currenttime()

if __name__ == '__main__':
    main()