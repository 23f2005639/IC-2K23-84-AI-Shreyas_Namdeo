from collections import deque
from math import gcd


def solve(capacity_a, capacity_b, target):
    if capacity_a <= 0 or capacity_b <= 0 or target < 0:
        raise ValueError("Capacities must be positive and target must be nonnegative.")
    if target > max(capacity_a, capacity_b) or target % gcd(capacity_a, capacity_b):
        return None

    start = (0, 0)
    queue = deque([start])
    parents = {start: None}
    while queue:
        state = queue.popleft()
        a, b = state
        if target in state:
            path = []
            while state != start:
                previous, action = parents[state]
                path.append((state, action))
                state = previous
            return [(start, "Start")] + path[::-1]

        to_b = min(a, capacity_b - b)
        to_a = min(b, capacity_a - a)
        moves = [
            ((capacity_a, b), "Fill A"),
            ((a, capacity_b), "Fill B"),
            ((0, b), "Empty A"),
            ((a, 0), "Empty B"),
            ((a - to_b, b + to_b), "Pour A -> B"),
            ((a + to_a, b - to_a), "Pour B -> A"),
        ]
        for next_state, action in moves:
            if next_state not in parents:
                parents[next_state] = (state, action)
                queue.append(next_state)
    return None


def main():
    try:
        a = int(input("Jug A capacity: "))
        b = int(input("Jug B capacity: "))
        target = int(input("Target amount in either jug: "))
        path = solve(a, b, target)
    except (ValueError, EOFError) as error:
        print(f"Invalid input: {error}")
        return
    if path is None:
        print("No solution.")
        return
    for step, ((a, b), action) in enumerate(path):
        print(f"Step {step}: {action} | A = {a}, B = {b}")
    print(f"Answer: {target} in a jug. Total moves: {len(path) - 1}")


if __name__ == "__main__":
    main()
