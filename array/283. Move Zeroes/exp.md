# LeetCode 283 - Move Zeroes

## Problem Statement

Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements.

The operation must be performed in-place without creating another array.

---

## Example 1

Input:

```python
nums = [0,1,0,3,12]
```

Output:

```python
[1,3,12,0,0]
```

---

## Example 2

Input:

```python
nums = [0]
```

Output:

```python
[0]
```

---

# Understanding the Problem

We need to:

1. Move all non-zero elements toward the beginning.
2. Move all zeroes toward the end.
3. Maintain the order of non-zero elements.
4. Use O(1) extra space.

Important:

```text
[1,3,12]
```

must remain in the same order.

We cannot rearrange them randomly.

---

# Initial Thought Process

Consider:

```python
nums = [0,1,0,3,12]
```

Non-zero elements:

```text
1, 3, 12
```

Zero elements:

```text
0, 0
```

Desired result:

```python
[1,3,12,0,0]
```

The challenge is doing this in-place.

---

# Brute Force Approach

Create a new array.

Step 1:

Store all non-zero elements.

```python
[1,3,12]
```

Step 2:

Count the number of zeroes.

```python
2
```

Step 3:

Append those zeroes.

```python
[1,3,12,0,0]
```

Copy back into original array.

---

## Drawback

Uses extra memory.

Space Complexity:

```text
O(n)
```

---

# Optimized Approach - Two Pointers

## Key Observation

We only care about non-zero elements.

If we move all non-zero elements to the front, zeroes automatically end up at the back.

---

## Two Pointer Strategy

### Read Pointer

Traverses every element.

### Write Pointer

Tracks where the next non-zero element should go.

---

# Algorithm

1. Initialize `write = 0`.
2. Traverse array using `read`.
3. If current element is non-zero:

   * Swap it with position `write`.
   * Increment `write`.
4. Continue until end.

---

# Dry Run

Input:

```python
nums = [0,1,0,3,12]
```

Initial:

```text
write = 0
```

---

### Read = 0

```python
nums[0] = 0
```

Skip.

Array:

```python
[0,1,0,3,12]
```

---

### Read = 1

```python
nums[1] = 1
```

Swap:

```python
nums[0], nums[1]
```

Array:

```python
[1,0,0,3,12]
```

Increment:

```text
write = 1
```

---

### Read = 2

```python
nums[2] = 0
```

Skip.

---

### Read = 3

```python
nums[3] = 3
```

Swap:

```python
nums[1], nums[3]
```

Array:

```python
[1,3,0,0,12]
```

Increment:

```text
write = 2
```

---

### Read = 4

```python
nums[4] = 12
```

Swap:

```python
nums[2], nums[4]
```

Array:

```python
[1,3,12,0,0]
```

Increment:

```text
write = 3
```

---

# Final Result

```python
[1,3,12,0,0]
```

---

# Why This Works

The write pointer always points to the next position where a non-zero element should be placed.

Whenever a non-zero element is found:

1. Move it to the write position.
2. Increase write pointer.

By the end:

* All non-zero elements are grouped at the beginning.
* All zeroes naturally shift to the end.
* Relative order remains unchanged.

---

# Pattern Recognition

This problem belongs to the Two Pointer pattern.

Clues:

* Modify array in-place.
* Move specific elements.
* Preserve relative order.
* Constant extra space.

---

# Similar Problems

* Remove Element
* Remove Duplicates from Sorted Array
* Sort Colors
* Partition Array
* Merge Sorted Array

---

# Interview Takeaway

When an array problem says:

* Move elements in-place
* Maintain order
* O(1) extra space

Think:

```text
Two Pointers (Read + Write)
```

This is one of the most frequently used array patterns in coding interviews.
