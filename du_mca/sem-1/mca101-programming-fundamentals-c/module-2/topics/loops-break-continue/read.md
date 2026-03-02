# Loops: break and continue

## Introduction
Loops form the backbone of iterative programming, enabling efficient repetition of code blocks. In the University of Delhi's MCA program, mastering loop control mechanisms like `break` and `continue` is essential for writing optimized algorithms and handling real-world data processing tasks.

The `break` statement provides controlled termination from loops, crucial for scenarios like search operations or error conditions. The `continue` statement skips current iterations while maintaining loop execution, useful in data filtering applications. Together, they offer fine-grained control over program flow in complex systems ranging from database queries to game development.

Modern applications heavily rely on these constructs. For instance, e-commerce platforms use `break` to exit inventory checks once an item is found, while `continue` helps skip invalid entries in big data processing. Understanding these concepts is fundamental for implementing efficient algorithms in time-sensitive applications.

## Key Concepts
1. **Loop Types**:
   - **for**: Fixed iteration count (e.g., array processing)
   - **while**: Condition-based repetition (e.g., user input validation)
   - **do-while**: Post-condition check (e.g., menu systems)

2. **Break Statement**:
   - Immediately exits the innermost enclosing loop
   - Used in search algorithms to stop after finding target
   ```python
   for i in range(100):
       if database[i] == target:
           print("Found at index", i)
           break
   ```

3. **Continue Statement**:
   - Skips remaining code in current iteration
   - Useful for filtering invalid data
   ```java
   while(file.hasNextLine()) {
       String data = file.nextLine();
       if(data.isEmpty()) continue;
       process(data);
   }
   ```

4. **Nested Loop Control**:
   - Break/continue affect only immediate enclosing loop
   - Use flags for outer loop control
   ```c
   int found = 0;
   for(int i=0; i<10; i++){
       for(int j=0; j<10; j++){
           if(matrix[i][j] == key){
               found = 1;
               break;
           }
       }
       if(found) break;
   }
   ```

## Examples

**Example 1: Prime Number Check**
```python
num = 29
is_prime = True
for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        is_prime = False
        break  # Exit early if factor found
print(f"{num} is {'prime' if is_prime else 'not prime'}")
```
*Step-by-Step:*
1. Iterate potential divisors up to √num
2. Break loop immediately upon finding any divisor
3. Avoid unnecessary iterations after determination

**Example 2: Data Cleaning with Continue**
```c
#include <stdio.h>

int main() {
    for(int i=1; i<=10; i++) {
        if(i % 3 == 0) continue;
        printf("%d ", i);  // Skips multiples of 3
    }
    return 0;
}
```
*Output:* 1 2 4 5 7 8 10

**Example 3: Password Attempt Limiter**
```java
int attempts = 0;
final int MAX_ATTEMPTS = 3;
String correctPassword = "DU@2024";

while(attempts < MAX_ATTEMPTS) {
    String input = System.console().readLine();
    if(input.equals(correctPassword)) {
        System.out.println("Access granted!");
        break;
    }
    attempts++;
    if(attempts == MAX_ATTEMPTS) {
        System.out.println("Account locked!");
    }
}
```

## Exam Tips
1. Remember: `break` exits entire loop, `continue` skips to next iteration
2. In nested loops, use flags to control outer loops from inner breaks
3. For do-while loops, note that body executes at least once
4. Common pattern: Use `continue` to handle edge cases before main logic
5. In output prediction questions, track loop variables carefully
6. When optimizing, look for opportunities to insert early breaks
7. For error spotting: Check for infinite loops from misplaced continue/break