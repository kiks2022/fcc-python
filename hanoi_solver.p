def hanoi_solver(n):
    rods = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    moves = []

    def format_state():
        return ' '.join(str(rods[rod]) for rod in ['A', 'B', 'C'])

    def move(num_disks, source, target, auxiliary):
        if num_disks == 1:
            moves.append(format_state())
            rods[target].append(rods[source].pop())
        else:
            move(num_disks - 1, source, auxiliary, target)
            moves.append(format_state())
            rods[target].append(rods[source].pop())
            move(num_disks - 1, auxiliary, target, source)

    move(n, 'A', 'C', 'B')
    moves.append(format_state())
    return '\n'.join(moves)

# Test Hanoi Solver
print("--- 2 Disks ---")
print(hanoi_solver(2))

print("\n--- 3 Disks ---")
print(hanoi_solver(3))
