#!/usr/bin/python

import codecs

string=raw_input("Enter string: ")

decoded=string.decode('rot13')

print "The decoded string is: ", decoded