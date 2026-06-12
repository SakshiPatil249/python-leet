# Complexity Analysis

## Optimized Solution

### Time Complexity

```text
O(n)
```

### Explanation

The algorithm traverses the array exactly once.

```python
for read in range(len(nums)):
```

If the array contains `n` elements:

* Each element is visited once.
* Each comparison takes constant time.
* Each assignment takes constant time.

Therefore:

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

### Explanation

The algorithm only uses one additional variable:

```python
write
```

No extra arrays, lists, dictionaries, or sets are created.

Regardless of input size, memory usage remains constant.

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

# Why This Is Optimal

To determine whether an element should be removed, every element must be examined at least once.

Therefore:

```text
Best Possible Time Complexity = O(n)
```

The solution also uses constant extra space:

```text
Best Possible Space Complexity = O(1)
```

Hence, this is the optimal solution for the problem.
