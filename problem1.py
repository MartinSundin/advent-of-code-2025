from collections import defaultdict

with open('input1.txt', 'r') as f:
    sequence = [w.strip() for w in f.readlines()]

count = 0
n = 50
m = 100
for key in sequence:
    k = int(key[1:])
    if key.startswith("R"):
        n = (n + k) % m
    else:
        n = (n - k + m) % m

    if n == 0:
        count += 1

print(f"Zero occurs {count} times")