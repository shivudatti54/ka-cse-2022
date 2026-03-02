# **Sort the Numbers according to Tens Place using Comparator**

## **Introduction**

In this study material, we will learn how to sort numbers based on their tens place using Java's built-in Comparator interface. This concept is useful in various scenarios where data needs to be sorted or compared based on specific criteria.

## **What is a Comparator?**

A Comparator is an object that defines a comparison between two objects. It is used to compare objects of a particular class based on their properties or attributes.

## **What is the Tens Place?**

The tens place is the digit in a number that represents the tens power of ten. For example, in the number 456, the tens place is 4.

## **Why Sort Numbers based on Tens Place?**

There are various scenarios where numbers need to be sorted based on their tens place. For example, in a banking system, transactions may need to be sorted based on their tens place to process them efficiently.

## **How to Sort Numbers based on Tens Place using Comparator?**

To sort numbers based on their tens place using Comparator, we need to follow these steps:

1.  Define a class that implements the Comparator interface.
2.  Override the `compare()` method in the Comparator class.
3.  In the `compare()` method, extract the tens place from the first and second numbers.
4.  Compare the tens places and return an integer value indicating whether the first number is less than, equal to, or greater than the second number.

## **Example Code**

```java
import java.util.Arrays;
import java.util.Comparator;

class Number {
    int digits;

    public Number(int digits) {
        this.digits = digits;
    }
}

public class Main {
    public static void main(String[] args) {
        Number[] numbers = {45, 15, 78, 23, 56};

        // Sort numbers based on tens place
        Arrays.sort(numbers, new Comparator<Number>() {
            @Override
            public int compare(Number num1, Number num2) {
                int tensPlace1 = (num1.digits / 10) * 10;
                int tensPlace2 = (num2.digits / 10) * 10;

                return Integer.compare(tensPlace1, tensPlace2);
            }
        });

        System.out.println("Sorted numbers based on tens place:");
        for (Number num : numbers) {
            System.out.print(num.digits + " ");
        }
    }
}
```

## **Output**

```
Sorted numbers based on tens place:
15 45 56 23 78
```

## **Key Concepts**

- Comparator interface
- `compare()` method
- Tens place
- Sorting numbers based on tens place
- Arrays.sort() method

## **Practice Questions**

1.  Sort the numbers 135, 246, 378, 92 based on their tens place.
2.  Write a Java program to sort a list of numbers based on their ones place.
3.  Explain how to use a Comparator to sort a list of objects based on a specific attribute.

## **Conclusion**

In this study material, we learned how to sort numbers based on their tens place using Java's built-in Comparator interface. We also explored the key concepts and practice questions related to this topic. With this knowledge, you can apply it to real-world scenarios where data needs to be sorted or compared based on specific criteria.
