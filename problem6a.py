with open('input6.txt','r') as f:
    problems = [s.strip().split(" ") for s in f.readlines()]
problems = [[c for c in row if c != ""] for row in problems]

total = 0
n = len(problems)
for i in range(len(problems[0])):
    problem_i = [problems[j][i] for j in range(n)]
    operation_i = problem_i.pop(-1)
    if operation_i == '+':
        total += sum(int(c) for c in problem_i)
    elif operation_i == '*':
        prod = 1
        for c in problem_i:
            prod *= int(c)
        total += prod
    else:
        raise Exception(f"Unknown operation {operation_i} in column {i}")
    
print(f"Total sum is {total}")