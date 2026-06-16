# Complexity Analysis

## Optimized Two Pointer Solution

### Time Complexity

```text
O(n)
```

### Why?

The array is traversed exactly once.

```python
for read in range(1, len(nums)):
```

For an array of size `n`:

* Each element is visited once.
* Each comparison takes O(1).
* Each assignment takes O(1).

Therefore:

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

### Why?

Only two variables are used:

```python
read
write
```

No additional data structures are created.

Memory usage does not grow with input size.

Therefore:

```text
O(1)
```

---

# Complexity Summary

| Metric           | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(1)       |

---

# Optimality Analysis

Every element must be checked at least once to determine whether it is a duplicate.

Therefore:

```text
Minimum Possible Time Complexity = O(n)
```

The solution also uses constant extra memory.

```text
Minimum Possible Space Complexity = O(1)
```

Hence, this is the optimal solution for the problem.

---

# Pattern Summary

| Pointer       | Purpose                    |
| ------------- | -------------------------- |
| Read Pointer  | Scans every element        |
| Write Pointer | Stores next unique element |

This Read + Write Pointer pattern is one of the most common interview patterns for array manipulation problems.
