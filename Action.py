# usr/bin/env python
# -*- coding: UTF-8 -*-
from string import *
from Graph import *
from Edge import *
from Vertex import *
class Action:
	
	

	def __init__(self,txtpath):
		self.txtpath=txtpath
		self.max=65535
		self.graph=Graph()
		print(self.txtpath)

	def readEdgeFromTxt(self):
		edge_list=[]
		if self.txtpath:
			try:
				file=open(self.txtpath,"r")
				line=file.readline()
				print(line)
				s_list=line.split(",")
				for s in s_list:
					print(s)
					# print(len(s))
					if s:
						# print(s[0])
						s=s.strip()
						v_s=Vertex(-1,s[0])
						v_e=Vertex(-1,s[1])
						d=int(s[2])
						edge=Edge(v_s,v_e,d)
						edge_list.append(edge)

			except IOError:
				return None
			else:
				# print(edge_list)
				return edge_list


	def getVertexList(self,edge_list):
		v_list=[]
		for e in edge_list:
			v_list.append(e.v_s.value)
			v_list.append(e.v_e.value)
		v_list.sort()
		# print(list)
		num=len(v_list)
		k=1
		while k<num:
			# print(k)
			if v_list[k]==v_list[k-1]:
				del v_list[k]
			else:
				k=k+1
			num=len(v_list)
		return v_list


	def initGraph(self):
		max=65535
		self.graph.edge_list=self.readEdgeFromTxt()
		self.graph.v_list=self.getVertexList(self.graph.edge_list)
		self.graph.v_num=len(self.graph.v_list)
		self.graph.edge_num=len(self.graph.edge_list)
		num=self.graph.v_num
		print(num)
		self.graph.edges=[]
		for i in range(self.graph.v_num):
			col=[]
			for j in range(self.graph.v_num):				
				col.append(max)
			# print("col element")
			# print(col)
			self.graph.edges.append(col)
		print(self.graph.v_list)
		
		


	def initEdges(self):
		for e in self.graph.edge_list:
			index1=self.graph.v_list.index(e.v_s.value)
			index2=self.graph.v_list.index(e.v_e.value)
			# print(index1)
			# print(index2)
			# print(e.d)
			if index1>=0 and index2>=0:
				self.graph.edges[index1][index2]=e.d
		for row in self.graph.edges:
			print(row)
		

	def shortestDistance(self, v1, v2):
		index1=self.graph.v_list.index(v1)
		index2=self.graph.v_list.index(v2)
		if index1>=0 and index2>=0:
			N=self.graph.v_num
			collect=[]
			d=[]
			p=[]
			for i in range(N):
				collect.append(0)
				d.append(self.graph.edges[index1][i])
				p.append(0)
			print("d[]")
			print(d)
			print("collect[]")
			print(collect)
			p[index1]=-1
			for i in range(N):
				min=65535
				min_index=0
				for k in range(N):
					if collect[k]==0 and d[k]<min:
						min=d[k]
						min_index=k
				collect[min_index]=1
				if min_index==index2:
					break
				else:
					for j in range(N):
						if collect[k]==0 and d[min_index]+self.graph.edges[min_index][j]<d[j]:
							d[j]=d[min_index]+self.graph.edges[min_index][j]
							p[j]=min_index
			return d[index2]
		else:
			return -1




