🧩 **Problem Name:**  
Read N Inputs (For Loop)

❓ **Goal:**  
✅ Read a number N  
✅ Then read N numbers (one per line)  
✅ Print each of those numbers, one per line, in the same order

🧠 **Concepts Used:**

- `input()`
- `int()`
- `for` loop
- `print()`

✅ **Code with Explanation:**

```python
# Read the number N
N = int(input())

# For each of the next N lines, read an integer and print it
for i in range(N):
    num = int(input())
    print(num)
```

🧪 **Sample Input:**

```
3
8
11
25
```

🧾 **Sample Output:**

```
8
11
25
```
