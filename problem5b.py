with open('input5.txt','r') as f:
    ranges = [s.strip() for s in f.readlines()]

i_split = ranges.index("")
ranges = [(int(r.split("-")[0]),int(r.split("-")[1])) for r in ranges[:i_split]]

# build non overlapping intervals
left_intervals = []
right_intervals = []
ranges.sort(key=lambda i:i[0])
amin,bmax = ranges[0]
for a,b in ranges:
    if bmax < a:
        left_intervals.append(amin)
        right_intervals.append(bmax)
        amin, bmax = a,b
    else:
        bmax = max(bmax, b)
        amin = min(amin, a)

left_intervals.append(amin)
right_intervals.append(bmax)

nfresh = 0
for a,b in zip(left_intervals, right_intervals):
    nfresh += b-a+1

print(f"{nfresh} fresh IDs")
