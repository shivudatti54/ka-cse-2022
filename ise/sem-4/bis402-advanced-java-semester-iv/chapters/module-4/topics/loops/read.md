# Loops in Programming

## Types of Loops

### For Loop

Fixed number of iterations.

```c
// C/Java
for (int i = 0; i < n; i++) {
    printf("%d ", i);
}

// Python
for i in range(n):
    print(i)
```

### While Loop

Condition-based, may not execute.

```c
int i = 0;
while (i < n) {
    printf("%d ", i);
    i++;
}
```

### Do-While Loop

Executes at least once.

```c
int i = 0;
do {
    printf("%d ", i);
    i++;
} while (i < n);
```

## Loop Control

| Statement | Purpose                  |
| --------- | ------------------------ |
| break     | Exit loop immediately    |
| continue  | Skip to next iteration   |
| return    | Exit function (and loop) |

## Nested Loops

```c
for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
        printf("(%d,%d) ", i, j);
    }
    printf("\n");
}
```

Time complexity: O(rows × cols)

## Common Patterns

### Sum of Array

```c
int sum = 0;
for (int i = 0; i < n; i++) {
    sum += arr[i];
}
```

### Find Maximum

```c
int max = arr[0];
for (int i = 1; i < n; i++) {
    if (arr[i] > max) {
        max = arr[i];
    }
}
```

### Print Pattern

```c
// Triangle
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
        printf("* ");
    }
    printf("\n");
}
```

## Infinite Loops

```c
while (true) { }      // Infinite
for (;;) { }          // Infinite
do { } while (1);     // Infinite
```

## Exam Tips

1. **for**: When count is known
2. **while**: When condition-based
3. **do-while**: At least one execution
4. **Nested complexity**: Multiply iterations
