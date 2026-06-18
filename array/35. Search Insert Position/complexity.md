# Complexity Analysis

## Binary Search Solution

### Time Complexity

```text
O(log n)
```

### Why?

Each iteration removes half of the search space.

Example:

```text
n
n/2
n/4
n/8
...
```

This continues until only one element remains.

Number of steps:

```text
log₂(n)
```

Therefore:

```text
O(log n)
```

---

## Space Complexity

```text
O(1)
```

### Why?

Only a few variables are used:

```python
left
right
mid
```

No extra arrays or data structures are created.

Memory usage remains constant.

Therefore:

```text
O(1)
```

---

# Complexity Summary

| Metric           | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(log n)   |
| Space Complexity | O(1)       |

---

# Why Is This Better Than Linear Search?

Linear Search:

```text
O(n)
```

Binary Search:

```text
O(log n)
```

Example:

```text
1,000,000 elements
```

Linear Search:

```text
1,000,000 checks
```

Binary Search:

```text
~20 checks
```

This huge improvement is why Binary Search is one of the most important interview topics.

---

# Pattern Summary

| Variable | Purpose               |
| -------- | --------------------- |
| left     | Start of search space |
| right    | End of search space   |
| mid      | Middle element        |

Binary Search works because the array is sorted, allowing us to eliminate half the remaining search space at every step.
