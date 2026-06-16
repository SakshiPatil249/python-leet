# LeetCode 88 - Merge Sorted Array

## Problem Statement

You are given two sorted integer arrays:

```python
nums1
nums2
```

The array `nums1` has a size of `m + n`, where:

* First `m` elements are valid.
* Last `n` elements are empty spaces represented by zeroes.

Merge `nums2` into `nums1` such that the final array remains sorted.

The merge must be performed in-place.

---

# Example

Input:

```python
nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3
```

Output:

```python
[1,2,2,3,5,6]
```

---

# Understanding the Problem

Initially:

```python
nums1 = [1,2,3,0,0,0]
```

Only:

```python
[1,2,3]
```

are valid elements.

The last three zeroes are placeholders.

Our goal is to insert elements from nums2 into nums1 while keeping the entire array sorted.

---

# Key Observation

If we start merging from the front, we may overwrite important values before using them.

Example:

```python
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
```

If we write from the beginning, values like:

```python
1
2
3
```

can be lost.

Therefore, we merge from the back.

---

# Why Merge from the End?

The largest elements are always located at the end of both sorted arrays.

Example:

```python
nums1 = [1,2,3]
nums2 = [2,5,6]
```

Largest elements:

```python
3
6
```

The larger one belongs at the last position.

By filling the array from the end, we avoid overwriting useful data.

---

# Three Pointer Approach

We use three pointers.

### Pointer p

Points to the last position in nums1.

```python
p = m + n - 1
```

---

### Pointer m

Points to the last valid element in nums1.

```python
m = m - 1
```

---

### Pointer n

Points to the last element in nums2.

```python
n = n - 1
```

---

# Algorithm

1. Compare nums1[m] and nums2[n].
2. Place the larger value at position p.
3. Move the corresponding pointer.
4. Move p backward.
5. Continue until one array is exhausted.
6. Copy any remaining nums2 elements.

---

# Dry Run

Input:

```python
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
```

Initial:

```text
p = 5
m = 2
n = 2
```

---

## Step 1

Compare:

```python
3 and 6
```

Place:

```python
nums1[5] = 6
```

Array:

```python
[1,2,3,0,0,6]
```

Move:

```text
n = 1
p = 4
```

---

## Step 2

Compare:

```python
3 and 5
```

Place:

```python
nums1[4] = 5
```

Array:

```python
[1,2,3,0,5,6]
```

Move:

```text
n = 0
p = 3
```

---

## Step 3

Compare:

```python
3 and 2
```

Place:

```python
nums1[3] = 3
```

Array:

```python
[1,2,3,3,5,6]
```

Move:

```text
m = 1
p = 2
```

---

## Step 4

Compare:

```python
2 and 2
```

Place:

```python
nums1[2] = 2
```

Array:

```python
[1,2,2,3,5,6]
```

Move:

```text
n = -1
```

Loop ends.

Final Result:

```python
[1,2,2,3,5,6]
```

---

# Why Do We Copy Remaining nums2 Elements?

After the main loop ends:

```python
while m >= 0 and n >= 0
```

there may still be elements left inside nums2.

These elements have never been copied into nums1.

Therefore:

```python
while n >= 0:
    nums1[p] = nums2[n]
```

copies them into their correct positions.

If elements remain in nums1, no action is needed because they are already in the correct place.

---

# Pattern Recognition

This problem uses:

```text
Backward Two Pointers
```

Common clues:

* Two sorted arrays
* In-place merge
* O(1) extra space requirement

---

# Interview Takeaway

When asked to merge sorted arrays without extra space:

1. Start from the end.
2. Use backward pointers.
3. Fill the largest element first.

This avoids overwriting important data and achieves the optimal solution.
