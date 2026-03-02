# **Methods & Objects**

## **Introduction**

In JavaScript, methods and objects are fundamental concepts that enable you to create reusable code, organize data, and interact with objects. In this study material, we will explore the basics of methods and objects, including their definitions, types, and usage.

## **Definitions**

### Methods

A method is a block of code that is executed in response to a specific event or action. It is a function that belongs to an object and is used to perform a specific action or operation.

### Objects

An object is a collection of key-value pairs that represent data. It is a blueprint or template that defines the structure and properties of an object. Objects can have methods, properties, and relationships with other objects.

## **Types of Methods**

### Instance Methods

Instance methods are methods that belong to an object and are used to perform actions on that object. They have access to the object's properties and can modify them.

### Static Methods

Static methods are methods that belong to a class and are used to perform actions on a class or its instances. They do not have access to the object's properties and cannot modify them.

### Constructor Methods

Constructor methods are methods that are called when an object is created. They are used to initialize the object's properties and set up its state.

## **Types of Objects**

### Primitive Object

A primitive object is a basic object that represents a single value, such as a number, string, or boolean.

### Reference Object

A reference object is an object that contains other objects as its properties.

### Built-in Object

A built-in object is an object that is part of the JavaScript language, such as the Math object or the String object.

## **Creating Objects**

### Object Declaration

Objects can be declared using the `let`, `const`, or `var` keywords.

```javascript
let person = {
  name: 'John Doe',
  age: 30,
};
```

### Object Literal

Object literals are used to create objects using the object declaration syntax.

```javascript
const person = {
  name: 'John Doe',
  age: 30,
};
```

### Object Constructor

Object constructors are used to create objects using the `new` keyword.

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
}

let person = new Person('John Doe', 30);
```

## **Methods in Objects**

### Accessing Methods

Methods can be accessed using the dot notation or the bracket notation.

```javascript
let person = {
  sayHello: function () {
    console.log('Hello!');
  },
};

person.sayHello(); // Output: Hello!

person['sayHello'](); // Output: Hello!
```

### Calling Methods

Methods can be called using the dot notation or the bracket notation.

```javascript
let person = {
  sayHello: function () {
    console.log('Hello!');
  },
};

person.sayHello(); // Output: Hello!

person['sayHello'](); // Output: Hello!
```

### Passing Arguments

Methods can pass arguments to other methods or functions.

```javascript
function greet(name) {
  console.log(`Hello, ${name}!`);
}

function sayGoodbye(name) {
  greet(name);
  console.log(`Goodbye, ${name}!`);
}

sayGoodbye('John Doe');
```

## **Example Use Cases**

### Creating a Person Object

```javascript
let person = {
  name: 'John Doe',
  age: 30,
  sayHello: function () {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  },
  sayGoodbye: function () {
    console.log('Goodbye!');
  },
};

person.sayHello(); // Output: Hello, my name is John Doe and I am 30 years old.
person.sayGoodbye(); // Output: Goodbye!
```

### Creating an Employee Object

```javascript
let employee = {
  name: 'Jane Doe',
  age: 25,
  salary: 50000,
  sayHello: function () {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  },
  getSalary: function () {
    return this.salary;
  },
};

employee.sayHello(); // Output: Hello, my name is Jane Doe and I am 25 years old.
console.log(employee.getSalary()); // Output: 50000
```
