with open('input9.txt', 'r') as f:
    tiles = [row.strip() for row in f.readlines()]

heap = []
max_area = 0
for i,s1 in enumerate(tiles):
    x1,y1 = [int(c) for c in s1.split(",")]
    for s2 in tiles[i+1:]:
        x2,y2 = [int(c) for c in s2.split(",")]
        area = (abs(x2-x1)+1)*(abs(y2-y1)+1)
        if area > max_area:
            max_area = area

print(f"Max Area = {max_area}")