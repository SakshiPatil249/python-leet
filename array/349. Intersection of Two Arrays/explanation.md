# LeetCode 349 - Intersection of Two Arrays

## Problem Statement

Given two integer arrays:

```python
nums1
nums2
```

Return an array containing their intersection.

Requirements:

- Each element in the result must be unique.
- The order of the output does not matter.

---

## Example 1

Input:

```python
nums1 = [1,2,2,1]
nums2 = [2,2]
```

Output:

```python
[2]
```

---

## Example 2

Input:

```python
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
```

Output:

```python
[9,4]
```

or

```python
[4,9]
```

Both are correct.

---

# Understanding the Problem

We need to find the elements that are present in both arrays.

Example:

```python
nums1 = [1,2,2,1]
nums2 = [2,2]
```

Common element:

```python
2
```

Even though `2` appears multiple times, it should appear only once in the answer.

---

# Key Observation

The problem only asks:

```text
Is an element present in both arrays?
```

It does not care about:

- Frequency
- Order

This is a strong hint to use a Set.

---

# Why Use a Set?

Sets automatically remove duplicates.

Example:

```python
set([1,2,2,1])
```

becomes:

```python
{1,2}
```

Sets also provide fast lookup operations.

Checking:

```python
2 in my_set
```

takes approximately:

```text
O(1)
```

time.

---

# Optimized Approach

Convert both arrays into sets.

Example:

```python
nums1 = [1,2,2,1]
nums2 = [2,2]
```

Convert:

```python
set1 = {1,2}
set2 = {2}
```

Now find common elements.

---

# Set Intersection

Python provides the intersection operator:

```python
&
```

Example:

```python
set1 = {1,2}
set2 = {2,3}

set1 & set2
```

Result:

```python
{2}
```

This gives exactly the unique common elements.

---

# Algorithm

### Step 1

Convert nums1 into a set.

```python
set1 = set(nums1)
```

### Step 2

Convert nums2 into a set.

```python
set2 = set(nums2)
```

### Step 3

Find intersection.

```python
set1 & set2
```

### Step 4

Convert the result back to a list.

```python
return list(set1 & set2)
```

---

# Dry Run

Input:

```python
nums1 = [1,2,2,1]
nums2 = [2,2]
```

### Create Sets

```python
set1 = {1,2}
set2 = {2}
```

### Intersection

```python
set1 & set2
```

Result:

```python
{2}
```

### Convert to List

```python
[2]
```

Return:

```python
[2]
```

---

# Why This Works

Sets remove duplicates automatically.

Example:

```python
set([1,2,2,1])
```

becomes:

```python
{1,2}
```

Taking the intersection of two sets gives all elements present in both sets.

Thus:

- Duplicates are removed.
- Only common elements remain.
- The solution is efficient.

---

# Pattern Recognition

Common clues:

- Find common elements
- Ignore duplicates
- Fast lookup needed

Think:

```text
Hash Set
```

---


# Interview Takeaway

Whenever you need:

```text
Fast membership checking
```

or

```text
Unique elements only
```

consider using a Set.

Hash Sets are one of the most frequently used data structures in coding interviews.
