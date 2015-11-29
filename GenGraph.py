#!/usr/bin/python

from Node import Node
import random

def generateNodes(graphSize, totalNodes, k):
	nodeSet = list()
	n = 0
	while (n<totalNodes):
		nodeSet.append(randomNode(graphSize, k))
		n += 1
	return nodeSet

def randomNode(graphSize , k):
	x = random.randrange(0, graphSize+1)
	y = random.randrange(0, graphSize+1)
	kval = random.randrange(1, (10*k)+1)
	return Node(x, y, kval, dict())

def generateEdges1(nodeSet, maxWeight, k):
	outer = 0
	for n in nodeSet:
		inner = 0
		for m in nodeSet:
			if inner > outer and abs(n.kval - m.kval) <= k:
				weight = random.randrange(1,maxWeight+1)
				n.adjList[m] = weight
				m.adjList[n] = weight
			inner += 1
		outer += 1

def generateEdges2(nodeSet, k):
	outer = 0
	for n in nodeSet:
		inner = 0
		for m in nodeSet:
			if inner > outer and abs(n.kval - m.kval) <= k:
				weight = ((n.xloc - m.xloc)**2 + (n.yloc - m.yloc)**2)**.5
				n.adjList[m] = weight
				m.adjList[n] = weight
			inner += 1
		outer+=1

def generateTrees(nodeSet):
	nodes = list(nodeSet)
	trees = list()
	for n in reversed(nodeSet):
		if n in nodes:
			tree = runDFS({}, n)
			for m in tree:
				nodes.remove(m)
			trees.append(tree)
	return trees

def runDFS(tree, node):
	if node in tree:
		return dict()
	else:
		tree[node] = node.adjList
		newTree = dict()
		for n in node.adjList:
			newTree = merge_two_dicts(newTree, runDFS(tree, n))
		newTree[node] = node.adjList
		return newTree

def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z

def filterNodes(nodes):
	for n in reversed(nodes):
		if not n.adjList:
			nodes.remove(n)
	return nodes

def GenerateGraph(totalNodes, graphSize, maxWeight, kval, edgeMethod):
	nodes = generateNodes(graphSize, totalNodes, kval)
	if edgeMethod == 1:
		generateEdges2(nodes, kval)
	elif edgeMethod == 2:
		generateEdges1(nodes, maxWeight, kval)
	trees = generateTrees(filterNodes(nodes))
	return trees