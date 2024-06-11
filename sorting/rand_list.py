from random import randint


def random_list(num_el):
    """A function that randomly generates a list"""
    numbers = []
    for i in range(num_el):
        numbers.append(randint(0, 500))
    return numbers
