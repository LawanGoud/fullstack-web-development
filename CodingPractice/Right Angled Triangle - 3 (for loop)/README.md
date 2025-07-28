🧩 **Problem Name:**  
Right Angled Triangle with Symbols (For Loop)

❓ **Goal:**  
✅ Read a number `N`  
✅ Print a right-angled triangle of `N` rows  
✅ The first `N-1` rows should use stars (`*`) separated by a space  
✅ The last (Nth) row should use pluses (`+`) separated by a space  
✅ Use only basic concepts: `input()`, `int()`, `for` loop, and `print()`

🧠 **Concepts Used:**

- `input()`
- `int()`
- `for` loop
- String multiplication
- `print()`

✅ **Code with Explanation:**

```python
# Read the number N
N = int(input())

# For the first N-1 rows, print stars
for i in range(1, N):
    print("* " * i)

# For the last row, print pluses
print("+ " * N)
```

### Explanation:

- `N = int(input())`: Reads the number of rows for the triangle.
- The first `for` loop runs from 1 to `N-1`; for each row, it prints `i` stars with spaces, using `print("* " * i)`.
- The last line uses `print("+ " * N)` to print `N` plus signs with spaces, forming the bottom row of the triangle.

🧪 **Sample Input:**

```
4
```

🧾 **Sample Output:**

```
*
* *
* * *
+ + + +
```
