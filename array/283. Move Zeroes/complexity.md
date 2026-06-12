# Complexity Analysis

## Optimized Two Pointer Solution

### Time Complexity

```text
O(n)
```

### Why?

The array is traversed exactly once.

```python
for read in range(len(nums)):
```

For an array of size `n`:

* Each element is visited once.
* Each swap operation takes O(1).
* Each comparison takes O(1).

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

The algorithm uses only:

```python
write
read
```

No additional arrays, lists, dictionaries, sets, or queues are created.

Memory usage remains constant regardless of input size.

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

To determine where every non-zero element belongs, we must inspect each element at least once.

Therefore:

```text
Minimum Possible Time Complexity = O(n)
```

The solution also uses constant extra memory.

```text
Minimum Possible Space Complexity = O(1)
```

Hence, this is the optimal solution for the problem.
