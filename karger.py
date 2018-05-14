import random
import copy
import fileinput

class Edge:
	def __init__(self, source, destination):
	    self.src = source
	    self.dest = destination

	def __str__(self):
		return "Source : {} Destination : {}".format(str(self.src), str(self.dest))

class Graph:

	def __init__(self, V, E, edges):
	    self.V = V
	    self.E = E
	    self.edges = edges

class Subset:
	def __init__(self, parent, rank):
		self.parent = parent
		self.rank = rank
	def __str__(self):
		return "Parent : {} Rank : {}".format(str(self.parent), str(self.rank))


def find(subsets, i):
	if (subsets[i].parent != i):
		subsets[i].parent = find(subsets, subsets[i].parent)
	return subsets[i].parent

def union(subsets, x, y):
	rootX = find(subsets, x)
	rootY = find(subsets, y)

	if (subsets[rootX].rank < subsets[rootY].rank):
		subsets[rootX].parent = rootY
	elif (subsets[rootX].rank > subsets[rootY].rank):
		subsets[rootY].parent = rootX
	else:
		subsets[rootY].parent = rootX;
		subsets[rootX].rank+=1


def karger(n, m, original):
	edges = original
	graph = Graph(n, m, edges)
	V = n
	E = m
	subsets = []
	for v in range(V):
		subset = Subset(v, 0)
		subsets.append(subset)
	nb_vertices = V

	# print("\n".join(map(str, subsets)))

	while (nb_vertices >2):
		
		random_edge = random.randrange(0, E)
		# print("Considered edge : {}".format(str(random_edge)))
		subset_src = find(subsets, edges[random_edge].src)
		subset_dest = find(subsets, edges[random_edge].dest)
		# print("subset_src : {}".format(str(subset_src)))
		# print("subset_dest : {}".format(str(subset_dest)))

		if (subset_src!=subset_dest):
			# print("contract edge : " +str(edges[random_edge].src)+ " " + str(edges[random_edge].dest))
			nb_vertices -=1
			union(subsets, subset_src, subset_dest)
		# print("\n".join(map(str, subsets)))

	cut_edges = 0
	cut_edges_list = []
	# print("Analysis after")
	for i in range(E):
		# print("Considered edge : {}".format(str(edges[i])))

		subset_src = find(subsets, edges[i].src)
		subset_dest = find(subsets, edges[i].dest)
		# print("subset_src : {}".format(str(subset_src)))
		# print("subset_dest : {}".format(str(subset_dest)))
		if (subset_src != subset_dest):
			cut_edges+=1
			cut_edges_list.append(i)

	return cut_edges, cut_edges_list



# f = open('input.txt', 'r')
line_nb=0

# n, m = map(int, input().rstrip().split())


# edges = []

# for _ in range(m):
# 	edges.append(list(map(int, input().rstrip().split())))

number_repetitions = 3000
min_so_far = 99999
differents = []

edges = []
for line in fileinput.input():
	if line_nb == 0:
		n, m = map(int, line.rstrip().split())
	else:
		src, dest = map(int, line.rstrip().split())
		src, dest = src-1, dest-1
		edges.append(Edge(src,dest))
	line_nb +=1
random.seed()



for i in range(number_repetitions):
	cut_edges, cut_edges_list = karger(n,m,edges)
	# print(cut_edges_list)
	if cut_edges<min_so_far:
		min_so_far = cut_edges
		differents = [cut_edges_list]
	elif cut_edges == min_so_far:
		if not(cut_edges_list in differents):
			differents.append(cut_edges_list)


print(str(min_so_far)+" "+ str(len(differents)))