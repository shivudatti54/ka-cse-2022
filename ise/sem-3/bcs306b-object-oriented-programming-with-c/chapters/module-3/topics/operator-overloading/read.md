# Operator Overloading in C++

## Introduction to Operator Overloading

Operator overloading is a powerful feature of C++ that allows you to redefine the behavior of operators when they are used with user-defined types (classes and structures). This enables objects of your classes to behave more like built-in types, making code more intuitive and readable.

**Key Concept**: Operator overloading is a form of compile-time polymorphism where the same operator can have different implementations depending on the types of its operands.

## Why Use Operator Overloading?

Operator overloading provides several benefits:

- Makes code more natural and expressive
- Reduces the learning curve for using your classes
- Enables intuitive mathematical operations on objects
- Allows integration with standard library algorithms

## Overloadable Operators

Most C++ operators can be overloaded. Here's a categorization:

| Category            | Operators                            |
| ------------------- | ------------------------------------ | ----------------------- | ------ |
| Arithmetic          | `+`, `-`, `*`, `/`, `%`              |
| Relational          | `==`, `!=`, `<`, `>`, `<=`, `>=`     |
| Logical             | `&&`, `                              |                         | `, `!` |
| Assignment          | `=`, `+=`, `-=`, `*=`, `/=`, `%=`    |
| Bitwise             | `&`, `                               | `, `^`, `~`, `<<`, `>>` |
| Increment/Decrement | `++`, `--`                           |
| Subscript           | `[]`                                 |
| Function call       | `()`                                 |
| Member access       | `->`                                 |
| Memory management   | `new`, `delete`, `new[]`, `delete[]` |

**Operators that cannot be overloaded**: `.`, `.*`, `::`, `?:`, `sizeof`, `typeid`

## Syntax for Operator Overloading

Operator overloading can be implemented as:

1. Member functions
2. Friend functions (non-member functions)

### Member Function Syntax

```cpp
return_type operator#(parameters);
```

### Friend Function Syntax

```cpp
friend return_type operator#(parameters);
```

## Implementation Examples

### Overloading Binary Operators

```cpp
class Complex {
private:
    double real, imag;
public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}

    // Member function overloading
    Complex operator+(const Complex& other) const {
        return Complex(real + other.real, imag + other.imag);
    }

    // Friend function overloading
    friend Complex operator-(const Complex& c1, const Complex& c2);
};

Complex operator-(const Complex& c1, const Complex& c2) {
    return Complex(c1.real - c2.real, c1.imag - c2.imag);
}
```

### Overloading Unary Operators

```cpp
class Vector {
private:
    double x, y, z;
public:
    Vector(double x, double y, double z) : x(x), y(y), z(z) {}

    // Prefix increment
    Vector& operator++() {
        ++x; ++y; ++z;
        return *this;
    }

    // Postfix increment
    Vector operator++(int) {
        Vector temp = *this;
        ++(*this);
        return temp;
    }

    // Unary minus
    Vector operator-() const {
        return Vector(-x, -y, -z);
    }
};
```

### Overloading Stream Operators

```cpp
class Date {
private:
    int day, month, year;
public:
    Date(int d, int m, int y) : day(d), month(m), year(y) {}

    friend std::ostream& operator<<(std::ostream& os, const Date& dt);
    friend std::istream& operator>>(std::istream& is, Date& dt);
};

std::ostream& operator<<(std::ostream& os, const Date& dt) {
    os << dt.day << '/' << dt.month << '/' << dt.year;
    return os;
}

std::istream& operator>>(std::istream& is, Date& dt) {
    char slash;
    is >> dt.day >> slash >> dt.month >> slash >> dt.year;
    return is;
}
```

### Overloading Subscript Operator

```cpp
class IntArray {
private:
    int* arr;
    int size;
public:
    IntArray(int s) : size(s) { arr = new int[size]; }
    ~IntArray() { delete[] arr; }

    int& operator[](int index) {
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of bounds");
        }
        return arr[index];
    }

    const int& operator[](int index) const {
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of bounds");
        }
        return arr[index];
    }
};
```

## Rules and Guidelines for Operator Overloading

1. **Preserve original semantics**: Don't change the fundamental meaning of operators
2. **Maintain precedence and associativity**: Overloaded operators maintain their original precedence
3. **Cannot change operand count**: Unary operators remain unary, binary remain binary
4. **Cannot create new operators**: Only existing operators can be overloaded
5. **At least one operand must be user-defined type**: Cannot overload operators for built-in types only

## Type Conversion Operators

You can define conversion operators to convert your class to other types:

```cpp
class Fraction {
private:
    int numerator, denominator;
public:
    Fraction(int num, int den) : numerator(num), denominator(den) {}

    operator double() const {
        return static_cast<double>(numerator) / denominator;
    }

    explicit operator int() const {
        return numerator / denominator;
    }
};
```

## Comparison: Member vs Non-member Overloading

| Aspect                    | Member Function         | Friend Function                 |
| ------------------------- | ----------------------- | ------------------------------- |
| Left operand              | Must be object of class | Can be any type                 |
| Implicit `this`           | Available               | Not available                   |
| Access to private members | Direct                  | Requires friendship             |
| Symmetry                  | Limited                 | Better for symmetric operations |

## Common Pitfalls and Best Practices

**Common Mistakes:**

- Overloading operators with non-intuitive meanings
- Forgetting to return references for assignment operators
- Not handling self-assignment in `operator=`
- Memory leaks in copy assignment operators

**Best Practices:**

1. Make arithmetic operators return new objects rather than modifying operands
2. Make assignment operators return `*this` by reference
3. Provide both const and non-const versions of subscript operators
4. Use `explicit` for conversion operators to avoid implicit conversions
5. Follow the Rule of Three when overloading assignment operators

## Advanced Example: Matrix Class

```cpp
class Matrix {
private:
    int rows, cols;
    double** data;

    void allocateMemory() {
        data = new double*[rows];
        for (int i = 0; i < rows; ++i) {
            data[i] = new double[cols]();
        }
    }

public:
    Matrix(int r, int c) : rows(r), cols(c) { allocateMemory(); }

    // Copy constructor
    Matrix(const Matrix& other) : rows(other.rows), cols(other.cols) {
        allocateMemory();
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                data[i][j] = other.data[i][j];
            }
        }
    }

    // Assignment operator
    Matrix& operator=(const Matrix& other) {
        if (this != &other) {
            // Free existing memory
            for (int i = 0; i < rows; ++i) {
                delete[] data[i];
            }
            delete[] data;

            // Copy dimensions and allocate new memory
            rows = other.rows;
            cols = other.cols;
            allocateMemory();

            // Copy data
            for (int i = 0; i < rows; ++i) {
                for (int j = 0; j < cols; ++j) {
                    data[i][j] = other.data[i][j];
                }
            }
        }
        return *this;
    }

    // Addition operator
    Matrix operator+(const Matrix& other) const {
        if (rows != other.rows || cols != other.cols) {
            throw std::invalid_matrix_size();
        }

        Matrix result(rows, cols);
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                result.data[i][j] = data[i][j] + other.data[i][j];
            }
        }
        return result;
    }

    // Destructor
    ~Matrix() {
        for (int i = 0; i < rows; ++i) {
            delete[] data[i];
        }
        delete[] data;
    }
};
```

## Exam Tips

1. **Remember operator syntax**: `return_type operator#(parameters)`
2. **Know which operators cannot be overloaded**: `.`, `.*`, `::`, `?:`, `sizeof`, `typeid`
3. **Understand the difference between prefix and postfix increment**: Postfix takes a dummy `int` parameter
4. **Stream operators must be friend functions**: They need the stream object as the first parameter
5. **Assignment operators should return `*this` by reference**: To allow chaining (`a = b = c`)
6. **Always check for self-assignment**: In copy assignment operators
7. **Provide both const and non-const versions**: For subscript operators when appropriate
