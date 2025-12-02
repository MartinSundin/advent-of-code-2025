with open('input2.txt', 'r') as f:
    productIds = f.readlines()[0].strip().split(",")

invalid_ids = []
for ids in productIds:
    num1,num2 = ids.split("-")
    for num in range(int(num1), int(num2)+1):
        num = str(num)
        if num[:len(num)//2] == num[len(num)//2:]:
            invalid_ids.append(int(num))

print(f"Total sum of invalid ids = {sum(invalid_ids)}")