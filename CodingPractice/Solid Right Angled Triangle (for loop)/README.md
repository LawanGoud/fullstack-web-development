🧩 **Problem Name:**  
Solid Right Angled Triangle (Single For Loop)

❓ **Goal:**  
✅ Read a number N  
✅ Print a right-angled triangle pattern of N lines using asterisks (`*`), with each asterisk separated by a space  
✅ Use only a single `for` loop (no nested loops)  
✅ Use only basic concepts like `input()`, `int()`, `for` loop, string concatenation, and `print()`

🧠 **Concepts Used:**

- `input()`
- `int()`
- Single `for` loop
- String concatenation
- `print()`

✅ **Code with Explanation:**

```python
# Read the number N
N = int(input())

# Initialize an empty string for building the pattern line by line
row = ""

# Loop from 1 to N
for i in range(1, N + 1):
    # Add one "* " each iteration
    row = row + "* "
    # Print the current row string (which grows each time)
    print(row)
```

🧪 **Sample Input:**

```
4
```

🧾 **Sample Output:**

```
*
* *
* * *
* * * *
```
