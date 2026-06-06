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
            # Record state before move
            moves.append(format_state())
            # Move disk
            rods[target].append(rods[source].pop())
        else:
            # Move n-1 disks from source to auxiliary
            move(num_disks - 1, source, auxiliary, target)
            # Move the largest disk from source to target
            moves.append(format_state())
            rods[target].append(rods[source].pop())
            # Move n-1 disks from auxiliary to target
            move(num_disks - 1, auxiliary, target, source)

    move(n, 'A', 'C', 'B')

    # Append the final state
    moves.append(format_state())

    return '\n'.join(moves)
