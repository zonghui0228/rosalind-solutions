# find an Eulerian cycle in a graph.
def EulerianCycle(graph):
	Cycle = []
	while len(graph) > 0:
		cycle = []
		cycle.append(graph[0][0])
		cycle.append(graph[0][1])
	# print cycle
		del graph[0]
		# print graph
		for i in graph:
			if cycle[-1] == i[0]:
				cycle.append(i[1])
				graph.remove(i)
				print cycle
				continue
				# print graph
		Cycle.append(cycle)
	print Cycle

if __name__ == '__main__':
	f = open('test.txt', 'r')
	g = []
	for line in f.readlines():
		line = line.strip()
		if ',' not in line:
			g.append(line.split(' -> '))
		else:
			l = line.split(' -> ')
			for i in l[1].split(','):
				g.append([l[0], i])
	f.close()
	print g
	EulerianCycle(g)