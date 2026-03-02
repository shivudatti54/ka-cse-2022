# **Add a Column Commission with Domain to the Employee Table**

## **Key Points**

- To add a commission column to the Employee table, we need to define a domain for it.
- Commission is calculated as a percentage of the employee's salary.
- The domain for the commission column should be a percentage value between 0 and 1.
- We can use the `CHECK` constraint to enforce the domain.
- The formula for commission is: `commission = salary * commission_percentage`

## **Important Formulas and Definitions**

- Commission Percentage: A percentage value between 0 and 1 that represents the commission rate.
- Commission Formula: `commission = salary * commission_percentage`
- Domain: A set of values that a column can take.

**Theorem:** The Commission Formula is correct because it calculates the commission as a percentage of the salary.

**CHECK Constraint:**
`CHECK (commission BETWEEN 0 AND 1)`

## **Revision Tips:**

- Understand the concept of a domain and its importance in defining a column.
- Know how to calculate the commission using the commission formula.
- Be able to apply the `CHECK` constraint to enforce the domain of the commission column.
