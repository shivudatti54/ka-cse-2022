# Lexical Issues: Whitespace in Java

## Introduction

In Java, **lexical structure** refers to the set of basic rules that dictate how you write the language. Before the compiler can even begin to understand your logic, it must first break down your source code into recognizable chunks called **tokens** (keywords, identifiers, operators, etc.). This process is known as **lexical analysis**. A fundamental, yet often misunderstood, part of this process is the handling of **whitespace**. This module explains the role of whitespace in Java, clarifying what it is and how it is interpreted by the compiler.

## Core Concepts of Whitespace

Whitespace in Java refers to any combination of spaces, tabs, carriage returns, and form feeds. Unlike in languages like Python, whitespace in Java is **not syntactically significant**. This means the Java compiler generally ignores it. Its primary purpose is to separate tokens that would otherwise be merged into a single, unrecognizable token, making the code readable for humans.

### 1. The Separator Role

The most critical function of whitespace is to separate keywords, identifiers, and other tokens. Without it, the compiler cannot distinguish where one token ends and the next begins.

**Example:**