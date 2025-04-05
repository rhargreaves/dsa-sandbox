# Data Structures & Algorithms Sandbox

## Requirements

* Python 3.13+

## Build

```sh
make deps
```

## Tests

```sh
make test
```

## Python notes

* `sorted()` time is *O(n * log n)*, space is *O(n)* (Tim sort)

## Dijkstra's shortest-path algorithm

V = number of vertices, E = number of edges
Time complexity = (binary heap) *O((E + V) log V)*
Soace complexity = (binary heap) *O(V)

It is a greedy algorithm, meaning it makes the best choice available at each step.

Dijkstra is neither depth-first search nor breadth-first. It is **least-cost-first**.

### Resources

* [Explanation with insight into how to return the route taken](https://www.youtube.com/watch?v=EFg3u_E6eHU)
* [Basic explanation](https://www.youtube.com/watch?v=gdmfOwyQlcI)
