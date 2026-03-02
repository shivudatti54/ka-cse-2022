# Introducing Methods, Constructors, The `this` Keyword, and Garbage Collection

=====================================================

### Class Fundamentals

---

- **Constructor**: A special method in a class that is called when an object is created. Initializes the state of the object.
  - Syntax: `public Type thisName(Type... params) { ... }`
  - Example: `public Person(String name, int age) { this.name = name; this.age = age; }`
- **Methods**: Reusable blocks of code that perform specific tasks.
  - Syntax: `public returnType methodName(Type... params) { ... }`
  - Example: `public int calculateArea(int length, int width) { return length * width; }`
- **`this` Keyword**: Used to access variables and methods from the same class.
  - Syntax: `this.variableName` or `this.methodName()`
  - Example: `this.name = name;`
- **Static Variables and Methods**: Shared by all instances of a class.
  - Syntax: `public static variableName` or `public static returnType methodName(Type... params)`
  - Example: `public static int counter = 0;`

### Garbage Collection

---

- **Definition**: A mechanism that automatically frees up memory occupied by objects that are no longer referenced.
- **Theorem**: Mark-and-Sweep Algorithm:
  - Mark Phase: Identify all reachable objects.
  - Sweep Phase: Free up memory occupied by unreachable objects.
- **GC Cycle**: The process of identifying and freeing up unreachable objects.

### Important Formulas and Definitions

---

- **Object Reference Variables**: Variables that hold references to objects.
  - Syntax: `Object obj;`
  - Example: `Person person; person = new Person("John", 30);`
- **Class Hash Code**: A unique integer value that represents an object.
  - Syntax: `hash code = obj.hashCode();`

### Quick Revision Tips

---

- Familiarize yourself with constructor and method syntax.
- Remember the purpose of the `this` keyword.
- Understand the concept of static variables and methods.
- Know the basics of garbage collection and the mark-and-sweep algorithm.

By reviewing these key points, you'll be well-prepared for your Object-Oriented Programming exams in Java.
