# Module 2: Updating Element Content & Attributes in the DOM

## Introduction

In the previous module, you learned how to _select_ elements from the Document Object Model (DOM). The real power of JavaScript in web development lies in dynamically _manipulating_ those elements. This section focuses on two fundamental types of manipulation: changing the content inside an element and modifying its attributes. Mastering these techniques is crucial for creating interactive and responsive user interfaces, a core skill for any full-stack developer.

---

## Core Concepts & Methods

### 1. Updating Element Content

This involves changing the text or HTML structure within an element.

#### `textContent`

The `textContent` property gets or sets the _plain text_ content of a node and all its descendants. It is the safest way to insert text as it treats the input as raw text, not HTML. This prevents accidental HTML injection (a security risk known as XSS).

**Example:**
