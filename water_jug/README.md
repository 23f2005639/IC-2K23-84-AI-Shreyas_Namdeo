# Water Jug

**Aim:** Measure a target amount in either jug using fill, empty, and pour operations. Supply and drain are unlimited; amounts are whole numbers.

```sh
python3 water_jug/main.py
```

Enter A = **4**, B = **3**, target = **2**:

```text
Step 0: Start | A = 0, B = 0
Step 1: Fill B | A = 0, B = 3
Step 2: Pour B -> A | A = 3, B = 0
Step 3: Fill B | A = 3, B = 3
Step 4: Pour B -> A | A = 4, B = 2
Answer: 2 in a jug. Total moves: 4
```

![Four-move solution, with jug amounts at each step](solution.svg)

## Algorithm

Breadth-first search (BFS) visits each state `(a, b)` once. Parent links recover the shortest sequence.

```mermaid
flowchart TD
    A[Read capacities and target] --> B{Valid input?}
    B -->|No| X[Print input error]
    B -->|Yes| C{Target reachable by GCD rule?}
    C -->|No| N[No solution]
    C -->|Yes| D[Queue empty-jug state]
    D --> E[Remove oldest state]
    E --> F{Either jug has target?}
    F -->|Yes| G[Follow parents and print numbered steps]
    F -->|No| H[Enqueue unseen fill, empty, and pour states]
    H --> E
```

For capacities $A,B>0$, a target $T\geq0$ is reachable iff

$$T\leq\max(A,B)\quad\text{and}\quad\gcd(A,B)\mid T.$$

Pour A → B: $p=\min(a,B-b)$, then $(a,b)\to(a-p,b+p)$.

**Performance:** At most $(A+1)(B+1)$ integer states; time and space $O(AB)$. BFS guarantees minimum moves because each action costs one move.

**Learning:** State modeling, visited sets, shortest paths, and parent-based path recovery.
