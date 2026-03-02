# **The Type Name and Export Keywords**

### Overview

---

In C++, the `typename` keyword and the `export` keyword are used to specify the type of a variable or function in different contexts. In this topic, we will explore the definitions, explanations, and examples of these keywords.

### Type Name Keyword

---

### Definition

The `typename` keyword is used to explicitly specify the type of a variable or function. It is used to avoid ambiguity in the code.

### Explanation

When using a template, the compiler needs to know the type of the variable or function at compile-time. However, the type is not specified until runtime. To resolve this ambiguity, we use the `typename` keyword.

### Example

```cpp
template <typename T>
class Container {
private:
    T* data;
public:
    void add(T value) { data = &value; }
};

int main() {
    Container<int>* container = new Container<int>();
    container->add(10);
    return 0;
}
```

In the above example, we are using a template class `Container` to store a pointer to an integer. To avoid ambiguity, we use the `typename` keyword to specify the type of the `data` member variable.

### Export Keyword

---

### Definition

The `export` keyword is used to specify that a variable or function should be exported from the current translation unit.

### Explanation

In C++, when we use the `extern` keyword to declare a variable or function, it means that the variable or function is defined in another translation unit. However, if we want to access this variable or function from another translation unit, we need to use the `export` keyword to indicate that it is accessible.

### Example

```cpp
// file1.cpp
extern "C" {
    void foo() {
        cout << "Hello, World!" << endl;
    }
}

// file2.cpp
void foo() {
    cout << "This is file2" << endl;
}

int main() {
    foo();
    return 0;
}
```

In the above example, we are trying to call the `foo` function from `file2.cpp`. However, the `foo` function is declared with `extern "C"` in `file1.cpp` to export it. To access this function, we use the `export` keyword.

### Best Practices

---

- Use `typename` keyword to specify the type of a variable or function in templates.
- Use `export` keyword to export variables or functions from the current translation unit.

### Key Concepts

---

- `typename` keyword is used to explicitly specify the type of a variable or function in templates.
- `export` keyword is used to export variables or functions from the current translation unit.
- Use `extern "C"` to export functions that should be accessible from C code.

### Common Mistakes

---

- Forgetting to use `typename` keyword in templates.
- Forgetting to use `export` keyword when exporting variables or functions.

### Conclusion

---

In this topic, we learned about the `typename` keyword and the `export` keyword in C++. We saw examples and best practices for using these keywords, and we also learned how to avoid common mistakes.
