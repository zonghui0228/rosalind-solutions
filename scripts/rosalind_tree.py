# completing a tree
# the minimum number of edges that can be added to the graph to produce a tree

def minimumtree(n, adlist):
	edges = []
	m = 0
	while len(adlist) > 0:
		edges.append(adlist[0])
		del adlist[0]
		for i in adlist:
			for j in i:
				if j in edges[m]:
					edges[m] += i
					adlist.remove(i)
					break
		m += 1
	
	edges = [set(edge) for edge in edges]
	c = 0
	for edge in edges:
		c += len(edge)

	# print edges
	return n - c + len(edges) - 1


if __name__ == '__main__':
	f = open('test.txt','r')
	n = int(f.readline())
	l = [line.strip().split(' ') for line in f.readlines()]
	f.close()
	print minimumtree(n, l)
