#!/usr/bin/env python

# Copyright 2011 Peter Hajas. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice, this list of
#       conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright notice, this list
#       of conditions and the following disclaimer in the documentation and/or other materials
#       provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY PETER HAJAS ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PETER HAJAS OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are those of the
# authors and should not be interpreted as representing official policies, either expressed
# or implied, of Peter Hajas.


# Feeling lucky, for your bash history!
# Because we all like to feel lucky, and pressing "up arrow" is for squares

# chmod a+x this, and add it to your path. You're going to dig it.
# Run with lucky.py <cmd>

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
list = reversed([l for l in history.readlines() if l != ""])

# Find matching entries
matches = [entry for entry in list if search in entry]

if len(matches):
	print "Found it: {0}".format(matches[0])
	os.system(matches[0])
else:
	print "Didn't find what you were looking for, you weren't lucky :("