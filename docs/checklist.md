# Solution Checklist

When your head is deep in an algorithm you can easily trip-up on the basics. Especially if you don't have the luxury of an IDE, compiler or tests. Before giving the 👍, check:

## Silly Mistakes

### 1. Initialise variables before entering `while`

A simple one, but you can sometimes forget if you've been used to using `for`:

```python
i = 0
while i < len(s):
    blah(i)
    i += 1
```

### 2. Check array indices/length maths

* When converting from indices into a length, add 1 to the result.
* When computing a new index using a length, subtract 1 from the result.

**Indices are zero-indexed, but even a substring at index 0 has length 1.**

Examples:

```python
mid = (start + end) // 2    # index = (index + index) / 2    (no +1 or -1 needed)
length = end - start        # length = index - index + 1     (+1 needed)
end = start + (length - 1)  # index = index + (length - 1)   (-1 needed)
```

### 3. Have you actually returned the result?

Another simple one. Easy to miss out.

1. `return result`
2. Is it the right type? (e.g. don't return an array if it is expecting a string):
   `return ''.join(result)`

### 4. Check use of `+=` and `-=` etc

Easy to get the `+`/`-` and `=` muddled up!

```python
i += 2
i -= 2
```

### 5. Slices and bounds

In both these cases, `start` is inclusive, and `end` is exclusive.

```python
arr[start:end]
range(start, end)
```

### 6. Missing off the colon

Another basic one. Could be missing `:` from `if`, `for`, `while`, `else` etc.

### 7. Forgetting `len` or `range`

Wrong ❌

```python
s = "hello"
for i in range(s):
    blah(i)
for i in len(s):
    blah(i)
```

Right ✅

```python
s = "hello"
for i in range(len(s)):
    blah(i)
```

### 8. Operator precedence

All gravy until you accidentally write this:

```
mid = start + end // 2      ❌
mid = (start + end) // 2    ✅
```

Or this doozy:

```
arr = [0] * len(s)+1        ❌
arr = [0] * (len(s)+1)      ✅
```

### 9. Falsiness of `None` and `0`

Be careful relying on `None`'s falsiness if also matching `0` is not valid:

```python
x = None

while True:
    if not x:
        do_something()
        ...
    x = 0    # do_something() will run again!
```
