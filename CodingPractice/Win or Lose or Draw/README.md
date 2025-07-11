## 🧩 **Problem Name:**

**Win or Lose or Draw**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads two scores `A` and `B`
- ✅ Compares `A` with `B` and prints:

  - `"Win"` if `A > B`
  - `"Draw"` if `A == B`
  - `"Lose"` if `A < B`

---

## 🧠 **Concepts Used:**

- Input/output
- Comparison operators (`>`, `<`, `==`)
- `if`, `elif`, `else` statements

---

## ✅ **Code with Comments and Explanation:**

```python
# Read two scores from the user
player_score = int(input())  # Example: 26
opponent_score = int(input())  # Example: 47

# Check if player's score is greater
if player_score > opponent_score:
    print("Win")
# If scores are equal
elif player_score == opponent_score:
    print("Draw")
# Otherwise, opponent has a higher score
else:
    print("Lose")
```

---

## 🧪 **Sample Input:**

```
26
47
```

## 🧾 **Sample Output:**

```
Lose
```

---
