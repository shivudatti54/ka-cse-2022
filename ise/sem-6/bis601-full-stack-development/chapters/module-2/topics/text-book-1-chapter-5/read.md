# **Text Book 1: Chapter 5 - Document Object Model: DOM Manipulation, Selecting Elements, Working with DOM Nodes, Updating**

## **1. Introduction**

In this chapter, we will delve into the world of Document Object Model (DOM) manipulation, selection, and updating. The DOM is a representation of a document as a tree-like structure, where each node represents an element in the document. Understanding how to manipulate and update the DOM is crucial for any web development project.

## **2. DOM Structure**

The DOM is composed of several key elements:

- **Document Object**: The root of the DOM tree, representing the entire document.
- **Node**: A generic term for any element in the DOM tree, including elements, attributes, and text nodes.
- **Element**: A node that represents an HTML element, such as a `<div>`, `<p>`, or `<img>`.
- **Attribute**: A property of an element that provides additional information, such as the `src` attribute of an `<img>` element.
- **Text Node**: A node that represents the text content of an element.

## **3. DOM Manipulation**

DOM manipulation involves modifying the structure and content of a document. The most common methods for DOM manipulation are:

### Methods for Manipulating Elements

| Method            | Description                                        |
| ----------------- | -------------------------------------------------- |
| `createElement()` | Creates a new element with the specified tag name. |
| `appendChild()`   | Adds a new element to the end of the DOM tree.     |
| `insertBefore()`  | Inserts a new element before the specified node.   |
| `removeChild()`   | Removes the specified node from the DOM tree.      |
| `replaceChild()`  | Replaces the specified node with a new element.    |

### Methods for Updating Element Properties

| Method           | Description                                        |
| ---------------- | -------------------------------------------------- |
| `setAttribute()` | Sets the value of an attribute on an element.      |
| `getAttribute()` | Retrieves the value of an attribute on an element. |
| `setStyle()`     | Sets the style property of an element.             |
| `getStyle()`     | Retrieves the style property of an element.        |

### Methods for Updating Text Content

| Method             | Description                                  |
| ------------------ | -------------------------------------------- |
| `nodeValue`        | Gets or sets the text content of an element. |
| `setTextContent()` | Sets the text content of an element.         |

## **4. Selecting Elements**

Selecting elements is the process of identifying specific elements in the DOM tree. There are several methods for selecting elements:

### Methods for Selecting Elements by Tag Name

| Method                        | Description                                            |
| ----------------------------- | ------------------------------------------------------ |
| `document.querySelector()`    | Selects the first element with the specified tag name. |
| `document.querySelectorAll()` | Selects all elements with the specified tag name.      |

### Methods for Selecting Elements by Class

| Method                              | Description                                              |
| ----------------------------------- | -------------------------------------------------------- |
| `document.getElementsByClassName()` | Selects all elements with the specified class name.      |
| `document.querySelector()`          | Selects the first element with the specified class name. |
| `document.querySelectorAll()`       | Selects all elements with the specified class name.      |

## **5. Working with DOM Nodes**

DOM nodes are the building blocks of the DOM tree. There are several types of DOM nodes:

- **Element Node**: Represents an HTML element.
- **Attribute Node**: Represents an attribute of an element.
- **Text Node**: Represents the text content of an element.
- **Comment Node**: Represents a comment in the document.

## **6. Updating the DOM**

Updating the DOM involves modifying the structure and content of a document. There are several methods for updating the DOM:

### Methods for Updating Element Properties

| Method        | Description                                    |
| ------------- | ---------------------------------------------- |
| `innerHTML`   | Gets or sets the HTML content of an element.   |
| `textContent` | Gets or sets the text content of an element.   |
| `style`       | Gets or sets the style property of an element. |

### Methods for Updating Text Content

| Method           | Description                                            |
| ---------------- | ------------------------------------------------------ |
| `appendChild()`  | Adds a new text node to the end of the DOM tree.       |
| `insertBefore()` | Inserts a new text node before the specified node.     |
| `removeChild()`  | Removes the specified text node from the DOM tree.     |
| `replaceChild()` | Replaces the specified text node with a new text node. |

### Example Use Case

```html
<!-- Create a new HTML document -->
<!DOCTYPE html>
<html>
  <head>
    <title>DOM Manipulation</title>
  </head>
  <body>
    <h1 id="title">Welcome to my page</h1>
    <p id="paragraph">This is a paragraph of text.</p>

    <!-- Select the title element -->
    <script>
      const title = document.getElementById('title');
      title.style.color = 'red';
      title.textContent = 'Hello World';
    </script>
  </body>
</html>
```

This example demonstrates how to select an element, update its properties, and update its text content using the DOM API.
