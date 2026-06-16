# Complexity Analysis

## Time Complexity

```text
O(m + n)
```

### Why?

Each element from nums1 and nums2 is processed at most once.

Pointers:

```python
m
n
```

only move left.

Therefore:

```text
Total Operations = m + n
```

Hence:

```text
O(m + n)
```

---

## Space Complexity

```text
O(1)
```

### Why?

The algorithm only uses three variables:

```python
p
m
n
```

No additional arrays, lists, dictionaries, or sets are created.

Memory usage remains constant regardless of input size.

Hence:

```text
O(1)
```

---

# Complexity Summary

| Metric           | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(m + n)   |
| Space Complexity | O(1)       |

---

# Optimality

To merge two arrays, every element must be inspected at least once.

Therefore:

```text
Best Possible Time Complexity = O(m + n)
```

Since only pointers are used:

```text
Best Possible Space Complexity = O(1)
```

This makes the solution optimal.
