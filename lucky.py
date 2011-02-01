#!/usr/bin/env python

# Feeling lucky, for your bash history!
# Because we all like to feel lucky, and pressing "up arrow" is for squares

# This currently only works in bash

import os, sys

if len(sys.argv) != 2:
	print "You need to provide a search term!"
	if len(sys.argv) > 2:
		print "And just one, you eager beaver..."
	quit()

search = sys.argv[1]

# Open history file
historyPath = os.environ['HOME'] + "/.bash_history"

history = open(historyPath)

# Read into a list
list = []

while 1:
	string = history.readline()
	if string == "":
		break
	list.append(string)

list.reverse()

for entry in list:
	if search in entry:
		print "Found it!"
		os.system(entry)
		quit()
		
print "Didn't find what you were looking for, you weren't lucky :("