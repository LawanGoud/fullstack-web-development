🧩 **Problem Name:**  
Right Angled Triangle (For Loop, Single Loop)

❓ **Goal:**  
✅ Read a number `num`  
✅ Print a right-angled triangle pattern of asterisks (`*`), where the 1st row has 1 `*`, the 2nd row has 2 `*`, and so on up to `num` rows  
✅ Use only a single `for` loop, no nested loops  
✅ Each row prints a string of stars created by multiplying the `*` character

🧠 **Concepts Used:**

- `input()`
- `int()`
- Single `for` loop
- String multiplication
- `print()`

✅ **Code with Explanation:**

```python
# Read the number of rows
num = int(input())

# Loop from 1 to num (inclusive)
for each_num in range(1, num + 1):
    # Create a string with 'each_num' asterisks
    result = "*" * each_num
    # Print the current row of stars
    print(result)
```

### Explanation:

- `num = int(input())`: Reads the number of rows for the triangle.
- The `for` loop runs from 1 up to `num` (inclusive).
- In each iteration, it creates a string with the current number of stars by multiplying `"*"` by `each_num`.
- `print(result)` prints that string, building the triangle line by line without any nested loop.

🧪 **Sample Input:**

```
4
```

🧾 **Sample Output:**

```
*
**
***
****
```
