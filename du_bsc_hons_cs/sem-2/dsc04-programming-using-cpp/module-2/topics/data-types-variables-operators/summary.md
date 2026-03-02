# Data Types, Variables & Operators in C++  
*Quick Revision – BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)*  

---

### Introduction
This unit forms the foundation of C++ programming as prescribed in the Delhi University NEP 2024 syllabus. Understanding data types, variable handling, and operators is essential for writing correct, efficient, and maintainable code.

---

### 1. Data Types  
- **Primitive (fundamental) types** – `int`, `float`, `double`, `char`, `bool`, `void`.  
- **Modifiers** – `short`, `long`, `signed`, `unsigned` alter range/sign.  
- **Size & Range** – implementation‑dependent; use `sizeof` or `<climits>` for exact values.  
- **Derived types** – pointers (`*`), references (`&`), arrays, functions.  
- **User‑defined types** – `struct`, `class`, `enum`, `union`, `typedef`.  
- **Qualifiers** – `const`, `volatile`, `constexpr` (compile‑time constants).  

---

### 2. Variables  
- **Declaration vs. Definition** – declaration announces type & name; definition also allocates storage.  
- **Initialization** – C‑style (`int a = 5;`), constructor (`int a(5);`), uniform (`int a{5};`).  
- **Naming rules** – alphanumeric & underscore, cannot start with a digit; case‑sensitive; avoid reserved keywords.  
- **Scope** – *global* (outside any function), *local* (inside block/function), *block* (e.g., `for` loop).  
- **Storage classes** – `auto` (default for local), `register`, `static`, `extern`, `mutable`.  
- **Lifetime** – automatic (stack), static (global/static variable), dynamic (heap via `new`/`delete`).  

---

### 3. Operators  

| Category | Operators | Remarks |
|----------|-----------|---------|
| **Arithmetic** | `+`, `-`, `*`, `/`, `%` | Integer `%` yields remainder; `/` for floats yields real division. |
| **Relational** | `==`, `!=`, `<`, `>`, `<=`, `>=` | Result is `bool`. |
| **Logical** | `&&`, `||`, `!` | Short‑circuit evaluation. |
| **Bitwise** | `&`, `|`, `^`, `~`, `<<`, `>>` | Operate on integer bits; `<<`/`>>` shift. |
| **Assignment** | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `|=` | Compound assignments modify in‑place. |
| **Increment/Decrement** | `++`, `--` | Prefix (`++a`) vs. postfix (`a++`) matters for value used. |
| **Conditional (Ternary)** | `?:` | `condition ? expr1 : expr2`. |
| **Comma** | `,` | Evaluates left, discards result, returns right. |
| **sizeof** | `sizeof(type/object)` | Returns size in bytes. |
| **Type Cast** | `static_cast<T>`, `const_cast`, `reinterpret_cast`, C‑style `(T)expr` | Explicit conversion. |

- **Operator Precedence & Associativity** – Highest: postfix (`()`, `[]`, `.`, `->`, `++`, `--`), then unary, multiplicative, additive, shift, relational, equality, bitwise AND, XOR, OR, logical AND, OR, conditional, assignment, comma. Parentheses override precedence.  

---

### Conclusion
Mastering data types, variable semantics, and C++ operators enables you to manipulate data correctly and write expressive statements. These fundamentals are directly tested in the Delhi University examinations and constitute the building blocks for more advanced topics such as control structures, functions, and object‑oriented programming. Review the table of operator precedence and practice declaring variables with different storage classes to solidify your understanding.  

---  

*Prepare well – clarity on these core concepts is the key to scoring in the NEP 2024 C++ paper!*