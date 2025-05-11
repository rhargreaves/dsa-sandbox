# Backtracking

Backtracking is a systematic way to explore all possible solutions to a problem by making a series of choices and undoing them when they don't lead to a solution.

[The Backtracking Blueprint: The Legendary 3 Keys To Backtracking Algorithms](https://www.youtube.com/watch?v=Zq4upTEaQyM)

## The Three Key Elements

### 1. Choice
At each step, we make a decision that affects our current state. For example:
- In subset generation: include or exclude an element
- In N-Queens: place a queen in a specific position
- In Sudoku: place a number in a cell

### 2. Constraints
These are the rules that determine if a choice is valid:
- In subset generation: no constraints (all choices are valid)
- In N-Queens: queens cannot attack each other
- In Sudoku: numbers cannot repeat in row/column/box

### 3. Goal
The condition that tells us we've found a solution:
- In subset generation: we've made decisions for all elements
- In N-Queens: all queens are placed safely
- In Sudoku: all cells are filled correctly

## Example: Subset Generation
```python
def generate_subsets(nums):
    result = []

    def backtrack(index, current_subset):
        # Goal: We've made decisions for all elements
        if index == len(nums):
            result.append(current_subset.copy())
            return

        # Choice 1: Include nums[index]
        current_subset.append(nums[index])
        backtrack(index + 1, current_subset)
        current_subset.pop()  # Backtrack

        # Choice 2: Skip nums[index]
        backtrack(index + 1, current_subset)

    backtrack(0, [])
    return result
```

## Key Points
1. Backtracking is about exploring all possibilities systematically
2. We make choices, check constraints, and work toward a goal
3. When a path doesn't work, we backtrack and try alternatives

The pattern is:
 - Make a choice
 - Explore further with that choice
 - Undo the choice (backtrack)
 - Try other choices
