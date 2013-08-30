#!/usr/bin/python

import i3

nodes = i3.filter(nodes=[])
windows = list()
for i in nodes:
    print i['name'].replace(" ", "_")
