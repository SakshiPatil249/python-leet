# Complexity Analysis

## Sum Formula Solution

### Time Complexity

```text
O(n)
```

### Why?

Computing:

```python
sum(nums)
```

requires traversing all elements once.

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

Only a few variables are used:

```python
n
expected_sum
actual_sum
```

No additional arrays, sets, or dictionaries are created.

Memory usage remains constant.

---

# Complexity Summary

| Metric           | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(n)       |
| Space Complexity | O(1)       |

---

# Optimality

Every element must be inspected at least once.

Therefore:

```text
Best Possible Time Complexity = O(n)
```

Only constant extra memory is used.

```text
Best Possible Space Complexity = O(1)
```

Hence, this is an optimal solution.
