# **Text Book 1: Chapter 2**

## **Basic JavaScript Instructions, Statements, Comments**

In this chapter, we will learn about the basic instructions, statements, and comments in JavaScript.

### What are Instructions?

In JavaScript, an instruction is a single statement that performs a specific task. Instructions are used to write JavaScript code that can be executed by the browser or a Node.js environment.

### Types of Instructions

There are several types of instructions in JavaScript:

- **Arithmetic Instructions**: These instructions perform mathematical operations such as addition, subtraction, multiplication, and division.
- **Assignment Instructions**: These instructions assign a value to a variable.
- **Comparison Instructions**: These instructions compare two values and return a boolean result.
- **Logical Instructions**: These instructions perform logical operations such as AND, OR, and NOT.

### Examples of Instructions

```javascript
// Arithmetic Instruction: Addition
let x = 5;
let y = 3;
let result = x + y;
console.log(result); // Output: 8

// Assignment Instruction: Assigning a value to a variable
x = 10;
console.log(x); // Output: 10

// Comparison Instruction: Comparing two values
let a = 5;
let b = 10;
if (a > b) {
  console.log('a is greater than b');
} else {
  console.log('a is less than or equal to b');
}

// Logical Instruction: Logical AND
let c = true;
let d = false;
let result = c && d;
console.log(result); // Output: false
```

### Statements

A statement in JavaScript is a group of instructions that perform a single task. Statements are used to write JavaScript code that can be executed by the browser or a Node.js environment.

### Types of Statements

There are several types of statements in JavaScript:

- **Expression Statements**: These statements evaluate an expression and return a value.
- **Statement Statements**: These statements do not evaluate an expression and do not return a value.

### Examples of Statements

```javascript
// Expression Statement: Evaluating an expression
let x = 5;
let y = 3;
let result = x + y;
console.log(result); // Output: 8

// Statement Statement: Not evaluating an expression
if (x > 5) {
  console.log('x is greater than 5');
}
```

### Comments

Comments in JavaScript are used to add notes to the code. Comments are ignored by the browser or a Node.js environment and are used for debugging and maintenance purposes.

### Types of Comments

There are two types of comments in JavaScript:

- **Single-Line Comments**: These comments are preceded by a `//` symbol and are used to add notes to a single line of code.
- **Multi-Line Comments**: These comments are preceded by `/*` symbols and are used to add notes to multiple lines of code.

### Examples of Comments

```javascript
// Single-Line Comment
let x = 5;
// This is a note about the variable x

/* Multi-Line Comment
This is a note about the code that follows
This comment spans multiple lines of code
*/
let y = 10;
```

### Variables and Data Types

---

In this chapter, we will learn about variables and data types in JavaScript.

### Variables

A variable in JavaScript is a name given to a value. Variables are used to store and manipulate data in a program.

### Types of Variables

There are several types of variables in JavaScript:

- **String Variables**: These variables store string values.
- **Number Variables**: These variables store number values.
- **Boolean Variables**: These variables store boolean values.
- **Array Variables**: These variables store array values.

### Examples of Variables

```javascript
// String Variable
let name = 'John Doe';
console.log(name); // Output: John Doe

// Number Variable
let age = 30;
console.log(age); // Output: 30

// Boolean Variable
let isAdmin = true;
console.log(isAdmin); // Output: true

// Array Variable
let colors = ['red', 'green', 'blue'];
console.log(colors); // Output: ["red", "green", "blue"]
```

### Data Types

In JavaScript, data types refer to the type of value that a variable or expression can hold. Data types are used to classify the type of data that a variable or expression can hold.

### Types of Data Types

There are several types of data types in JavaScript:

- **Primitive Data Types**: These data types include string, number, boolean, null, and undefined.
- **Reference Data Types**: These data types include arrays, objects, and functions.

### Examples of Data Types

```javascript
// Primitive Data Type: String
let str = 'Hello World';
console.log(typeof str); // Output: string

// Primitive Data Type: Number
let num = 10;
console.log(typeof num); // Output: number

// Primitive Data Type: Boolean
let bool = true;
console.log(typeof bool); // Output: boolean

// Reference Data Type: Array
let arr = [1, 2, 3];
console.log(typeof arr); // Output: object

// Reference Data Type: Object
let obj = { name: 'John Doe', age: 30 };
console.log(typeof obj); // Output: object
```

### Arrays and Strings

---

In this section, we will learn about arrays and strings in JavaScript.

### Arrays

An array in JavaScript is a collection of values that can be of any data type, including strings, numbers, booleans, and other arrays.

### Creating Arrays

Arrays can be created using the `[]` syntax.

```javascript
// Creating an array
let colors = ['red', 'green', 'blue'];
console.log(colors); // Output: ["red", "green", "blue"]
```

### Accessing Array Elements

Array elements can be accessed using the index syntax.

```javascript
// Accessing an array element
let colors = ['red', 'green', 'blue'];
console.log(colors[0]); // Output: "red"
```

### Modifying Array Elements

Array elements can be modified using the assignment syntax.

```javascript
// Modifying an array element
let colors = ['red', 'green', 'blue'];
colors[0] = 'yellow';
console.log(colors); // Output: ["yellow", "green", "blue"]
```

### Strings

A string in JavaScript is a sequence of characters that can be used to represent text.

### Creating Strings

Strings can be created using the `""` syntax.

```javascript
// Creating a string
let name = 'John Doe';
console.log(name); // Output: "John Doe"
```

### Concatenating Strings

Strings can be concatenated using the `+` operator.

```javascript
// Concatenating strings
let name = 'John Doe';
let age = 30;
console.log(name + ' is ' + age + ' years old'); // Output: "John Doe is 30 years old"
```

### String Methods

---

Strings have several methods that can be used to manipulate strings.

### Examples of String Methods

```javascript
// ToUpperCase()
let str = 'hello world';
console.log(str.toUpperCase()); // Output: "HELLO WORLD"

// ToLowerCase()
let str = 'HELLO WORLD';
console.log(str.toLowerCase()); // Output: "hello world"

// Split()
let str = 'hello,world';
let array = str.split(',');
console.log(array); // Output: ["hello", "world"]

// Join()
let array = ['hello', 'world'];
let str = array.join(',');
console.log(str); // Output: "hello,world"
```
