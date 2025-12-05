with open('input5.txt','r') as f:
    ranges = [s.strip() for s in f.readlines()]

i_split = ranges.index("")
queries = [int(r) for r in ranges[i_split+1:]]
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
for q in queries:
    # binary search
    left = 0
    right = len(right_intervals) - 1
    while left < right:
        mid = (left+right)//2
        if left_intervals[mid] <= q <= right_intervals[mid]:
            left, right = mid, mid
        elif q < left_intervals[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if left == right and left_intervals[left] <= q <= right_intervals[right]:
        nfresh += 1

print(f"{nfresh} fresh IDs")
