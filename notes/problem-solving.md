# Problem Solving for Programming

## Common Logic Building Blocks

A nonexhaustive list of common building blocks:
- Monotonic stack
- Rabin-Karp
- Topological sort
- Dijkstra's algorithm
- BFS and DFS
- Longest increasing subsequence (O(n log n))
- Multipointer iteration and traversal
- Floyd-Warshall
- Tries, linked lists, hash tables, sets, heaps, deques, BSTs, balanced trees, etc
- RadixSort
- Binary search for answer validation
- Algorithms and data structures over abstractions (e.g., split array largest sum, bus routes)
- Decomposing compound types (e.g., n intervals into 2 * n points)
- Aggregating types (e.g., 2 * n points into n intervals)
- Modulus tricks
- Combinatorial identities (e.g., hockey stick identity, Pascal's identity)

## Exploratory Practice Method

1. Solve the problem.
2. If step 1 succeeds, you are done. Otherwise, troubleshoot (see below).
3. Once you solve the problem, study and understand the best solutions for it.
4. If it's an important question, relate it to other questions, extend the solution, and memorize the solution structure.


### Troubleshooting

1. Do you understand the problem?

   - Restate the problem and the structure of the optimal solution, and note important edge cases.

2. Does it fit into any of the algorithm design paradigms?

   1. Does it involve combining *non-overlapping* subproblems? Try divide and conquer.
   2. Does it involve optimization over *overlapping* subproblems? Try dynamic programming.
   3. Does it involve satisfying complicated constraints? Try backtracking.
   4. Does it involve optimization over bounded and prunable subproblems? Try branch and bound.
   5. Does it involve graphs? Try well-known graph algorithms.
   6. If it fits into none of the above, try relating it to well-known algorithms and data structures.

3. Do any heuristics help?

   - Is there a direct, imperative-esque solution?
   - Is there an analogous problem?
   - Is the problem easier in a more general form?
   - Is it easier to iteratively refine a brute-force solution?
   - Is it easier to work backward from the optimal solution?
   - Is it better to use *less* raw information and greater abstraction?
   - Is it better to use *more* raw information and less abstraction?

4. If all else fails, try sketching out the entire solution, using imagination to fill out the unknown parts. For example,

   - Hypothesize an unknown data structure whose existence would help greatly, and then find (or code) it.
   - Hypothesize an unknown piece of information whose existence would help greatly, and then try to derive it.
   - Failing the above, rinse and repeat with a different heuristic.
