from functools import lru_cache

with open('input7.txt', 'r') as f:
    diagram = [row.strip() for row in f.readlines()]

# recursive counting with cache
@lru_cache
def _inner(beam_index, diagram_index):
    if diagram_index >= len(diagram):
        return 1
    else:
        if diagram[diagram_index][beam_index] == '.':
            return _inner(beam_index, diagram_index+1)
        elif diagram[diagram_index][beam_index] == '^':
            return _inner(beam_index+1, diagram_index+1) + _inner(beam_index-1, diagram_index+1)

beam_index = diagram[0].index('S')
nsplits = _inner(beam_index, 1)

print(f"In the quantum case, the beam is split {nsplits} times.")