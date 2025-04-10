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

# Algorithm notes

## Dijkstra's shortest-path algorithm

* V = number of vertices, E = number of edges
* Time complexity = (binary heap) *O((E + V) log V)*
* Soace complexity = (binary heap) *O(V)

It is a greedy algorithm, meaning it makes the best choice available at each step.

Dijkstra is neither depth-first search nor breadth-first. It is **least-cost-first**.

## Trie trees

* A state machine where each node is a state, and the edges represent the transitions based on input characters. This model aligns naturally with the concept of prefixes in strings.

## Running medians using 2 heaps

Given:
```
[ max_heap ] [ min_heap ]
```

1. Insert into *max_heap*:
```
[ X        ] [          ]
```

2. Immediately pop from *max_heap* and insert into *min_heap*:
```
[          ] [ X        ]
```

3. If *min_heap* has more elements, pop from *min_heap* and insert into *max_heap*:
e.g.
```
[ X X      ] [ X X X    ]
[ X X X    ] [ X X      ]
```

4. Median is largest of *max_heap* (if *max_heap* bigger)
OR average of largest of *max_heap* and smallest of *min_heap* (if heaps are equal size)

# Python notes

## Debug Print

Helper for when you need to log vars to **stderr** in a hurry...

```python
def debug(context='', **kwargs):
    print((context + ": " if context else '') +
          ' '.join(f"{k}={v}" for k, v in kwargs.items()), file=sys.stderr)

a = 0
b = 1
debug(a=a,b=b)
# a=0 b=1
debug("done something", a=a)
# done something: a=0
```

## Recursion

Some exercises can throw a runtime error for deep recurvise calls.
Use `sys.setrecursionlimit(x)` to increase the limit to some *x* (e.g. 15000).

## Memory Management

* Uses **reference counting** to automatically deallocate objects when they are out-of-scope. This happens immediately, outside of the GC.
* Can use `del` to decrement count (removes a binding between a name and an object):

```py
a = 1  # ref count = 1
b = a  # 2
del b  # 1
del a  # 0
```

### Garbage Collector

* Uses a **cyclic garbage collector** (to deal with objects which reference each other in a **cyclic** manner).
* Three generations (`gen0`, `gen1`, `gen2`). Objects start in `gen0`.
* Runs automatically periodically (or manually using `gc.collect()`)

### CPython: Memory Arenas, Pools & Blocks

* `pymalloc` is Python's private allocator (i.e. internal allocation, not with OS & `malloc`) for small objects < 512 bytes.
* It allocates memory in 256 KB blocks (**arenas**).
* A **pool** is a 4 KB subdivision of an arena, holding blocks of the same size class.
* A **block** is a chunk of memory in a pool.
* Aims to reduce fragmentation and OS memory allocation calls.

### Sorting

`sorted()` time is *O(n * log n)*, space is *O(n)* (Tim sort)




### Resources

* [Explanation with insight into how to return the route taken](https://www.youtube.com/watch?v=EFg3u_E6eHU)
* [Basic explanation](https://www.youtube.com/watch?v=gdmfOwyQlcI)
