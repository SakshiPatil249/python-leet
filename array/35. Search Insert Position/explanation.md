# LeetCode 35 - Search Insert Position

## Problem Statement

Given a sorted array of distinct integers and a target value, return the index if the target is found.

If the target is not found, return the index where it would be inserted in order.

---

## Example 1

Input:

```python
nums = [1,3,5,6]
target = 5
```

Output:

```python
2
```

Because:

```python
nums[2] = 5
```

---

## Example 2

Input:

```python
nums = [1,3,5,6]
target = 2
```

Output:

```python
1
```

Because:

```python
[1,2,3,5,6]
```

Target should be inserted at index 1.

---

## Example 3

Input:

```python
nums = [1,3,5,6]
target = 7
```

Output:

```python
4
```

Because:

```python
[1,3,5,6,7]
```

Target should be inserted at the end.

---

# Understanding the Problem

We need to find:

1. Target's index if it exists.
2. Otherwise, the position where it should be inserted.

The array is sorted.

This is the biggest clue.

Whenever you see:

```text
Sorted Array
Search
```

think:

```text
Binary Search
```

---

# Brute Force Approach

Traverse the entire array.

Example:

```python
for i in range(len(nums)):
    if nums[i] >= target:
        return i
```

If not found:

```python
return len(nums)
```

### Complexity

```text
Time Complexity: O(n)
Space Complexity: O(1)
```

This works but does not use the sorted property.

---

# Optimized Approach - Binary Search

## Why Binary Search?

Since the array is sorted:

```python
[1,3,5,6]
```

we can eliminate half the search space every time.

Instead of checking every element:

```text
1 → 3 → 5 → 6
```

we jump directly to the middle.

---

# Binary Search Idea

Maintain:

```python
left
right
```

Find:

```python
mid = (left + right) // 2
```

Compare:

```python
nums[mid]
```

with:

```python
target
```

and eliminate half the array.

---

# Dry Run

Input:

```python
nums = [1,3,5,6]
target = 2
```

Initial:

```text
left = 0
right = 3
```

---

### Iteration 1

```python
mid = (0 + 3) // 2
mid = 1
```

Value:

```python
nums[1] = 3
```

Compare:

```python
3 > 2
```

Move:

```python
right = mid - 1
right = 0
```

---

### Iteration 2

```python
left = 0
right = 0

mid = 0
```

Value:

```python
nums[0] = 1
```

Compare:

```python
1 < 2
```

Move:

```python
left = mid + 1
left = 1
```

---

Now:

```text
left = 1
right = 0
```

Loop ends.

Return:

```python
left
```

Answer:

```python
1
```

---

# Why Return Left?

When the loop finishes:

```python
left > right
```

At this moment:

```python
left
```

points exactly to the position where the target should be inserted.

Example:

```python
nums = [1,3,5,6]
target = 2
```

Final:

```text
left = 1
right = 0
```

Target belongs at:

```python
index = 1
```

Therefore:

```python
return left
```

---

# Visual Understanding

Array:

```python
[1,3,5,6]
```

Target:

```python
2
```

Final state:

```text
1 < 2 < 3
```

Insertion position:

```python
index = 1
```

which is exactly where left stops.

---

# Pattern Recognition

This is a classic Binary Search problem.

Common clues:

* Sorted array
* Search element
* Return index
* O(log n) solution expected

---

# Similar Problems

* Binary Search
* First Bad Version
* Guess Number Higher or Lower
* Find Peak Element
* Search in Rotated Sorted Array

---

# Interview Takeaway

When you see:

```text
Sorted Array
Search
```

your first thought should be:

```text
Binary Search
```

The key insight in this problem is understanding why:

```python
return left
```

gives the correct insertion position when the target does not exist.
