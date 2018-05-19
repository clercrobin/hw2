from random import shuffle
    
def union(components, ranks, u, v):
    u = find(components, u)
    v = find(components, v)
    if ranks[u] > ranks[v]:
        components[v] = u
    elif ranks[v] > ranks[u]:
        components[u] = v
    else:
        components[v] = u
        ranks[u] += 1

def find(components, u):
    v = u
    while components[v] != v:
        v = components[v]
    while components[u] != v:
        tmp = components[u]
        components[u] = v
        u = tmp
    return v

def karger():
    # Contract
    components = list(range(n))
    ranks = [1] * n
    shuffle(edges)
    nb_vertices = n
    for u, v in edges:
        if nb_vertices == 2:
            break
        u, v = find(components, u), find(components, v)
        if u != v:
            union(components, ranks, u, v)
            nb_vertices -= 1
    # Find cut
    cut = []
    for u in range(n):
        if find(components, u) == find(components, 0):
            cut.append(u)
    # Find weight of the cut
    size = 0
    for u, v in edges:
        if components[u] != components[v]:
            size += 1
    return size, tuple(cut)
    
n, m = map(int, input().split())
edges = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]

N = 100000
cuts = {}
min_size = 10**9
for _ in range(N):
    size, cut = karger()
    if size < min_size:
        cuts = {cut}
        min_size = size
    elif size == min_size:
        cuts.add(cut)
print(min_size, len(cuts))
