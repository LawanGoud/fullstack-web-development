🧩 **Problem Name:**  
10 Numbers after N (For Loop)

❓ **Goal:**  
✅ Read a number `N`  
✅ Print the next 10 numbers after `N`, one number per line

🧠 **Concepts Used:**

- `input()`
- `int()`
- `for` loop
- `print()`

✅ **Code with Explanation:**

```python
# Read the number N
N = int(input())

# Print the next 10 numbers after N
for i in range(1, 11):        # Loop variable i from 1 to 10
    print(N + i)              # Print N plus i
```

### Explanation:

- `N = int(input())`: Reads a number from the user and converts it to an integer.
- `range(1, 11)`: Generates numbers from 1 to 10, so when these are added to `N`, you get the next ten numbers after `N`.
- Inside the loop, `print(N + i)` prints each of those numbers on a new line.

🧪 **Sample Input:**

```
4
```

🧾 **Sample Output:**

```
5
6
7
8
9
10
11
12
13
14
```
