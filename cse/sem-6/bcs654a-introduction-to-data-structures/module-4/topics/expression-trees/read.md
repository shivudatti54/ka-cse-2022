# Expression Trees

## Introduction to Expression Trees

An expression tree is a specialized binary tree used to represent arithmetic expressions. Unlike other binary trees, expression trees have a specific structure where:

- Each **leaf node** contains an operand (a number or variable)
- Each **internal node** contains an operator (+, -, \*, /, etc.)

Expression trees provide an elegant way to evaluate and manipulate mathematical expressions by encoding the operator precedence and associativity rules directly into the tree structure.

**Key Characteristics:**

- Perfect binary structure (every non-leaf node has exactly two children)
- Operators have higher precedence as you move down the tree
- Parentheses are implicitly represented by the tree structure

## Structure and Representation

### Basic Components

An expression tree consists of three types of nodes:

1. **Operand Nodes**: Leaf nodes containing constants or variables
2. **Operator Nodes**: Internal nodes containing arithmetic operators
3. **Structural Nodes**: The framework that connects operators and operands

```
 *
 / \
 + /
 / \ / \
 a b c d
```

_Figure 1: Expression tree for (a + b) _ (c / d)\*

### Tree Representation of Expressions

Different expressions create different tree structures:

**Infix Expression**: (a + b) \* c

```
 *
 / \
 + c
 / \
a b
```

**Postfix Expression**: a b + c \*

```
 *
 / \
 + c
 / \
a b
```

**Prefix Expression**: \* + a b c

```
 *
 / \
 + c
 / \
a b
```

## Building Expression Trees

### From Postfix Notation

The most common method for constructing expression trees uses postfix (Reverse Polish) notation. The algorithm:

1. Read the expression from left to right
2. For each token:

- If operand: Push a new node containing the operand onto stack
- If operator: Pop two nodes from stack, make them children of a new operator node, push new node onto stack

3. After processing all tokens, the stack contains the root of the expression tree

**Example**: Building tree for postfix expression "a b + c d - \*"

```
Step 1: Push a Stack: [a]
Step 2: Push b Stack: [a, b]
Step 3: Encounter +
 Pop b, pop a
 Create + node with a and b as children
 Push + node Stack: [+]
Step 4: Push c Stack: [+, c]
Step 5: Push d Stack: [+, c, d]
Step 6: Encounter -
 Pop d, pop c
 Create - node with c and d as children
 Push - node Stack: [+, -]
Step 7: Encounter *
 Pop -, pop +
 Create * node with + and - as children
 Push * node Stack: [*]
```

Final tree structure:

```
 *
 / \
 + -
 / \ / \
 a b c d
```

### From Infix Notation

Building from infix notation requires handling operator precedence and parentheses, which is more complex but follows similar principles.

## Operations on Expression Trees

### Tree Traversals

Different traversals produce different expression notations:

| Traversal Type | Expression Notation | Example Output |
| -------------- | ------------------- | -------------- |
| Inorder        | Infix               | (a + b) \* c   |
| Preorder       | Prefix              | \* + a b c     |
| Postorder      | Postfix             | a b + c \*     |

**Inorder Traversal** (Left-Root-Right):

- Produces infix notation
- Requires parentheses to maintain precedence

**Preorder Traversal** (Root-Left-Right):

- Produces prefix notation (Polish notation)
- No parentheses needed

**Postorder Traversal** (Left-Right-Root):

- Produces postfix notation (Reverse Polish notation)
- No parentheses needed

### Expression Evaluation

To evaluate an expression tree:

1. Traverse the tree (typically postorder)
2. For leaf nodes: Return the operand value
3. For internal nodes: Apply the operator to the results from left and right subtrees

**Pseudocode:**

```
function evaluate(node):
 if node is leaf:
 return node.value
 else:
 left_result = evaluate(node.left)
 right_result = evaluate(node.right)
 return apply_operator(node.operator, left_result, right_result)
```

**Example**: Evaluate tree for expression (3 + 4) \* 5

```
Tree:
 *
 / \
 + 5
 / \
3 4

Evaluation:
evaluate(*) → apply(*, evaluate(+), evaluate(5))
evaluate(+) → apply(+, evaluate(3), evaluate(4)) → 3 + 4 = 7
evaluate(5) → 5
Final: 7 * 5 = 35
```

## Applications of Expression Trees

### 1. Expression Evaluation

- Compilers and interpreters use expression trees for efficient evaluation
- Scientific computing applications
- Calculator applications

### 2. Expression Optimization

- Compilers can optimize expressions by rearranging trees
- Constant folding: Precomputing constant expressions
- Common subexpression elimination

### 3. Symbolic Computation

- Computer algebra systems
- Mathematical software (Mathematica, Maple)
- Differentiation and integration of expressions

### 4. Query Processing

- Database query optimization
- XML path expression evaluation

## Implementation in C

### Node Structure

```c
typedef struct Node {
 char data; // For operators or single-character variables
 float value; // For numeric values (optional)
 struct Node* left;
 struct Node* right;
} Node;
```

### Building from Postfix

```c
Node* create_node(char data) {
 Node* newNode = (Node*)malloc(sizeof(Node));
 newNode->data = data;
 newNode->left = newNode->right = NULL;
 return newNode;
}

Node* build_expression_tree(char postfix[]) {
 Node* stack[100];
 int top = -1;

 for (int i = 0; postfix[i] != '\0'; i++) {
 if (isalnum(postfix[i])) {
 // Operand
 Node* newNode = create_node(postfix[i]);
 stack[++top] = newNode;
 } else {
 // Operator
 Node* newNode = create_node(postfix[i]);
 newNode->right = stack[top--]; // First popped becomes right child
 newNode->left = stack[top--]; // Second popped becomes left child
 stack[++top] = newNode;
 }
 }
 return stack[top]; // Root of the expression tree
}
```

### Evaluation Function

```c
float evaluate(Node* root) {
 if (root == NULL) return 0;

 if (!root->left && !root->right) {
 // If leaf node, return numeric value
 return root->value; // Assuming values are stored
 }

 float left_val = evaluate(root->left);
 float right_val = evaluate(root->right);

 switch (root->data) {
 case '+': return left_val + right_val;
 case '-': return left_val - right_val;
 case '*': return left_val * right_val;
 case '/': return left_val / right_val;
 default: return 0;
 }
}
```

## Comparison with Other Expression Representations

| Representation       | Advantages                                                | Disadvantages                         |
| -------------------- | --------------------------------------------------------- | ------------------------------------- |
| **Expression Tree**  | Explicit precedence, Easy evaluation, Multiple traversals | Memory overhead, Complex construction |
| **Postfix Notation** | No parentheses, Easy evaluation                           | Hard to read for humans               |
| **Infix Notation**   | Human-readable                                            | Requires parentheses, Complex parsing |
| **Prefix Notation**  | No parentheses                                            | Less intuitive for humans             |

## Advanced Concepts

### Handling Variables and Functions

Expression trees can be extended to handle:

- Multi-character variable names
- Mathematical functions (sin, cos, log)
- User-defined functions
- Conditional expressions

### Memory Management

Important considerations:

- Dynamic memory allocation for nodes
- Proper deallocation to prevent memory leaks
- Recursive deletion of trees

```c
void delete_tree(Node* root) {
 if (root == NULL) return;
 delete_tree(root->left);
 delete_tree(root->right);
 free(root);
}
```

### Error Handling

Robust implementations should handle:

- Invalid expressions
- Division by zero
- Stack underflow during construction
- Memory allocation failures

## Exam Tips

1. **Tree Construction**: Practice building expression trees from both postfix and infix notations
2. **Traversal Types**: Remember which traversal produces which notation
3. **Evaluation Order**: Understand that postorder traversal is used for evaluation
4. **Parentheses**: Infix traversal requires parentheses to maintain precedence
5. **Memory Management**: Always consider memory allocation and deallocation in implementation questions
6. **Common Mistakes**: Watch for incorrect operator-operand placement and stack handling errors
