# Reading Dictionaries in UNIX System Programming

## Introduction

In UNIX system programming, a "dictionary" is not a language dictionary but a fundamental data structure: a collection of key-value pairs. It is often implemented using hash tables for efficient lookups. The term "reading a dictionary" in this context refers to the process of a program parsing and loading such a data structure from a persistent storage medium, most commonly a text file. Mastering this technique is crucial for building applications that rely on configuration files, data caches, or any form of structured, persistent data.

## Core Concepts

### 1. The Dictionary File Format

A typical dictionary file is a simple text file where each line represents a single key-value pair. The key and value are separated by a delimiter, such as a colon (`:`), equals sign (`=`), or a space. The choice of delimiter depends on the application's needs and the data being stored.

**Example file `config.txt`:**