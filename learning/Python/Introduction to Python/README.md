# Intro to Programming with Python

**Software:**  
Software is a set of instructions to the hardware.

**Programming:**  
Programming means writing the instructions to create a software.

**Code:**  
The instructions that we write to create software is called **code**.

**Syntax:**  
Similar to grammar rules in English or Hindi, each programming language has a unique set of rules. These rules are called the **syntax** of a programming language.

## Why Python

Python is an easy-to-learn, powerful programming language. With Python, you can create programs using a minimal amount of code.

Compare the code below that prints the message **"Hello World"** in Java and Python:

**Java:**

```java
class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

**Python:**

```python
print("Hello World")
```

## Applications of Python

Python is a versatile language used in many different fields:

- Artificial Intelligence (AI)
- Machine Learning (ML)
- Big Data
- Smart Devices / Internet of Things (IoT)
- Cyber Security
- Game Development
- Backend Web Development
- Automation, and more

## Career Opportunities

Python developers have a wide range of job opportunities around the world:

- DevOps Engineer
- Software Developer
- Data Analyst
- Data Scientist
- Machine Learning Engineer
- AI Scientist
- Automation Tester
- Backend Developer

## Hello World Program in Python

Here is a simple Python code that displays the message **"Hello World"**:

```python
print("Hello World!")  # output: Hello World!
```

## Possible Mistakes

Here are some common mistakes you might make while writing Python code to display the message **"Hello World"**, along with examples:

---

### 🔴 1. Spelling Mistake in `print`

**Incorrect:**

```python
prnt("Hello World")
```

❌ This will cause an error because `prnt` is not a valid Python command.

---

### 🔴 2. Using an Uppercase ‘P’ in `Print`

**Incorrect:**

```python
Print("Hello World")
```

❌ Python is case-sensitive, so `Print` is not the same as `print`.

---

### 🔴 3. Missing Quotes Around the Text

**Incorrect:**

```python
print(Hello World)
```

❌ This will result in an error because Python doesn’t know what `Hello` or `World` means without quotes.

---

### 🔴 4. Missing Parentheses

**Incorrect (Python 3):**

```python
print "Hello World"
```

❌ This syntax was valid in Python 2, but in Python 3, parentheses are required.

---

### ✅ Correct Code:

```python
print("Hello World")
```

This is the proper way to write the code in Python 3 to display a message.
Here's your updated content, rewritten in a clear and properly formatted Markdown version with headings, spacing, and code blocks:

## Printing Without Quotes

If you want to **calculate** and print the result of `2 + 5`, **do not** use quotes:

```python
print(2 + 5)  # output: 7
```

If you want to **display the exact text** "2 + 5" instead of calculating, **use quotes**:

```python
print("2 + 5")  # output: 2 + 5
```

---

## Calculations with Python

Python can perform basic arithmetic operations easily.

### ➕ Addition

Addition is done using the `+` sign. It adds two numbers.

```python
print(2 + 5)      # output: 7
print(1 + 1.5)    # output: 2.5
```

---

### ➖ Subtraction

Subtraction is done using the `-` sign. It subtracts one number from another.

```python
print(5 - 2)      # output: 3
```

---

### ✖️ Multiplication

Multiplication is done using the `*` sign.

```python
print(2 * 5)      # output: 10
print(5 * 0.5)    # output: 2.5
```

---

### ➗ Division

Division is done using the `/` sign. It divides one number by another.

```python
print(5 / 2)      # output: 2.5
print(4 / 2)      # output: 2.0
```
