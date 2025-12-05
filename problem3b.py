with open('input3.txt','r') as f:
    batteries = [s.strip() for s in f.readlines()]

# Get the maximum power from each batterybank
total = 0
for row in batteries:
    # traverse list backwards, keeping only the 12 largest numbers
    result = ""
    for c in reversed(row):
        if len(result) < 12:
            new_num = c + result
        else:
            i = result.index(min(result))
            new_num = max(c + result[:i] + result[i+1:] for i in range(12))
        if result == '' or int(new_num) >= int(result):
            result = new_num
    total += int("".join([str(c) for c in result]))

print(f"The maximum sum is {total}")