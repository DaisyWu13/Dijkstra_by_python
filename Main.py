#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from string import *
from Action import *

txtpath="data"
action=Action(txtpath)
action.initGraph()
action.initEdges()
d=action.shortestDistance("A","C")
print(d)