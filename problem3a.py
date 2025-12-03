import heapq

with open('input3.txt','r') as f:
    batteries = [s.strip() for s in f.readlines()]

# batteries = '987654321111111,811111111111119,234234234234278,818181911112111'.split(",")

# Get the maximum power from each battery
total = 0
for row in batteries:
    nums = [int(b) for b in row]
    bmax = max(nums)
    i = nums.index(bmax)
    if i < len(nums)-1:
        bmax = bmax*10 + max(nums[i+1:])
    else:
        bmax = bmax + 10*max(nums[:i])

    # print(row, bmax)
    total += bmax

print(f"The maximum sum is {total}")
