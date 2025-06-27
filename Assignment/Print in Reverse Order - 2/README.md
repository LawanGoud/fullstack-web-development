### 🔁 Print in Reverse Order - 2

**Task:**  
Write a program that reads two words `A` and `B`, and prints them in **reverse order**,  
separated by `###` (three hash symbols).

---

### ✅ Example

**Input:**

```
apple
banana
```

**Output:**

```
banana
###
apple
```

---

### ✅ Python Code

```python
a = input()
b = input()
print(b)
print("###")
print(a)
```

---

### 🧠 Explanation

- `input()` reads the two words: first assigned to `a`, second to `b`.
- They are printed in reverse order: `b` first, then `a`.
- `"###"` is used to join the words.
