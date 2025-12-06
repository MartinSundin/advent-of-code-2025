with open('input6.txt','r') as f:
    problems = [s.replace("\n","") for s in f.readlines()]

problems = [[c for c in row] for row in problems]

total = 0
n = len(problems[0])
# get one problem at the time
operator_row = problems.pop(-1)
while len(operator_row) > 0:
    operator_i = operator_row.pop(0)
    problem_i = [[row.pop(0)] for row in problems]
    while operator_row and operator_row[0] == ' ':
        operator_row.pop(0)
        for row,prow in zip(problems, problem_i):
            prow.append(row.pop(0))

    # rotate the problem
    rotated_problem = [[problem_i[i][j] for i in range(len(problem_i))] for j in range(len(problem_i[0]))]
    rotated_problem = ["".join(c for c in row if c != ' ') for row in rotated_problem]
    rotated_problem = [int(c) for c in rotated_problem if c != ""]

    if operator_i == '+':
        total += sum(rotated_problem)
    else:
        prod = 1
        for p in rotated_problem:
            prod *= p
        total += prod

print(f"Total sum is {total}")
