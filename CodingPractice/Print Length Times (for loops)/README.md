🧩 **Problem Name:**  
Print Length times (For Loop)

❓ **Goal:**  
✅ Read a string  
✅ Print the first character (the character at index `0`) of the string, exactly as many times as the length of the string (once per line)

🧠 **Concepts Used:**

- `input()`
- `len()`
- `for` loop
- String indexing
- `print()`

✅ **Code with Explanation:**

```python
# Read the input string
s = input()

# Get the first character of the string
first_char = s[0]

# Get the length of the string
length = len(s)

# Print the first character 'length' times, each on a new line
for i in range(length):
    print(first_char)
```

🧪 **Sample Input:**  
query

🧾 **Sample Output:**

```
q
q
q
q
q
```
