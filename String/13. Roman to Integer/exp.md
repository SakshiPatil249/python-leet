# LeetCode 13 - Roman to Integer

## Problem Statement

Roman numerals are represented by seven symbols:

| Symbol | Value |
|----------|----------|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Given a Roman numeral string, convert it into an integer.

---

## Example 1

Input:

```python
s = "III"
```

Output:

```python
3
```

Explanation:

```text
I + I + I = 3
```

---

## Example 2

Input:

```python
s = "LVIII"
```

Output:

```python
58
```

Explanation:

```text
L = 50
V = 5
III = 3

50 + 5 + 3 = 58
```

---

## Example 3

Input:

```python
s = "MCMXCIV"
```

Output:

```python
1994
```

---

# Understanding Roman Numerals

Most Roman numerals are formed by adding values.

Example:

```text
VIII
```

means:

```text
5 + 1 + 1 + 1 = 8
```

---

# Special Cases

Sometimes a smaller numeral appears before a larger numeral.

Example:

```text
IV
```

Normally:

```text
1 + 5 = 6
```

But Roman numeral rules say:

```text
IV = 4
```

Meaning:

```text
5 - 1 = 4
```

---

Other examples:

| Roman | Value |
|---------|---------|
| IV | 4 |
| IX | 9 |
| XL | 40 |
| XC | 90 |
| CD | 400 |
| CM | 900 |

---

# Key Observation

If:

```text
Current Value < Next Value
```

then:

```text
Subtract Current Value
```

Otherwise:

```text
Add Current Value
```

---

# Example

Consider:

```python
s = "IV"
```

Values:

```text
I = 1
V = 5
```

Check:

```text
1 < 5
```

True.

So:

```text
-1 + 5 = 4
```

Correct answer.

---

# Why Use a Dictionary?

We need fast access to Roman numeral values.

```python
roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
```

Now:

```python
roman['X']
```

returns:

```python
10
```

in O(1) time.

---

# Algorithm

### Step 1

Create a Roman numeral dictionary.

```python
roman = {...}
```

---

### Step 2

Initialize total.

```python
total = 0
```

---

### Step 3

Traverse the string.

```python
for i in range(len(s)):
```

---

### Step 4

Compare current symbol with next symbol.

```python
roman[s[i]] < roman[s[i+1]]
```

---

### Step 5

If current value is smaller:

```python
total -= roman[s[i]]
```

Otherwise:

```python
total += roman[s[i]]
```

---

# Dry Run

Input:

```python
s = "MCMXCIV"
```

---

### M

```text
1000
```

Next:

```text
100
```

1000 > 100

Add:

```text
total = 1000
```

---

### C

```text
100
```

Next:

```text
1000
```

100 < 1000

Subtract:

```text
total = 900
```

---

### M

Add:

```text
total = 1900
```

---

### X

```text
10 < 100
```

Subtract:

```text
total = 1890
```

---

### C

Add:

```text
total = 1990
```

---

### I

```text
1 < 5
```

Subtract:

```text
total = 1989
```

---

### V

Add:

```text
total = 1994
```

Return:

```python
1994
```

---

# Why This Works

For normal numerals:

```text
VIII
```

all values are added.

For subtractive cases:

```text
IV
IX
XL
XC
CD
CM
```

the smaller value is automatically subtracted.

Thus the algorithm correctly handles both situations.

---

# Pattern Recognition

Common clues:

- Symbol → Value mapping
- Character conversion
- Lookup table needed

Think:

```text
HashMap / Dictionary
```

---

# Similar Problems

- Integer to Roman
- Decode String
- Excel Sheet Column Number
- Valid Parentheses

---

# Interview Takeaway

Whenever a problem involves:

```text
Character → Value Conversion
```

consider using a dictionary for O(1) lookups.

The key insight here is:

```text
If Current Value < Next Value
→ Subtract

Otherwise
→ Add
```

This single rule handles all Roman numeral cases.
