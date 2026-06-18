# LeetCode 268 - Missing Number

## Problem Statement

Given an array containing `n` distinct numbers taken from the range:

```python
[0, n]
```

return the only number that is missing from the array.

---

## Example 1

Input:

```python
nums = [3,0,1]
```

Output:

```python
2
```

Because:

```python
Expected: [0,1,2,3]
Present : [0,1,3]
Missing : 2
```

---

## Example 2

Input:

```python
nums = [0,1]
```

Output:

```python
2
```

---

# Understanding the Problem

We are given:

```python
n distinct numbers
```

from:

```python
0 to n
```

Exactly one number is missing.

Example:

```python
nums = [3,0,1]
```

Length:

```python
n = 3
```

Expected numbers:

```python
[0,1,2,3]
```

Missing:

```python
2
```

---

# Interview Thought Process

Let's think step by step.

We know:

```python
0,1,2,3,...,n
```

should exist.

If we calculate:

```python
Expected Sum
```

and compare it with:

```python
Actual Sum
```

the difference must be the missing number.

---

# Key Observation

Example:

```python
nums = [3,0,1]
```

Expected numbers:

```python
0 + 1 + 2 + 3
```

Expected Sum:

```python
6
```

Actual Sum:

```python
3 + 0 + 1 = 4
```

Difference:

```python
6 - 4 = 2
```

Missing number:

```python
2
```

---

# Mathematical Formula

Sum of numbers from:

```python
0 to n
```

is:

Therefore:

```python
expected_sum = n * (n + 1) // 2
```

---

# Algorithm

Step 1:

Find array length.

```python
n = len(nums)
```

---

Step 2:

Calculate expected sum.

```python
expected_sum = n * (n + 1) // 2
```

---

Step 3:

Calculate actual sum.

```python
actual_sum = sum(nums)
```

---

Step 4:

Return difference.

```python
expected_sum - actual_sum
```

---

# Dry Run

Input:

```python
nums = [9,6,4,2,3,5,7,0,1]
```

Length:

```python
n = 9
```

Expected numbers:

```python
0,1,2,3,4,5,6,7,8,9
```

Expected Sum:

```python
9 * 10 // 2 = 45
```

Actual Sum:

```python
37
```

Difference:

```python
45 - 37 = 8
```

Answer:

```python
8
```

---

# Why This Works

The expected sum includes every number from:

```python
0 to n
```

The actual sum is missing exactly one value.

Subtracting the two sums leaves only the missing number.

---

# Alternative Approaches

## Approach 1: Hash Set

Store all numbers in a set.

Check from:

```python
0 to n
```

to find missing value.

Time:

```text
O(n)
```

Space:

```text
O(n)
```

---

## Approach 2: Sorting

Sort array.

Find where sequence breaks.

Time:

```text
O(n log n)
```

Space:

```text
O(1)
```

or

```text
O(n)
```

depending on sorting implementation.

---

## Approach 3: Sum Formula (Best)

Time:

```text
O(n)
```

Space:

```text
O(1)
```

---

# Pattern Recognition

Clues:

* Numbers are from 0 to n.
* Exactly one number missing.
* Distinct values.

Think:

```text
Math Formula
```

or

```text
XOR Pattern
```

---

# Interview Takeaway

Whenever you see:

```text
Numbers from 0 to n
One number missing
```

Immediately consider:

1. Sum Formula
2. XOR

These are the two most common optimal solutions.
