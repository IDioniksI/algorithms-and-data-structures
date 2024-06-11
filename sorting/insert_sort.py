import time
from rand_list import random_list


def insert_sort(lst):
    """Insert sort function"""
    start = time.time()
    m = c = 0
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            c += 1
            lst[j + 1] = lst[j]
            m += 1
            j -= 1
        c += 1
        lst[j + 1] = key
        m += 1
    end = (time.time() - start) * 1000
    return lst, m, c, end


counter = 0

for x in range(5):
    counter += 1
    lst1 = random_list(100)
    lst2 = random_list(1000)
    lst3 = random_list(10000)

    print(f'\nRandomly generated list №{counter}: {lst1}')
    fin_lst1, copy1, comp1, time1 = insert_sort(lst1)
    print(f'Sorted list: {fin_lst1}')
    print(f'Sorting required: \n{copy1} copies\n'
          f'{comp1} comparisons \n{round(time1, 3)} milliseconds')

    print(f'\nRandomly generated list №{counter}: {lst2}')
    fin_lst2, copy2, comp2, time2 = insert_sort(lst2)
    print(f'Sorted list: {fin_lst2}')
    print(f'Sorting required: \n{copy2} copies\n'
          f'{comp2} comparisons \n{round(time2, 3)} milliseconds')

    print(f'\nRandomly generated list №{counter}: {lst3}')
    fin_lst3, copy3, comp3, time3 = insert_sort(lst3)
    print(f'Sorted list: {fin_lst3}')
    print(f'Sorting required: \n{copy3} copies\n'
          f'{comp3} comparisons \n{round(time3, 3)} milliseconds')
