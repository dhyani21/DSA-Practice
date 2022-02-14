Dynamic Programming with Optimality Criterion:

It's natural to attempt dynamic programming, as we encounter similar subproblems. Our state is (K, N): K eggs and N floors left. When we drop an egg from floor X, it either survives and we have state (K, N-X), or it breaks and we have state (K-1, X-1).

Complexity Analysis:
  Time Complexity: O(K * N)O(K∗N).
  Space Complexity: O(N)O(N).
