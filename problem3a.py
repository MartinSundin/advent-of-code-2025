with open('input3.txt','r') as f:
    batteries = [s.strip() for s in f.readlines()]

# Get the maximum power from each batterybank
total = 0
for row in batteries:
    nums = [int(b) for b in row]
    bmax = max(nums)
    i = nums.index(bmax)
    if i < len(nums)-1:
        bmax = bmax*10 + max(nums[i+1:])
    else:
        bmax = bmax + 10*max(nums[:i])
    total += bmax

print(f"The maximum sum is {total}")
