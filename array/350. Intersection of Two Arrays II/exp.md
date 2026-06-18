# LeetCode 350 - Intersection of Two Arrays II

## Problem Statement

Given two integer arrays:

```python
nums1
nums2
```

Return their intersection.

Unlike LeetCode 349:

```text
Duplicates must be included.
```

Each element should appear as many times as it appears in both arrays.

---

## Example 1

Input:

```python
nums1 = [1,2,2,1]
nums2 = [2,2]
```

Output:

```python
[2,2]
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
[4,9]
```

or

```python
[9,4]
```

Both are correct.

---

# Difference Between 349 and 350

### LeetCode 349

Input:

```python
nums1 = [1,2,2,1]
nums2 = [2,2]
```

Output:

```python
[2]
```

Only unique values.

---

### LeetCode 350

Input:

```python
nums1 = [1,2,2,1]
nums2 = [2,2]
```

Output:

```python
[2,2]
```

Duplicates must be preserved.

---

# Why Set Won't Work

For Problem 349:

```python
set([1,2,2,1])
```

becomes:

```python
{1,2}
```

Duplicates disappear.

For this problem, duplicates matter.

Therefore:

```text
Hash Set is not enough.
```

We need frequency information.

---

# Key Observation

We need to know:

```text
How many times each number appears.
```

Example:

```python
nums1 = [1,2,2,1]
```

Frequency:

```python
{
    1: 2,
    2: 2
}
```

This is exactly what a HashMap (Dictionary) provides.

---

# Optimized Approach

Use a dictionary to store frequencies of nums1.

Then iterate through nums2.

Whenever:

```python
freq[num] > 0
```

the number belongs in the intersection.

Add it to the answer and decrease its frequency.

---

# Algorithm

### Step 1

Create a frequency dictionary.

```python
freq = {}
```

---

### Step 2

Count occurrences in nums1.

```python
for num in nums1:
    freq[num] = freq.get(num, 0) + 1
```

Example:

```python
nums1 = [1,2,2,1]
```

Produces:

```python
{
    1: 2,
    2: 2
}
```

---

### Step 3

Traverse nums2.

```python
for num in nums2:
```

---

### Step 4

If the number exists and frequency is positive:

```python
if num in freq and freq[num] > 0:
```

Add it to result.

```python
result.append(num)
```

Decrease count.

```python
freq[num] -= 1
```

---

# Dry Run

Input:

```python
nums1 = [1,2,2,1]
nums2 = [2,2]
```

---

### Build Frequency Map

```python
freq = {
    1: 2,
    2: 2
}
```

---

### First 2

```python
freq[2] = 2
```

Add to answer.

```python
result = [2]
```

Decrease frequency.

```python
freq[2] = 1
```

---

### Second 2

```python
freq[2] = 1
```

Add to answer.

```python
result = [2,2]
```

Decrease frequency.

```python
freq[2] = 0
```

---

Loop ends.

Return:

```python
[2,2]
```

---

# Why This Works

The frequency dictionary tracks how many copies of each number are still available.

Every time we use a number:

```python
freq[num] -= 1
```

ensures we don't use it more times than it appears.

Thus duplicates are handled correctly.

---

# Pattern Recognition

Common clues:

- Duplicates matter
- Count occurrences
- Frequency tracking

Think:

```text
HashMap / Frequency Counter
```

---

# Similar Problems

- Two Sum
- Valid Anagram
- Ransom Note
- Top K Frequent Elements
- Find All Anagrams in a String

---

# Interview Takeaway

When the problem asks:

```text
How many times does something occur?
```

or

```text
Duplicates must be preserved
```

immediately consider:

```text
HashMap (Dictionary)
```

Frequency counting is one of the most common interview patterns.
