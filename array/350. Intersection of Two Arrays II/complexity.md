# Complexity Analysis

## HashMap Frequency Solution

### Time Complexity

Building frequency map:

```python
for num in nums1
```

takes:

```text
O(n)
```

Traversing nums2:

```python
for num in nums2
```

takes:

```text
O(m)
```

Total:

```text
O(n + m)
```

---

## Space Complexity

The frequency dictionary stores at most:

```text
Unique elements of nums1
```

Worst case:

```text
O(n)
```

More precisely:

```text
O(min(n, m))
```

if we build the frequency map using the smaller array.

---

# Complexity Summary

| Metric | Complexity |
|----------|------------|
| Time Complexity | O(n + m) |
| Space Complexity | O(n) |

---

# Optimality Analysis

Every element from both arrays must be inspected at least once.

Therefore:

```text
Minimum Possible Time Complexity ≈ O(n + m)
```

The HashMap solution achieves this efficiently.

---

# Pattern Summary

| Data Structure | Purpose |
|---------------|----------|
| Dictionary | Store frequencies |
| Frequency Counter | Track duplicates |
| Hashing | O(1) average lookup |

This problem is a classic example of using a HashMap to preserve duplicate occurrences while finding an intersection.
