# **Methods & Objects**

## **Introduction**

In JavaScript, methods and objects are two fundamental concepts that are used together to create complex data structures and functions. In this section, we will delve into the world of methods and objects, exploring their history, syntax, and usage.

## **What are Methods?**

A method is a function that is attached to an object. It is a way to perform an action on an object or its properties. Methods are used to encapsulate code that operates on an object's state, making it easier to manage complexity and modify code.

## **What are Objects?**

An object is a collection of properties (also known as keys or attributes) and methods that are bundled together. Objects are used to represent real-world entities, such as people, vehicles, or buildings. In JavaScript, objects are mutable, meaning their properties and methods can be modified after creation.

## **Historical Context**

The concept of methods and objects has its roots in object-oriented programming (OOP) languages like Smalltalk and C++. These languages introduced the idea of encapsulating data and behavior together, making it easier to manage complex systems.

In JavaScript, the concept of methods and objects was first introduced in the Netscape Navigator browser engine in the mid-1990s. The engine used a proprietary syntax for creating objects and methods, which eventually became the basis for modern JavaScript.

## **Modern Developments**

In modern JavaScript, methods and objects are used extensively in both front-end and back-end development. They are particularly useful for creating reusable code, encapsulating data, and improving code readability.

## **Syntax**

In JavaScript, methods and objects are created using the following syntax:

```javascript
const obj = {
  property1: 'value1',
  property2: 'value2',
  method1: function () {
    console.log('Hello World!');
  },
};
```

In this example, `obj` is an object with two properties (`property1` and `property2`) and one method (`method1`).

## **Types of Objects**

There are two types of objects in JavaScript:

1. **Literal Objects**: These are objects created using the syntax above.
2. **Prototype-Based Objects**: These are objects created using the prototype chain, which allows for inheritance and polymorphism.

## **Literal Objects**

Literal objects are created using the syntax above. They are the most common type of object in JavaScript.

## **Prototype-Based Objects**

Prototype-based objects are created using the `Object.create()` method or the `new` keyword. They are used for inheritance and polymorphism.

## **Methods**

Methods are functions that are attached to an object. They can be used to perform various actions on the object or its properties.

## **Types of Methods**

There are two types of methods in JavaScript:

1. **Instance Methods**: These are methods that are attached to an object instance.
2. **Static Methods**: These are methods that are attached to an object without a `this` reference.

## **Instance Methods**

Instance methods are methods that are attached to an object instance. They have access to the object's properties and can modify them.

## **Static Methods**

Static methods are methods that are attached to an object without a `this` reference. They do not have access to the object's properties and cannot modify them.

## **Example**

Here is an example of a simple object with an instance method and a static method:

```javascript
const Person = {
  name: 'John',
  age: 30,

  // Instance method
  sayHello() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  },

  // Static method
  static sayGoodbye() {
    console.log('Goodbye!');
  }
};

const person = new Person();
person.sayHello(); // Output: Hello, my name is John and I am 30 years old.
Person.sayGoodbye(); // Output: Goodbye!
```

## **Applications**

Methods and objects are used extensively in various applications, including:

1. **Front-end development**: Methods and objects are used to create reusable code and improve code readability.
2. **Back-end development**: Methods and objects are used to create service-oriented architecture and improve code organization.
3. **Game development**: Methods and objects are used to create game objects and behaviors.
4. **Desktop applications**: Methods and objects are used to create application objects and behaviors.

## **Case Study**

Here is a case study of a simple banking system that uses methods and objects:

```javascript
const BankAccount = {
  // Constructor
  constructor(accountNumber, balance) {
    this.accountNumber = accountNumber;
    this.balance = balance;
  },

  // Method to deposit money
  deposit(amount) {
    this.balance += amount;
    console.log(`Deposited ${amount}. New balance: ${this.balance}`);
  },

  // Method to withdraw money
  withdraw(amount) {
    if (this.balance >= amount) {
      this.balance -= amount;
      console.log(`Withdrew ${amount}. New balance: ${this.balance}`);
    } else {
      console.log('Insufficient balance.');
    }
  },
};

const account = new BankAccount('123456789', 1000);
account.deposit(500); // Output: Deposited 500. New balance: 1500
account.withdraw(200); // Output: Withdrew 200. New balance: 1300
```

## **Conclusion**

Methods and objects are a fundamental concept in JavaScript and are used extensively in various applications. They provide a way to encapsulate data and behavior together, making it easier to manage complexity and improve code readability.

## **Further Reading**

- [MDN Web Docs: Objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects)
- [ECMAScript 2015: Object Creation](https://www.ecma-international.org/ecma-262/6.0/#sec-object-creation)
- [JavaScript: The Good Parts](https://www.amazon.com/JavaScript-Good-Parts-David-Flanagan/dp/0596009208)
