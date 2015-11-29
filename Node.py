#!/usr/bin/python

class Node(object):

	def __init__(self, xloc, yloc, kval, adjList):
		self.xloc = xloc
		self.yloc = yloc
		self.kval = kval
		self.adjList = adjList

	def __eq__(self, rhs):
		return self.xloc == rhs.xloc and self.yloc == rhs.yloc and self.kval == rhs.kval