# **The Second Order Linear Homogeneous Recurrence Relation with Constant Coefficients**

## **Key Points**

- **Definition**: A second-order linear homogeneous recurrence relation with constant coefficients is an equation of the form:
  ```math
  a_n + b_n x_n + c_n x_{n-1} + d_n x_{n-2} = 0
  ```

````
  where $a_n$, $b_n$, $c_n$, and $d_n$ are constants, and $x_n$ is the sequence we're trying to find a closed-form expression for.

* **Key Theorems**:
  + **Theorem 1**: A second-order linear homogeneous recurrence relation with constant coefficients has a solution of the form:
    ```math
x_n = r^n
````

    where $r$ is a constant to be determined.

- **Theorem 2**: If the characteristic equation is:
  ```math
  r^2 + br + c = 0

````
    then the solution is a linear combination of the two solutions:
    ```math
x_n = A r_1^n + B r_2^n
````

    where $A$ and $B$ are constants, and $r_1$ and $r_2$ are the roots of the characteristic equation.

- **Characteristic Equation**: The characteristic equation is the equation obtained by substituting $x_n = r^n$ into the recurrence relation:
  ```math
  r^2 + br + c = 0
  ```

````
* **Solving the Characteristic Equation**:
  + **Theorem 3**: If the characteristic equation has two distinct roots $r_1$ and $r_2$, then the solution is a linear combination of the two solutions:
    ```math
x_n = A r_1^n + B r_2^n
````

- **Theorem 4**: If the characteristic equation has a repeated root $r$, then the solution is of the form:
  ```math
  x_n = A n r^n + B r^n

````

**Important Formulas**
------------------------

* **Riccati's Formula**:
  ```math
x_n = \frac{A r^n + B}{n r^n}
````

where $r$ is a root of the characteristic equation.

## **Important Definitions**

- **Roots of the Characteristic Equation**: The values of $r$ that satisfy the characteristic equation.
- **Linear Combination**: A linear combination of two or more functions is a function that can be expressed as a linear combination of the original functions.

## **Key Concepts**

- **Recurrence Relation**: A relation between consecutive terms of a sequence.
- **Homogeneous**: A recurrence relation that is independent of the initial conditions.
- **Constant Coefficients**: A recurrence relation with constant coefficients, i.e., the coefficients do not depend on $n$.

This summary provides a concise overview of the key points, theorems, and formulas related to the Second Order Linear Homogeneous Recurrence Relation with Constant Coefficients. It is a quick revision guide for exams and is written in Markdown format for easy reading.
