# Read a String from the User

## FULL STACK DEVELOPMENT

### MongoDB: Basics, Documents, Collections, Databases, Query Language, Installation, The Mongo Shell

#### Key Points

- To read a string from the user in MongoDB, you can use the `getLine()` method in the mongo shell.
- The `getLine()` method reads a single line of input from the user and returns it as a string.
- You can also use the `getline()` method in Node.js to read a string from the user.
- The `getline()` method is part of the `readline` module in Node.js and returns a string when invoked.
- To use the `getline()` method, you need to create a new instance of the `readline.createInterface()` function and pass it to the method.
- The `getline()` method will block until the user enters a string and presses enter.

#### Important Formulas, Definitions, Theorems

- None relevant to this topic

#### Revision Notes

- To read a string from the user in MongoDB, use the `getLine()` method.
- To read a string from the user in Node.js, use the `getline()` method and the `readline` module.
- Always handle the case where the user enters nothing or an empty string.

#### Example Code

- In the mongo shell:

```javascript
var line = db.getLine();
print(line);
```

- In Node.js:

```javascript
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question('Enter a string: ', (line) => {
  console.log(line);
  rl.close();
});
```
