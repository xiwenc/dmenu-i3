#!/usr/bin/python

import i3
import sys

if len(sys.argv) is not 2:
    sys.stderr.write('Usage: %s windowname' % sys.argv[0])
    sys.exit(1)

nodes = i3.filter(nodes=[])
windows = list()

target = sys.argv[1]
selection = 0

for i in nodes:
    if target == i['name'].replace(" ", "_"):
        selection = i['window']
        break

if selection is not 0:
    i3.focus(id=selection)
