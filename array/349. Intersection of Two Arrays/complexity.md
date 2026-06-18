# Complexity Analysis

## Hash Set Solution

### Time Complexity

Creating sets:

```python
set(nums1)
```

takes:

```text
O(n)
```

Creating:

```python
set(nums2)
```

takes:

```text
O(m)
```

Finding intersection:

```python
set1 & set2
```

takes:

```text
O(min(n, m))
```

Overall:

```text
O(n + m)
```

---

## Space Complexity

Two sets are created:

```python
set1
set2
```

In the worst case:

```text
set1 stores n elements
set2 stores m elements
```

Therefore:

```text
O(n + m)
```

---

# Complexity Summary

| Metric | Complexity |
|----------|------------|
| Time Complexity | O(n + m) |
| Space Complexity | O(n + m) |

---

# Optimality Analysis

Without sorting, every element must be inspected at least once.

Therefore:

```text
Minimum Possible Time Complexity ≈ O(n + m)
```

The Hash Set approach achieves this efficiently.

---

# Pattern Summary

| Data Structure | Purpose |
|---------------|----------|
| Set | Store unique elements |
| Set Intersection (&) | Find common elements |
| Hashing | Fast lookups |

This problem is a classic example of using Hash Sets to reduce a potentially O(n²) solution to O(n + m).
