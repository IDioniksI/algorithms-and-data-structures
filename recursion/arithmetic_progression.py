def gen_prog(first, last, step):
    prog = []
    while first <= last:
        prog.append(first)
        first += step
    return prog


def progression(lst):
    if not lst:
        return 0
    else:
        rem_el = lst.pop(0)
        return rem_el + progression(lst)


prog1 = gen_prog(0, 10, 2)
prog2 = gen_prog(10, 50, 3)
print(f'The first progression: {prog1} \nThe sum of all elements of the progression {progression(prog1)}\n')
print(f'The second progression: {prog2} \nThe sum of all elements of the progression {progression(prog2)}')
