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

i1,j1 = None, None
while heap:
    nd,i,j = heapq.heappop(heap)
    if find(i) != find(j):
        union(i,j)
        i1,j1 = i,j


print(f"The last boxes to connect are {boxes[i1]} and {boxes[j1]}.")
print(f"Product of x-coordinates is {boxes[i1][0]*boxes[j1][0]}")
