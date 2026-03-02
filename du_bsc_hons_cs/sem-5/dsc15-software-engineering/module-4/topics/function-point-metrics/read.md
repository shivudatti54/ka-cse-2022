# Function Point Metrics
## Introduction

Function Point Metrics is a method of measuring the size and complexity of a software system. It was first introduced by Allan Albrecht in 1979 and has since become a widely used metric in software engineering. The main goal of Function Point Metrics is to provide a way to estimate the effort required to develop a software system, based on the functionality it provides to the user.

Function Point Metrics is based on the idea that the size of a software system is directly related to the number of functions it performs. By counting the number of functions, inputs, outputs, and other components of the system, we can estimate the overall size and complexity of the system. This information can then be used to estimate the effort required to develop the system, as well as to track progress and productivity during the development process.

## Key Concepts

* **Function Points (FPs)**: A unit of measurement that represents a single function or feature of a software system.
* **Counting Rules**: A set of rules that define how to count function points, including how to identify and classify different types of functions.
* **Function Point Analysis (FPA)**: The process of applying the counting rules to a software system to determine its size in function points.
* **Value Adjustment Factor (VAF)**: A factor that is applied to the raw function point count to adjust for the complexity and difficulty of the system.
* **General System Characteristics (GSCs)**: A set of 14 characteristics that are used to determine the VAF.

## Examples

### Example 1: Counting Function Points for a Simple System

Suppose we have a simple software system that allows users to log in, view their account balance, and transfer funds. To count the function points for this system, we would identify the following functions:

* Log in (1 FP)
* View account balance (1 FP)
* Transfer funds (1 FP)

The total function point count for this system would be 3 FPs.

### Example 2: Applying the Value Adjustment Factor

Suppose we have a software system with a raw function point count of 100 FPs. To apply the VAF, we would assess the 14 GSCs and determine a score for each one. For example:

* Data Communications (score: 5)
* Distributed Data Processing (score: 3)
* Performance (score: 4)

The total VAF score would be the sum of the individual scores, which in this case would be 60. The VAF would then be applied to the raw function point count to adjust for the complexity and difficulty of the system.

## Exam Tips

1. Understand the basic concepts of Function Point Metrics, including function points, counting rules, and function point analysis.
2. Be able to identify and classify different types of functions, including inputs, outputs, and inquiries.
3. Know how to apply the counting rules to a software system to determine its size in function points.
4. Understand the concept of the Value Adjustment Factor and how it is applied to the raw function point count.
5. Be able to assess the 14 General System Characteristics and determine a score for each one.
6. Know how to use Function Point Metrics to estimate the effort required to develop a software system.
7. Understand the limitations and criticisms of Function Point Metrics, including its subjectivity and lack of precision.