# **Data Flow and Behavioural Model**

## **Introduction**

In digital design and computer organization, the two fundamental models used to describe digital circuits are the Data Flow Model and the Behavioural Model. In this study material, we will explore the definitions, characteristics, and applications of both models.

## **Data Flow Model**

### Definition

The Data Flow Model is a mathematical representation of digital circuits that focuses on the flow of data through a circuit, rather than the logic functions that control it.

### Characteristics

- **Data-centric**: The model emphasizes the flow of data through the circuit.
- **Hierarchical**: The circuit is represented as a hierarchy of functional blocks, each with a specific input and output.
- **Declarative**: The model describes the circuit's behavior using a set of equations that relate the inputs and outputs.

### Notation

The Data Flow Model uses a set of notation to describe the circuit's behavior:

| Notation | Description               |
| -------- | ------------------------- |
| `A`      | Input signal              |
| `B`      | Output signal             |
| `X`      | Intermediate signal       |
| `G`      | Gain or transfer function |
| `Y`      | Output signal             |

### Example

Consider a simple digital circuit with two inputs, `A` and `B`, and one output, `Y`. The circuit can be represented using the Data Flow Model as follows:

```
  A  ---> X1
  |
  | G1
  | X2
  |
  | A ---> X2
  |
  | B ---> X3
  |
  | G2
  | Y
```

In this example, `X1`, `X2`, and `X3` are intermediate signals that flow through the circuit, while `G1` and `G2` are the gain or transfer functions that control the flow of data.

## **Behavioural Model**

### Definition

The Behavioural Model is a mathematical representation of digital circuits that focuses on the control signals and their effects on the circuit's behavior.

### Characteristics

- **Control-centric**: The model emphasizes the control signals that drive the circuit's behavior.
- ** Imperative**: The model describes the circuit's behavior using a set of statements that specify the actions to be taken.
- **Procedural**: The model describes the circuit's behavior using a set of procedures that define the steps to be taken.

### Notation

The Behavioural Model uses a set of notation to describe the circuit's behavior:

| Notation | Description              |
| -------- | ------------------------ |
| `IF`     | Control condition        |
| `THEN`   | Action to be taken       |
| `ELSE`   | Alternative action       |
| `ENDIF`  | End of control structure |

### Example

Consider a simple digital circuit with two inputs, `A` and `B`, and one output, `Y`. The circuit can be represented using the Behavioural Model as follows:

```
IF (A > B)
  THEN Y = A
  ELSE Y = B
ENDIF
```

In this example, the control condition `IF (A > B)` specifies the condition under which the circuit takes action, and the action `THEN Y = A` specifies the output when the condition is true.

## **Comparison and Contrast**

| Model           | Data Flow    | Behavioural     |
| --------------- | ------------ | --------------- |
| **Focus**       | Data flow    | Control signals |
| **Notation**    | Hierarchical | Imperative      |
| **Description** | Declarative  | Procedural      |

## **Conclusion**

In conclusion, the Data Flow Model and the Behavioural Model are two fundamental models used to describe digital circuits. While the Data Flow Model emphasizes the flow of data through the circuit, the Behavioural Model focuses on the control signals that drive the circuit's behavior. By understanding both models, designers and engineers can develop a deeper appreciation for the complexities of digital design and computer organization.

## **Key Concepts**

- **Data Flow Model**: A mathematical representation of digital circuits that focuses on the flow of data through a circuit.
- **Behavioural Model**: A mathematical representation of digital circuits that focuses on the control signals and their effects on the circuit's behavior.
- **Hierarchical**: A characteristic of the Data Flow Model that describes the circuit as a hierarchy of functional blocks.
- **Imperative**: A characteristic of the Behavioural Model that describes the circuit's behavior using a set of statements that specify the actions to be taken.

## **Study Questions**

1.  What is the main difference between the Data Flow Model and the Behavioural Model?
2.  How do the two models describe the circuit's behavior?
3.  What is the significance of the notation used in each model?

## **References**

- **"Digital Design and Computer Organization"** by M. Morris Mano
- **"Computer Organization and Design"** by David A. Patterson and John L. Hennessy
