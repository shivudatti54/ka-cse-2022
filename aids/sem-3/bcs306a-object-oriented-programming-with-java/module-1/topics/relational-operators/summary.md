# Relational Operators in Java - Summary

## Key Definitions and Concepts

- **Relational Operators**: Binary operators that compare two operands and return a boolean value (true or false)
- **Six Relational Operators**: == (equals), != (not equals), > (greater than), < (less than), >= (greater than or equals), <= (less than or equals)
- **Boolean Result**: All relational operations return boolean values used in conditional expressions

## Important Formulas and Theorems

| Operator | Name                  | Example | Result (a=10, b=20) |
| -------- | --------------------- | ------- | ------------------- |
| ==       | Equal to              | a == b  | false               |
| !=       | Not equal to          | a != b  | true                |
| >        | Greater than          | a > b   | false               |
| <        | Less than             | a < b   | true                |
| >=       | Greater than or equal | a >= b  | false               |
| <=       | Less than or equal    | a <= b  | true                |

## Key Points

- Relational operators work with primitive types: int, long, float, double, char, and boolean
- Boolean variables can only use == and != operators (not >, <, >=, <=)
- Character comparisons use ASCII/Unicode values ('A' = 65, 'a' = 97)
- Floating-point comparisons should use tolerance ranges, not direct == due to precision issues
- For object comparisons (Strings), use .equals() method, not == which compares references
- Relational operators are essential in if-else, while, for, and ternary operators
- Java does not allow chaining: use logical operators (&&, ||) instead

## Common Mistakes to Avoid

1. **Using = instead of ==**: Writing `if (a = b)` instead of `if (a == b)` causes assignment, not comparison
2. **Direct floating-point equality**: Using `d1 == d2` for doubles fails due to precision; use tolerance
3. **Comparing strings with ==**: Strings should use .equals() for content comparison
4. **Using >, < with booleans**: Cannot use comparison operators on boolean values
5. **Forgetting null checks**: Comparing objects that might be null causes NullPointerException

## Revision Tips

1. **Practice with comparisons**: Write small programs comparing different data types
2. **Remember precedence**: Arithmetic > Relational > Logical (&&, ||)
3. **Use ASCII table**: Memorize common character values for character comparisons
4. **Create decision trees**: Map out complex conditions using relational and logical operators
5. **Review String comparison**: Understand the difference between == (reference) and .equals() (content)
