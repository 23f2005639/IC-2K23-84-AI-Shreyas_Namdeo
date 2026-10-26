from collections import deque


def solve(missionaries, cannibals, capacity):
    if missionaries < 0 or cannibals < 0 or missionaries + cannibals == 0 or capacity < 1:
        raise ValueError("Populations must be nonnegative, with at least one person; capacity must be positive.")

    def safe(m, c):
        right_m, right_c = missionaries - m, cannibals - c
        return (0 <= m <= missionaries and 0 <= c <= cannibals
                and (m == 0 or m >= c) and (right_m == 0 or right_m >= right_c))

    if not safe(missionaries, cannibals):
        raise ValueError("The starting bank is unsafe: cannibals outnumber missionaries.")

    # State holds the left-bank counts and whether the boat is on the left.
    start = (missionaries, cannibals, True)
    queue = deque([start])
    parents = {start: None}
    loads = [(m, c) for m in range(min(missionaries, capacity) + 1)
             for c in range(min(cannibals, capacity - m) + 1) if m + c > 0]
    while queue:
        state = queue.popleft()
        m, c, left = state
        if m == c == 0:
            path = []
            while state != start:
                previous, load = parents[state]
                path.append((state, load))
                state = previous
            return [(start, (0, 0))] + path[::-1]
        direction = -1 if left else 1
        for boat_m, boat_c in loads:
            next_m, next_c = m + direction * boat_m, c + direction * boat_c
            next_state = (next_m, next_c, not left)
            if safe(next_m, next_c) and next_state not in parents:
                parents[next_state] = (state, (boat_m, boat_c))
                queue.append(next_state)
    return None


def main():
    try:
        missionaries = int(input("Missionaries [3]: ") or "3")
        cannibals = int(input("Cannibals [3]: ") or "3")
        capacity = int(input("Boat capacity [2]: ") or "2")
        path = solve(missionaries, cannibals, capacity)
    except (ValueError, EOFError) as error:
        print(f"Invalid input: {error}")
        return
    if path is None:
        print("No solution.")
        return
    for step, ((m, c, left), (boat_m, boat_c)) in enumerate(path):
        action = "Start" if step == 0 else f"{boat_m}M + {boat_c}C {'R -> L' if left else 'L -> R'}"
        print(f"Step {step}: {action} | Left: {m}M {c}C | "
              f"Right: {missionaries - m}M {cannibals - c}C | Boat: {'L' if left else 'R'}")
    print(f"Total crossings: {len(path) - 1}")


if __name__ == "__main__":
    main()
