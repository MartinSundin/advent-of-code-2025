from collections import defaultdict
import heapq

with open('input8.txt', 'r') as f:
    boxes = [s.strip() for s in f.readlines()]

boxes = [[int(c) for c in row.split(",")] for row in boxes]

heap = []
for i,(x1,y1,z1) in enumerate(boxes):
    for j,(x2,y2,z2) in enumerate(boxes[i+1:], start=i+1):
        d = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
        heapq.heappush(heap, (d,i,j))
        
# union find
parent = list(range(len(boxes)+1))

def find(a):
    while a != parent[a]:
        a = parent[a]
    return a

def union(a,b):
    pa, pb = find(a), find(b)
    if pa != pb:
        parent[pa] = pb

nconnections = 1000 # 1_000 # 10
connected = 0
while heap and connected < nconnections:
    # print(f"{connected} connections")
    nd,i,j = heapq.heappop(heap)
    if find(i) != find(j):
        union(i,j)
    connected += 1

group_counts = defaultdict(int)
for i in range(len(boxes)):
    group_counts[find(i)] += 1

group_counts = [-n for n in group_counts.values()]
group_counts.sort()
total = 1
print(group_counts[:5])
for nn in group_counts[:3]:
    total *= -nn

print(f"Total product = {total}")