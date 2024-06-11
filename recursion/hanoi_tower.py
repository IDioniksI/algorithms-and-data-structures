def tower(n, first, second, third, first_name='A', second_name='B', third_name='C'):
    if n > 0:
        tower(n - 1, first, third, second, first_name, third_name, second_name)
        second.append(first.pop())
        print(f"Step {tower.counter}: Move disk {n} from the {first_name} rod to the {second_name} rod")
        print(f"Tower condition: \n{print_tower_state(rods)}")
        tower.counter += 1
        tower(n - 1, third, second, first, third_name, second_name, first_name)


def print_tower_state(rods):
    rod_names = {1: 'A', 2: 'C', 3: 'B'}
    state_str = ""
    for i, rod in enumerate(rods):
        rod_name = rod_names.get(i + 1, str(i + 1))
        state_str += f"Rod {rod_name}: {len(rod)}\n"
    return state_str


num_discs = 4

rod1 = list(range(num_discs, 0, -1))
rod2 = []
rod3 = []
rods = [rod1, rod2, rod3]

print(f"\nInitial state of the tower: \n{print_tower_state(rods)}")

tower.counter = 1

tower(num_discs, rod1, rod3, rod2)
print(f"It took {tower.counter - 1} steps for everything")
