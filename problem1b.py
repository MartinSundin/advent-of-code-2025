count = 0
n = 50
m = 100
with open('input1.txt', 'r') as f:
    for w in f.readlines():
        key = w.strip()
        k = int(key[1:])
        if key.startswith("L"):
            n += k
            count += n//m
            n = n % m
        else:
            if n == 0:
                count -= 1

            n -= k
            count -= n//m
            n = n % m
            if n == 0:
                count += 1

print(f"Zero is crossed {count} times")
