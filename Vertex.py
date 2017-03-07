#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class Vertex:
	index=-1
	value=None

	def __init__(self, i, v):
		self.index=i
		self.value=v

	def getIndex(self):
		return self.index

	def setIndex(self, i):
		self.index=i

	def setValue(self, value):
		self.value=value

	def getValue(self):
		return self.value
