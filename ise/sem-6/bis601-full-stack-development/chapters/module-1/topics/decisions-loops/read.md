# **Decisions & Loops**

### Introduction

Decisions and loops are fundamental concepts in programming that allow your code to execute different blocks of instructions based on conditions or repeat a set of instructions for each item in a collection.

### Decisions

**What is a Decision?**

A decision is a condition that determines the flow of your program's execution. It's a way to evaluate a condition and execute one block of code if the condition is true and another block of code if it's false.

**Types of Decisions**

- **Simple Decision**: Evaluates a single condition and executes one block of code if true and another block of code if false.
- **Nested Decision**: Evaluates a condition within another condition.

**Decision Statements**

- **If Statement**: Used to execute a block of code if a condition is true.
- **If-Else Statement**: Used to execute one block of code if a condition is true and another block of code if the condition is false.

### Example Code

```javascript
// If Statement
let num = 5;
if (num > 10) {
  console.log('Number is greater than 10');
} else {
  console.log('Number is less than or equal to 10');
}

// If-Else Statement
let num = 5;
if (num > 10) {
  console.log('Number is greater than 10');
} else {
  if (num === 5) {
    console.log('Number is equal to 5');
  } else {
    console.log('Number is less than 5');
  }
}
```

### Loops

**What is a Loop?**

A loop is a control structure that repeats a set of instructions for each item in a collection.

**Types of Loops**

- **For Loop**: Used to execute a block of code for each item in an array.
- **While Loop**: Used to execute a block of code as long as a condition is true.
- **Do-While Loop**: Used to execute a block of code at least once and then repeat it as long as a condition is true.

### Example Code

```javascript
// For Loop
let numbers = [1, 2, 3, 4, 5];
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}

// While Loop
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}

// Do-While Loop
let i = 0;
do {
  console.log(i);
  i++;
} while (i < 5);
```

### Key Concepts

- **Boolean Values**: True and False
- **Conditional Operators**: &&, ||, !
- **Logical Operators**: &&, ||, !

### Practice Exercises

1. Write a program that asks the user for their age and then prints out a message based on whether they are eligible to vote or not.
2. Write a program that prints out the numbers from 1 to 10 using a for loop.
3. Write a program that asks the user for a number and then prints out a message based on whether the number is even or odd.

### Conclusion

Decisions and loops are fundamental concepts in programming that allow your code to execute different blocks of instructions based on conditions or repeat a set of instructions for each item in a collection. Understanding these concepts is crucial for writing efficient and effective code.
