# LeetCode 26 - Remove Duplicates from Sorted Array

## Problem Statement

Given a sorted integer array `nums`, remove duplicates in-place such that each unique element appears only once.

The relative order of the elements should remain the same.

Return the number of unique elements `k`.

The first `k` positions of the array should contain the unique elements.

---

## Example 1

Input:

```python
nums = [1,1,2]
```

Output:

```python
2
```

Modified Array:

```python
[1,2,_]
```

---

## Example 2

Input:

```python
nums = [0,0,1,1,1,2,2,3,3,4]
```

Output:

```python
5
```

Modified Array:

```python
[0,1,2,3,4,_,_,_,_,_]
```

---

# Understanding the Problem

We are given a sorted array.

Since the array is sorted:

```python
[1,1,1,2,2,3,3,4]
```

all duplicates appear next to each other.

This is the most important observation.

We need to:

1. Keep only one occurrence of each number.
2. Modify the array in-place.
3. Return the count of unique elements.

---

# Key Observation

Because the array is sorted:

```python
1,1,1
```

duplicates will always be adjacent.

To detect duplicates we only need to compare:

```python
current element
```

with

```python
previous element
```

No HashMap or Set is required.

---

# Brute Force Approach

Use a Set.

Example:

```python
nums = [1,1,2]
```

Create:

```python
unique = {1,2}
```

Copy elements back.

---

## Problem with Brute Force

Extra memory is used.

Space Complexity:

```text
O(n)
```

The problem asks for an in-place solution.

---

# Optimized Approach - Two Pointers

## Idea

Use:

### Read Pointer

Scans every element.

### Write Pointer

Marks where the next unique element should be placed.

---

# Why Start Write = 1?

The first element is always unique.

Example:

```python
[1,1,2,3]
```

We keep:

```python
1
```

already at index 0.

The next unique element should be placed at:

```python
index = 1
```

Therefore:

```python
write = 1
```

---

# Algorithm

1. Keep first element.
2. Traverse from index 1.
3. Compare current element with previous element.
4. If different:

   * Copy current element to write position.
   * Increment write.
5. Return write.

---

# Dry Run

Input:

```python
nums = [0,0,1,1,1,2,2,3,3,4]
```

Initial:

```text
write = 1
```

Array:

```python
[0,0,1,1,1,2,2,3,3,4]
```

---

### Read = 1

```python
nums[1] = 0
nums[0] = 0
```

Duplicate.

Skip.

---

### Read = 2

```python
nums[2] = 1
nums[1] = 0
```

Different.

Copy:

```python
nums[1] = 1
```

Array:

```python
[0,1,1,1,1,2,2,3,3,4]
```

Increment:

```text
write = 2
```

---

### Read = 3

```python
1 == 1
```

Duplicate.

Skip.

---

### Read = 4

```python
1 == 1
```

Duplicate.

Skip.

---

### Read = 5

```python
2 != 1
```

Copy:

```python
nums[2] = 2
```

Array:

```python
[0,1,2,1,1,2,2,3,3,4]
```

Increment:

```text
write = 3
```

---

Continue similarly.

Final Array:

```python
[0,1,2,3,4,_,_,_,_,_]
```

Return:

```python
5
```

---

# Why This Works

Since duplicates are adjacent in a sorted array:

```python
1,1,1
```

we only need to check:

```python
nums[read]
```

against:

```python
nums[read - 1]
```

Whenever they differ:

```text
New unique element found.
```

Move it to the write position.

Thus:

* Unique elements remain at the beginning.
* Duplicates are overwritten.
* No extra memory is used.

---

# Pattern Recognition

This is a Two Pointer problem.

Key clues:

* Sorted array
* Remove duplicates
* In-place modification
* O(1) extra space

---

# Similar Problems

* Remove Element
* Move Zeroes
* Remove Duplicates from Sorted Array II
* Merge Sorted Array

---

# Interview Takeaway

When you see:

* Sorted array
* Remove duplicates
* In-place modification

Think:

```text
Two Pointers (Read + Write)
```

The sorted property allows duplicate detection using only adjacent comparisons, making the solution efficient and elegant.
