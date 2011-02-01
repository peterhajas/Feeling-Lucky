Feeling Lucky
=============
I'm Feeling Lucky for your bash history
---------------------------------------

by Peter Hajas
--------------

Feeling Lucky is a simple project to let you do a reverse "I'm feeling lucky" search on your bash history. It'll search for the most recently used command of yours that included the search term, and run it.

Pressing the up arrow is for squares.

To use, simply chmod a+x the script, add it to your path (you'll want to, it's handy!) and use:

lucky.py <cmdname>
	
For example:

phajas$ lucky.py ssh
Found it!
Linux Chronos 2.6.32-22-generic-pae #36-Ubuntu SMP Thu Jun 3 23:14:23 UTC 2010 i686 GNU/Linux
Ubuntu 10.04.1 LTS
phajas@Chronos:~$

Pretty awesome, right?

Things Feeling Lucky should NOT be used for:

rm
git
dd
mv

and more! Be careful! Being lucky can be dangerous!

This is 2-clause BSD licensed. More details in lucky.py. Have fun, be careful, and don't count on luck too much.