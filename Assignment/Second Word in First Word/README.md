### 🔍 Second Word in First Word

**Task:**  
Write a program that reads two words `W1` and `W2`.  
`W2` is at the **beginning** of `W1`.

Print the **index of the last character** of `W2` in `W1`.

---

### ✅ Example:

**Input:**

```
sunflower
sun
```

**Output:**

```
2
```

🧠 Because `"sun"` ends at index `2` in `"sunflower"`  
(Indexes start at 0: `s=0`, `u=1`, `n=2`)

---

### ✅ Python Code:

```python
w1 = input()
w2 = input()
print(len(w2) - 1)
```

---

### 🧠 Explanation:

- `len(w2)` gives the number of characters in `W2`.
- Since indexing starts at 0, we subtract 1 to get the index of the **last character** of `W2`.
