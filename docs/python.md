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

Some exercises can throw a runtime error for deep recursive calls.
Use `sys.setrecursionlimit(x)` to increase the limit to some *x* (e.g. 15000).

## Multi-dimensional Array Init

A common gotcha is initialising 2D arrays like `arr = [[None] * 10] * 5`.
This only creates an outer array with 5 references to a SINGLE inner array with 10 `None`s.
Solve this by using generators:

```python
arr = [[None] * 10 for i in range(5)]
```

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



