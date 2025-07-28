🧩 **Problem Name:**  
Two Right Angled Triangles (For Loop)

❓ **Goal:**  
✅ Read a number `N`  
✅ Print two right-angled triangles of `N` rows each, one after the other, using numbers  
✅ For each triangle, the 1st row has one `1`, the 2nd row has two `2`s, the 3rd row has three `3`s, ..., the Nth row has N `N`s  
✅ Use only basic concepts: `input()`, `int()`, `for` loop, string multiplication, and `print()`

🧠 **Concepts Used:**

- `input()`
- `int()`
- Single `for` loop (repeated for each triangle)
- String multiplication
- `print()`

✅ **Code with Explanation:**

```python
# Read the number N
N = int(input())

# Print the first right-angled triangle
for i in range(1, N + 1):
    # Print the row number i, i times, as a string
    print(str(i) * i)

# Print the second right-angled triangle
for i in range(1, N + 1):
    print(str(i) * i)
```

### Explanation:

- `N = int(input())`: Reads the number of rows for the triangles.
- The first `for` loop prints the first triangle, with row number used as the digit and repeated that many times.
- The second `for` loop prints the second triangle in the same way.
- Both triangles are printed one after another.

🧪 **Sample Input:**

```
4
```

🧾 **Sample Output:**

```
1
22
333
4444
1
22
333
4444
```
