import time
from rand_list import random_list


def increment(seq, size):
    """The function counts the step according to Sedgwick's formula"""
    p1 = p2 = p3 = 1
    s = -1
    while True:
        s += 1
        if s % 2:
            seq[s] = 8 * p1 - 6 * p2 + 1
        else:
            seq[s] = 9 * p1 - 9 * p3 + 1
            p2 *= 2
            p3 *= 2
        p1 *= 2
        if 3 * seq[s] >= size:
            break
    return s if s > 0 else 0


def shell_sort(lst):
    """Shell sorting function"""
    start = time.time()
    m = c = 0
    seq = [0] * 40
    step = increment(seq, len(lst))
    while step >= 0:
        inc = seq[step]
        step -= 1
        for i in range(inc, len(lst)):
            j = i
            key = lst[j]
            while j >= inc and lst[j - inc] > key:
                c += 1
                lst[j] = lst[j - inc]
                m += 1
                j -= inc
            c += 1
            lst[j] = key
            m += 1
    end = (time.time() - start) * 1000
    return lst, m, c, end


counter = 0

for x in range(1):
    counter += 1
    lst1 = random_list(100)
    lst2 = random_list(1000)
    lst3 = random_list(10000)

    print(f'\nRandomly generated list №{counter}: {lst1}')
    fin_lst1, copy1, comp1, time1 = shell_sort(lst1)
    print(f'Sorted list: {fin_lst1}')
    print(f'Sorting required: \n{copy1} copies\n'
          f'{comp1} comparisons \n{round(time1, 3)} milliseconds')

    print(f'\nRandomly generated list №{counter}: {lst2}')
    fin_lst2, copy2, comp2, time2 = shell_sort(lst2)
    print(f'Sorted list: {fin_lst2}')
    print(f'Sorting required: \n{copy2} copies\n'
          f'{comp2} comparisons \n{round(time2, 3)} milliseconds')

    print(f'\nRandomly generated list №{counter}: {lst3}')
    fin_lst3, copy3, comp3, time3 = shell_sort(lst3)
    print(f'Sorted list: {fin_lst3}')
    print(f'Sorting required: \n{copy3} copies\n'
          f'{comp3} comparisons \n{round(time3, 3)} milliseconds')
