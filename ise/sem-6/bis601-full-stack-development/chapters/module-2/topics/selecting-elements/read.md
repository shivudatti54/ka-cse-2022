# Module 2: Full Stack Development - Selecting Elements

## Introduction

In the world of web development, the Document Object Model (DOM) is a programming interface that represents the structure of an HTML or XML document as a tree of objects. To dynamically manipulate a webpage—be it changing content, style, or responding to user interactions—you first need to _select_ the specific elements you want to work with. This process of pinpointing one or more elements in the DOM is the foundational step in client-side scripting, primarily using JavaScript. This module covers the core methods and best practices for selecting elements efficiently.

## Core Concepts and Methods

JavaScript provides several built-in methods on the `document` object to query and select elements. These methods can be broadly categorized into those that return a single element and those that return a collection (specifically, a `NodeList`) of multiple elements.

### 1. Selecting a Single Element

#### `document.getElementById()`

This is the most direct and fastest method for selecting an element if it has a unique `id` attribute.

- **Syntax:** `document.getElementById(idString)`
- **Returns:** A single `Element` object if found, otherwise `null`.
- **Example:**
