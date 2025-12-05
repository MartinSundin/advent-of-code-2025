from itertools import product

with open('input4.txt','r') as f:
    rolls = [s.strip() for s in f.readlines()]

num_rolls = 0
n,m = len(rolls), len(rolls[0])
for i in range(n):
    for j in range(m):
        if rolls[i][j] == '@':
            rolls_ij = 0
            for di,dj in product([1,-1,0],[1,-1,0]):
                if not (di == 0 and dj == 0):
                    i2, j2 = i+di, j+dj
                    if 0 <= i2 < n and 0 <= j2 < m and rolls[i2][j2] == '@':
                        rolls_ij += 1

            if rolls_ij < 4:
                num_rolls += 1

print(f"The number of rolls is {num_rolls}")