with open('input2.txt', 'r') as f:
    productIds = f.readlines()[0].strip().split(",")

invalid_ids = []
for ids in productIds:
    num1,num2 = ids.split("-")
    for num in range(int(num1), int(num2)+1):
        num = str(num)
        l = len(num)
        k = 1
        while k < l:
            if l % k == 0 and num == num[:k]*(l//k):
                print(num, l, k)
                invalid_ids.append(int(num))
                k = len(num)
            else:
                k += 1

print(f"Total sum of invalid ids = {sum(invalid_ids)}")