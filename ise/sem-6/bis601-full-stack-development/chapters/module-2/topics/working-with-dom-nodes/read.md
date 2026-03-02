# Working with DOM Nodes in Full Stack Development

## Introduction

The Document Object Model (DOM) is a critical concept for any web developer. It is a programming interface that represents the structure of an HTML or XML document as a tree of objects, where each object corresponds to a part of the document. For front-end developers, the ability to interact with and manipulate these objects—known as **DOM Nodes**—is fundamental to creating dynamic, interactive web applications. This module focuses on understanding these nodes and how to work with them effectively using JavaScript.

## Core Concepts

### 1. What is a DOM Node?

Everything in the DOM is a node. The document itself is a node, every HTML element is an element node, the text inside an element is a text node, every attribute is an attribute node, and comments are comment nodes. This tree-like hierarchy of nodes allows developers to navigate, access, and modify the content, structure, and style of a document programmatically.

### 2. Types of Nodes

The most common node types you will work with are:

- **Element Node**: Represents an HTML tag (e.g., `<div>`, `<p>`, `<span>`).
- **Text Node**: Represents the textual content inside an element.
- **Attribute Node**: Represents an attribute of an element (e.g., `class="title"`).
- **Document Node**: The root node that represents the entire HTML document.

Each node has properties like `nodeType`, `nodeName`, and `nodeValue` to identify its type.

### 3. Accessing DOM Nodes (Selection)

Before you can manipulate a node, you must first select it. JavaScript provides several methods to find nodes in the DOM tree:

- `document.getElementById(id)`: Selects a single element by its `id` attribute.
- `document.getElementsByClassName(className)`: Selects a live collection of elements by their class name.
- `document.getElementsByTagName(tagName)`: Selects a live collection of elements by their tag name (e.g., `p`, `div`).
- `document.querySelector(cssSelector)`: Returns the **first** element that matches a given CSS selector.
- `document.querySelectorAll(cssSelector)`: Returns a static **NodeList** of all elements that match the CSS selector.

**Example:**
