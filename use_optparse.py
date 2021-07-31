#!/usr/bin/env python

#https://docs.python.org/ja/3/library/optparse.html
#Deprecated since version 3.2

from optparse import OptionParser

parser = OptionParser()

parser.add_option(
    '-f', '--file', dest='filename', metavar='FILE',
    action='store', 
    help="write report to FILE"
)

parser.add_option(
    "-q", "--quiet",
    action="store_false", default=True,
    help="don't print status messages to stdout"
)

(options, args) = parser.parse_args()


print(options.filename)
print(options.quiet)
