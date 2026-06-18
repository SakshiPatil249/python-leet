# Complexity Analysis

## Dictionary-Based Solution

### Time Complexity

We traverse the string once:

```python
for i in range(len(s))
```

Each lookup:

```python
roman[s[i]]
```

takes:

```text
O(1)
```

Therefore:

```text
O(n)
```

where n is the length of the Roman numeral string.

---

## Space Complexity

The dictionary contains only 7 fixed Roman symbols:

```python
{
'I','V','X','L','C','D','M'
}
```

Regardless of input size.

Therefore:

```text
O(1)
```

constant space.

---

# Complexity Summary

| Metric | Complexity |
|----------|------------|
| Time Complexity | O(n) |
| Space Complexity | O(1) |

---

# Why Is This Optimal?

Every character must be examined at least once.

Therefore:

```text
Best Possible Time Complexity = O(n)
```

The algorithm uses only:

- One dictionary
- One integer variable

Thus:

```text
Best Possible Space Complexity = O(1)
```

This makes the solution optimal.

---

# Pattern Summary

| Concept | Usage |
|----------|----------|
| Dictionary | Symbol → Value mapping |
| Greedy Rule | Add or subtract based on next value |
| Single Pass Traversal | O(n) solution |

This problem is a classic example of combining a lookup table (dictionary) with a simple greedy rule.
