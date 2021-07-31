#!/usr/bin/env python
#https://docs.python.org/ja/3/library/argparse.html#module-argparse

import argparse

parser = argparse.ArgumentParser(description='')

parser.add_argument(
    "-f", "--file", dest="filename", metavar="FILE",
    action='store', type=str,
    help="write report to FILE",
    nargs=1
)

parser.add_argument(
    "-q", "--quiet",
    action="store_false", default=True,
    help="don't print status messages to stdout",
    #nargs='None'
)

args = parser.parse_args()

print(args.filename)
print(args.quiet)


#nargs=1
#nargs='?'
#nargs='+'
#nargs='*'

#action='store_const'
#action='store_true'
#action='store_false'
#action='append'
#action='append_const'
#action='version'
#action='extend'
