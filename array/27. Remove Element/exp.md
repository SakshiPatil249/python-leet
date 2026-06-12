# LeetCode 27 - Remove Element

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place and return the number of elements that are not equal to `val`.

The first `k` positions of the array should contain all elements that are not equal to `val`, where `k` is the returned value.

---

## Example

Input:

```python
nums = [3,2,2,3]
val = 3
```

Output:

```python
2
```

Modified Array:

```python
[2,2,_,_]
```

The values after the first `k` elements are not important.

---

# Understanding the Problem

The problem asks us to remove all occurrences of a specific value from the array without creating a new array.

Important observations:

1. We must modify the original array.
2. We only care about the first `k` elements after modification.
3. The order of remaining elements does not necessarily matter.
4. We should use constant extra space.

---

# Approach 1: Brute Force

Create a new array containing only elements that are not equal to `val`.

Example:

```python
nums = [3,2,2,3]
val = 3

result = [2,2]
```

Then copy the elements back to the original array.

### Drawback

Although this approach works, it uses additional memory.

Space Complexity:

```text
O(n)
```

---

# Optimized Approach: Two Pointers

## Key Idea

Use two pointers:

### Read Pointer

Traverses every element of the array.

### Write Pointer

Tracks where the next valid element should be placed.

---

## Algorithm

1. Initialize `write = 0`.
2. Traverse the array using a read pointer.
3. If the current element is not equal to `val`:

   * Copy it to index `write`.
   * Increment `write`.
4. Continue until all elements are processed.
5. Return `write`.

The value of `write` represents the number of valid elements remaining.

---

# Dry Run

Input:

```python
nums = [3,2,2,3]
val = 3
```

Initial State:

```text
write = 0
```

### Step 1

```python
nums[0] = 3
```

Equals `val`.

Skip it.

```text
write = 0
```

---

### Step 2

```python
nums[1] = 2
```

Not equal to `val`.

Copy:

```python
nums[0] = 2
```

Array becomes:

```python
[2,2,2,3]
```

Increment write:

```text
write = 1
```

---

### Step 3

```python
nums[2] = 2
```

Valid element.

Copy:

```python
nums[1] = 2
```

Increment write:

```text
write = 2
```

---

### Step 4

```python
nums[3] = 3
```

Equals `val`.

Skip.

---

Final Array:

```python
[2,2,_,_]
```

Return:

```python
2
```

---

# Why the Solution Works

The write pointer always points to the next available position where a valid element should be stored.

Whenever we encounter a valid element:

1. Move it to the write position.
2. Advance the write pointer.

By the end:

* All valid elements are moved to the front.
* Unwanted elements are effectively removed.
* No additional array is required.

---

# Pattern Recognition

This problem belongs to the Two Pointer pattern.

Common indicators:

* Modify array in-place.
* Remove elements.
* Move valid elements forward.
* Constant space requirement.

Similar Problems:

* Remove Duplicates from Sorted Array
* Move Zeroes
* Sort Colors
* Merge Sorted Array

---

# Final Takeaway

Whenever you see phrases such as:

* "In-place modification"
* "Remove elements"
* "O(1) extra space"

Think about using the Two Pointer technique with a Read Pointer and a Write Pointer.
