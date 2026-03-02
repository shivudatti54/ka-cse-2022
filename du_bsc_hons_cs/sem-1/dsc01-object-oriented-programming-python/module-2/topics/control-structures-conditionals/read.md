# Control Structures: Conditionals in Python

## Object Oriented Programming (Python) — BSc (Hons) Computer Science

### Delhi University NEP 2024 UGCF Syllabus

---

## 1. Introduction

Control structures are fundamental building blocks in any programming language that determine the flow of execution. Among these, **conditional statements** (also known as **branching statements**) allow the program to make decisions based on certain conditions. In Python, conditionals enable your code to respond dynamically to different inputs and situations, making programs intelligent and interactive.

### Real-World Relevance

Consider these everyday scenarios where conditionals are essential:

- **Banking Systems**: Checking if account balance is sufficient before allowing a withdrawal
- **E-commerce Platforms**: Applying discounts based on customer membership tier
- **Weather Applications**: Displaying appropriate clothing suggestions based on temperature
- **Authentication Systems**: Verifying username and password before granting access
- **Game Development**: Determining if a player has won or lost based on score

Without conditionals, software would execute the same instructions every time, regardless of context or user input. This chapter covers the complete spectrum of conditional structures in Python, from basic `if` statements to the modern `match` statement introduced in Python 3.10.

---

## 2. The `if` Statement

The simplest form of conditional in Python is the `if` statement. It executes a block of code only when a specified condition evaluates to `True`.

### Syntax

```python
if condition:
    # block of code to execute
    statement1
    statement2
```

**Important Notes:**
- The condition must be an expression that evaluates to a boolean value (`True` or `False`)
- The code block must be **indented** (typically 4 spaces) — this is syntactically required in Python
- A colon (`:`) must follow the condition

### Example 1: Basic `if` Statement

```python
# Check if a number is positive
number = 10

if number > 0:
    print("The number is positive")

# Output: The number is positive
```

### Example 2: Using `if` in Real-World Context

```python
# User authentication check
username = input("Enter username: ")

if username == "admin":
    print("Welcome, Administrator!")
```

---

## 3. The `if-else` Statement

The `if-else` statement provides an alternative path when the condition is `False`. It ensures that exactly one block of code executes — either the `if` block or the `else` block.

### Syntax

```python
if condition:
    # executed when condition is True
    statements_if
else:
    # executed when condition is False
    statements_else
```

### Example: Even or Odd Number Check

```python
number = 17

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Output: 17 is odd
```

---

## 4. The `if-elif-else` Chain

When you need to check multiple conditions sequentially, use the `elif` (else-if) statement. Python evaluates conditions top-to-bottom and executes the first block whose condition is `True`.

### Syntax

```python
if condition1:
    # executed if condition1 is True
    statements1
elif condition2:
    # executed if condition1 is False and condition2 is True
    statements2
elif condition3:
    # executed if condition1 and condition2 are False, condition3 is True
    statements3
else:
    # executed if all conditions are False
    statements_else
```

### Key Characteristics

- You can use **zero or more** `elif` clauses
- The `else` clause is **optional**
- Only **one block** executes — the first `True` condition
- Once a condition is `True`, subsequent `elif` statements are **not evaluated**

### Example: Grade Classification System

```python
# Academic grade classification
score = 85

if score >= 90:
    grade = "O (Outstanding)"
elif score >= 80:
    grade = "A+ (Excellent)"
elif score >= 70:
    grade = "A (Very Good)"
elif score >= 60:
    grade = "B+ (Good)"
elif score >= 50:
    grade = "B (Above Average)"
else:
    grade = "F (Fail)"

print(f"Grade: {grade}")
# Output: Grade: A+ (Excellent)
```

### Example: Traffic Light Simulation

```python
# Traffic light control system
signal = "yellow"

if signal == "red":
    print("STOP! Vehicles must stop.")
elif signal == "yellow":
    print("CAUTION! Prepare to stop if safe.")
elif signal == "green":
    print("GO! Vehicles can proceed.")
else:
    print("Invalid signal!")

# Output: CAUTION! Prepare to stop if safe.
```

---

## 5. Nested Conditionals

You can place one conditional statement inside another. This is called **nesting**. While useful, excessive nesting can make code harder to read.

### Syntax

```python
if outer_condition:
    # outer block
    if inner_condition:
        # inner block (both conditions True)
        inner_statements
    else:
        # inner block (outer True, inner False)
        inner_else_statements
else:
    # outer block (outer condition False)
    else_statements
```

### Example: Eligibility Checker

```python
# Check eligibility for a scholarship program
age = 20
income = 150000
cgpa = 8.5

if age >= 18:
    if income < 200000:
        if cgpa >= 8.0:
            print("Eligible for scholarship!")
        else:
            print("CGPA requirement not met (need ≥ 8.0)")
    else:
        print("Income exceeds threshold")
else:
    print("Age requirement not met (need ≥ 18)")

# Output: Eligible for scholarship!
```

### Refactored Version (Using Logical Operators)

The above nested condition can be simplified using logical operators (explained in Section 6):

```python
if age >= 18 and income < 200000 and cgpa >= 8.0:
    print("Eligible for scholarship!")
```

---

## 6. Logical Operators

Python provides three logical operators to combine or negate boolean conditions:

| Operator | Description | Truth Table |
|----------|-------------|-------------|
| `and` | Returns `True` if **both** conditions are True | `True and True = True`, otherwise `False` |
| `or` | Returns `True` if **at least one** condition is True | `False or False = False`, otherwise `True` |
| `not` | Returns the **inverse** boolean value | `not True = False`, `not False = True` |

### The `and` Operator

```python
# Check if a number is between 1 and 100 (inclusive)
number = 50

if number >= 1 and number <= 100:
    print(f"{number} is between 1 and 100")
else:
    print(f"{number} is outside the range 1-100")

# Output: 50 is between 1 and 100
```

### The `or` Operator

```python
# Check if a character is a vowel
char = 'u'

if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print(f"'{char}' is a vowel")
else:
    print(f"'{char}' is a consonant")

# Output: 'u' is a vowel
```

### The `not` Operator

```python
# Check if a user is NOT logged in
is_logged_in = False

if not is_logged_in:
    print("Please log in to continue")
else:
    print("Welcome back!")

# Output: Please log in to continue
```

### Short-Circuit Evaluation

Python optimizes logical operations using short-circuit evaluation:

- `and`: If the first operand is `False`, the second operand is **not evaluated** (result is `False`)
- `or`: If the first operand is `True`, the second operand is **not evaluated** (result is `True`)

```python
# Demonstration of short-circuit
x = 5

# Second condition not checked because first is False
result = (x < 0) and (10 / x > 2)  # Safe: doesn't cause ZeroDivisionError

print(result)  # Output: False
```

---

## 7. Truthy and Falsy Values

In Python, not just `True` and `False` are evaluated in conditions. **Every object** has an inherent boolean value — this is called "truthiness."

### Falsy Values (Evaluate to `False`)

The following values are considered `False` in a boolean context:

- `None`
- `False`
- Zero: `0`, `0.0`, `0j`
- Empty sequences: `''` (empty string), `[]` (empty list), `()` (empty tuple), `{}` (empty dict)
- Objects with `__len__()` returning 0

### Truthy Values (Evaluate to `True`)

Everything else is truthy, including:

- Non-zero numbers (including negative numbers)
- Non-empty strings, lists, tuples, dictionaries
- `True`
- Custom objects

### Practical Examples

```python
# Example 1: Checking non-empty strings
username = "student123"

if username:
    print(f"Welcome, {username}!")
else:
    print("Please enter a username")

# Output: Welcome, student123!
```

```python
# Example 2: Checking empty lists
shopping_cart = []

if shopping_cart:
    print(f"Items in cart: {len(shopping_cart)}")
else:
    print("Your cart is empty")

# Output: Your cart is empty
```

```python
# Example 3: Using default values
def greet(name):
    # If name is empty string, use "Guest"
    if not name:
        name = "Guest"
    return f"Hello, {name}!"

print(greet(""))        # Output: Hello, Guest!
print(greet("Amit"))    # Output: Hello, Amit!
```

```python
# Example 4: Zero as falsy in financial applications
balance = 0

if balance:
    print(f"Account balance: ₹{balance}")
else:
    print("Insufficient funds / Account empty")

# Output: Insufficient funds / Account empty
```

### Best Practice Note

While truthy/falsy values make code concise, they can reduce readability. For clarity, especially in educational contexts, prefer explicit comparisons:

```python
# Less clear (but valid)
if items:
    process(items)

# More explicit (recommended for clarity)
if len(items) > 0:
    process(items)
```

---

## 8. Match Statements (Python 3.10+)

Introduced in Python 3.10, the `match` statement provides pattern matching functionality similar to switch-case statements in other languages, but with much greater power.

### Syntax

```python
match subject:
    case pattern1:
        # statements
    case pattern2:
        # statements
    case _:
        # default case (wildcard)
```

### Key Features

- The `_` pattern acts as a **wildcard** (matches anything) — similar to `default` in other languages
- Patterns can include **literal values**, **variables**, **wildcards**, **or-patterns**, and **guards**
- Patterns are checked top-to-bottom; first match wins

### Example 1: Simple Pattern Matching

```python
# HTTP status code handler
status_code = 404

match status_code:
    case 200:
        print("OK - Success")
    case 201:
        print("Created - Resource successfully created")
    case 400:
        print("Bad Request")
    case 401:
        print("Unauthorized")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown status code")

# Output: Not Found
```

### Example 2: Using OR Patterns

```python
# Weekend/weekday classifier
day = "Saturday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Invalid day")

# Output: Weekend
```

### Example 3: Pattern Matching with Guards

```python
# Grade evaluation with guards (additional if conditions)
score = 85

match score:
    case n if n >= 90:
        print("Grade: O (Outstanding)")
    case n if n >= 80:
        print("Grade: A+ (Excellent)")
    case n if n >= 70:
        print("Grade: A (Very Good)")
    case n if n >= 60:
        print("Grade: B+ (Good)")
    case n if n >= 50:
        print("Grade: B (Above Average)")
    case _:
        print("Grade: F (Fail)")

# Output: Grade: A+ (Excellent)
```

### Example 4: Pattern Matching with Data Structures

```python
# Processing geometric shapes
shape = {"type": "circle", "radius": 5}

match shape:
    case {"type": "circle", "radius": r}:
        print(f"Circle with area: {3.14159 * r ** 2}")
    case {"type": "rectangle", "width": w, "height": h}:
        print(f"Rectangle with area: {w * h}")
    case {"type": "triangle", "base": b, "height": h}:
        print(f"Triangle with area: {0.5 * b * h}")
    case _:
        print("Unknown shape")

# Output: Circle with area: 78.53975
```

### When to Use Match vs If-elif-else

| Scenario | Recommended Approach |
|----------|---------------------|
| Few conditions (1-3) | `if-elif-else` is simpler |
| Multiple conditions with complex patterns | `match` statement |
| Checking against exact values | `match` |
| Range checks or complex boolean logic | `if-elif-else` |
| Data structure pattern matching | `match` |

---

## 9. Practical Examples

### Example A: ATM Simulation System

```python
# Simplified ATM transaction system
print("=== Welcome to Delhi University ATM ===")

balance = 5000
pin = 1234

entered_pin = int(input("Enter your 4-digit PIN: "))

if entered_pin == pin:
    print("\nSelect transaction type:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    
    choice = input("Enter choice (1/2/3): ")
    
    if choice == "1":
        print(f"\nYour current balance is: ₹{balance}")
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            if amount > 0:
                balance -= amount
                print(f"\nPlease collect your cash: ₹{amount}")
                print(f"Remaining balance: ₹{balance}")
            else:
                print("\nError: Amount must be positive")
        else:
            print("\nError: Insufficient balance")
    elif choice == "3":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"\nAmount deposited successfully!")
            print(f"New balance: ₹{balance}")
        else:
            print("\nError: Amount must be positive")
    else:
        print("\nInvalid choice")
else:
    print("\nError: Incorrect PIN")
```

### Example B: Student Result Processing

```python
# Calculate final grade with internal assessments
print("=== Student Grade Calculator ===")

# Input marks
theory_marks = float(input("Enter theory marks (0-70): "))
internal_marks = float(input("Enter internal assessment marks (0-30): "))

# Validate inputs
if theory_marks < 0 or theory_marks > 70:
    print("Error: Theory marks should be between 0 and 70")
elif internal_marks < 0 or internal_marks > 30:
    print("Error: Internal marks should be between 0 and 30")
else:
    total_marks = theory_marks + internal_marks
    
    # Determine grade using match statement
    match True:
        case _ if total_marks >= 90:
            grade = "O"
            remark = "Outstanding performance!"
        case _ if total_marks >= 75:
            grade = "A"
            remark = "Excellent work!"
        case _ if total_marks >= 60:
            grade = "B"
            remark = "Good effort!"
        case _ if total_marks >= 50:
            grade = "C"
            remark = "Satisfactory."
        case _ if total_marks >= 45:
            grade = "P"
            remark = "Pass - needs improvement."
        case _:
            grade = "F"
            remark = "Fail - better luck next time."
    
    print(f"\nTotal Marks: {total_marks}/100")
    print(f"Grade: {grade}")
    print(f"Remark: {remark}")
```

---

## 10. Common Pitfalls and Best Practices

### Pitfalls to Avoid

1. **Forgetting the Colon**
   ```python
   # Wrong
   if x > 0
       print("Positive")
   
   # Correct
   if x > 0:
       print("Positive")
   ```

2. **Incorrect Indentation**
   ```python
   # Wrong - inconsistent indentation
   if x > 0:
   print("Positive")  # Error!
   
   # Correct
   if x > 0:
       print("Positive")
   ```

3. **Using `=` Instead of `==`**
   ```python
   # Wrong - assignment instead of comparison
   if x = 5:  # SyntaxError!
   
   # Correct - comparison
   if x == 5:
       print("x is 5")
   ```

4. **Not Handling All Cases**
   ```python
   # Problem: What if signal has unexpected value?
   if signal == "red":
       print("Stop")
   elif signal == "green":
       print("Go")
   # No else - unexpected values silently pass
   
   # Better: Always handle edge cases
   if signal == "red":
       print("Stop")
   elif signal == "green":
       print("Go")
   else:
       print("Invalid signal")
   ```

### Best Practices

1. **Use Descriptive Variable Names**
   ```python
   # Poor
   if x > 18:
       print("Adult")
   
   # Better
   age = 20
   if age >= 18:
       print("Adult")
   ```

2. **Keep Conditions Simple**
   ```python
   # Complex - hard to read
   if (a > b and c > d) or (e == f and g != h) or (i < j):
       # complex logic
   
   # Better - break into named variables
   condition1 = a > b and c > d
   condition2 = e == f and g != h
   condition3 = i < j
   
   if condition1 or condition2 or condition3:
       # clearer logic
   ```

3. **Use Match for Multiple Fixed Values**
   Match statements are more readable when checking against many values.

4. **Comment Complex Conditions**
   ```python
   # Check if student is eligible for scholarship
   # Criteria: CGPA >= 8.0 AND (Family income < 2L OR Is Orphan)
   if cgpa >= 8.0 and (income < 200000 or is_orphan):
       print("Eligible for scholarship")
   ```

---

## 11. Key Takeaways

1. **Conditional statements** allow programs to make decisions based on conditions.

2. **`if` statement** executes code only when the condition is `True`.

3. **`if-else`** provides two paths: one for `True`, one for `False`.

4. **`if-elif-else`** chains handle multiple conditions sequentially; only the first `True` condition executes.

5. **Nested conditionals** place conditionals inside other conditionals, useful for complex decision trees (use sparingly).

6. **Logical operators** (`and`, `or`, `not`) combine or negate boolean expressions:
   - `and`: Both must be `True`
   - `or`: At least one must be `True`
   - `not`: Inverts the boolean value

7. **Truthy/Falsy values**: In Python, many non-boolean values evaluate to `True` or `False` in conditions (e.g., `0`, `""`, `[]` are falsy).

8. **`match` statement** (Python 3.10+) provides powerful pattern matching, replacing complex if-elif chains for value-based selection.

9. **Always use proper indentation** — Python relies on indentation to define code blocks.

10. **Avoid common mistakes**: forgetting colons, using `=` instead of `==`, not handling edge cases.

---

## 12. Multiple Choice Questions (MCQs)

### Question 1
What will be the output of the following code?

```python
x = 10
if x > 5:
    print("A")
elif x > 8:
    print("B")
elif x > 10:
    print("C")
```

A) A  
B) B  
C) A B  
D) A B C

**Answer: A** — Once `x > 5` evaluates to `True` and prints "A", subsequent `elif` statements are not evaluated.

---

### Question 2
Which of the following is a **falsy** value in Python?

A) `"0"`  
B) `[0]`  
C) `0.0`  
D) `"False"`

**Answer: C** — The integer `0` and float `0.0` are falsy. String `"0"` and list `[0]` are truthy (non-empty).

---

### Question 3
What does the `or` operator return if the first operand is `True`?

A) `False`  
B) `True`  
C) The first operand value  
D) The second operand value

**Answer: B** — Due to short-circuit evaluation, `or` returns `True` immediately if the first operand is `True`, without evaluating the second operand.

---

### Question 4
In a Python `match` statement, what does the pattern `_` represent?

A) A variable named underscore  
B) A wildcard that matches anything  
C) An error  
D) A break statement

**Answer: B** — The underscore `_` is a wildcard pattern that matches any value (like `default` in switch-case).

---

### Question 5
What is the output?

```python
result = "hello" and "world"
print(result)
```

A) `True`  
B) `False`  
C) `"world"`  
D) `"hello"`

**Answer: C** — The `and` operator returns the last evaluated value. Since both are truthy, it returns `"world"`.

---

### Question 6
Which logical operator has **short-circuit evaluation**?

A) Only `and`  
B) Only `or`  
C) Both `and` and `or`  
D) None

**Answer: C** — Both `and` and `or` use short-circuit evaluation to optimize performance.

---

### Question 7
What will be printed?

```python
x = 5
if x:
    print("Truthy")
else:
    print("Falsy")
```

A) Falsy  
B) Truthy  
C) Error  
D) None

**Answer: B** — Non-zero integers are truthy, so `x` evaluates to `True`.

---

### Question 8
In Python, which statement is used for pattern matching (Python 3.10+)?

A) `switch`  
B) `case`  
C) `match`  
D) `select`

**Answer: C** — Python 3.10 introduced the `match` statement for pattern matching.

---

## 13. Flashcards for Quick Review

| Term | Definition |
|------|------------|
| **Conditional Statement** | A statement that executes code based on whether a condition is True or False |
| **if-elif-else Chain** | Sequential conditional checks; executes the first block where the condition is True |
| **Nested Conditional** | An if/elif/else statement placed inside another conditional block |
| **Logical AND** | Operator that returns True only if both operands are True |
| **Logical OR** | Operator that returns True if at least one operand is True |
| **Logical NOT** | Operator that inverts the boolean value (True → False, False → True) |
| **Falsy Value** | A value that evaluates to False in a boolean context (e.g., 0, "", [], None) |
| **Truthy Value** | A value that evaluates to True in a boolean context (e.g., non-zero numbers, non-empty strings) |
| **Short-Circuit Evaluation** | Optimization where the second operand is not evaluated if the result is already determined |
| **Match Statement** | Python 3.10+ feature for pattern matching, similar to switch-case in other languages |
| **Wildcard Pattern** | In match statements, `_` matches any value (acts like default) |
| **Guard** | An additional `if` condition in a match case pattern |

---

## References and Further Reading

1. **Official Python Documentation**: https://docs.python.org/3/tutorial/controlflow.html
2. **Python Enhancement Proposal (PEP) 622**: Structural Pattern Matching — https://peps.python.org/pep-0622/
3. Delhi University B.Sc. (Hons) Computer Science Syllabus — NEP 2024 UGCF

---

*Generated for BSc (Hons) Computer Science — Delhi University, NEP 2024 UGCF*