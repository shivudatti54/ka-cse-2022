## Sort the Numbers according to Tens Place using Comparator

### Advanced Java - JDBC

#### Revision Notes

#### Key Concepts

- **Comparator**: An interface in Java that allows objects to be compared with each other.
- **Lambda Expressions**: Used to implement comparators in a concise manner.
- **Tens Place Sort**: Sorting numbers based on their tens place digit.

#### Important Formulas and Definitions

- **Tens Place**: The second digit from the right in a decimal number (e.g., 123 -> 2 is the tens place).
- **Comparator Interface**: `public interface Comparator<T> { int compare(T o1, T o2); }`

#### Theorems and Concepts

- **Lambda Expressions**: `Comparator<T> comparator = (o1, o2) -> { /* compare logic */ };`
- **Method Reference**: Can be used to implement comparators in a concise manner.
- **Comparator Chain**: Multiple comparators can be chained together to compare objects.

#### Key Points

- Use a lambda expression or method reference to implement a custom comparator.
- Use the `compare()` method to compare two objects.
- The order of comparison is determined by the comparator's logic.
- The `Comparator` interface is used to define the comparison logic.

#### Example

```java
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) {
        // Create an array of numbers
        int[] numbers = {12, 45, 67, 89, 10};

        // Sort the numbers using a custom comparator
        Arrays.sort(numbers, (o1, o2) -> {
            int tens1 = Integer.parseInt(String.valueOf(o1).substring(1));
            int tens2 = Integer.parseInt(String.valueOf(o2).substring(1));
            return Integer.compare(tens1, tens2);
        });

        // Print the sorted numbers
        System.out.println(Arrays.toString(numbers));
    }
}
```

#### Revision Tips

- Understand the concept of comparators and lambda expressions.
- Practice implementing custom comparators for sorting numbers.
- Familiarize yourself with the `Comparator` interface and its methods.
