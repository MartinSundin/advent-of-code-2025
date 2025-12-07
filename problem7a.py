with open('input7.txt', 'r') as f:
    diagram = [row.strip() for row in f.readlines()]

nsplits = 0
n = len(diagram[0])
beams = [False]*n
beams[diagram[0].index('S')] = True
for row in diagram[1:]:
    new_beams = [False]*n
    for i,(b,d) in enumerate(zip(beams, row)):
        if b:
            if d == '.':
                new_beams[i] = True
            elif d == '^':
                new_beams[i-1] = True
                new_beams[i+1] = True
                nsplits += 1
    beams = new_beams

print(f"The beam is split {nsplits} times.")