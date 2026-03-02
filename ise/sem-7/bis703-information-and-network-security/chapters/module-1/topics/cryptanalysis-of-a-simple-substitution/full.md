# **Cryptanalysis of a Simple Substitution**

## **Introduction**

A substitution cipher is a type of encryption where each plaintext letter is replaced by a different letter or symbol. Simple substitution ciphers are easy to create and use, but they are also vulnerable to cryptanalysis, which is the process of breaking an encryption algorithm. In this topic, we will explore the principles of cryptanalysis of a simple substitution, including the methods used to break these ciphers.

## **Historical Context**

Simple substitution ciphers have been used for centuries, dating back to ancient civilizations such as the Egyptians and Greeks. The Caesar Cipher, a simple substitution cipher, was used by the Roman Emperor Julius Caesar to encrypt messages.

## **Types of Substitution Ciphers**

There are several types of substitution ciphers, including:

- **Monoalphabetic Substitution Cipher**: In this type of cipher, each plaintext letter is replaced by a different letter. For example, the letter "a" is replaced by the letter "d".
- **Polyalphabetic Substitution Cipher**: In this type of cipher, each plaintext letter is replaced by a different letter, but the same letter can be replaced by different letters depending on the context.
- **Transposition Cipher**: In this type of cipher, the plaintext letters are rearranged according to a specific pattern.

## **Cryptanalysis Methods**

There are several methods used to cryptanalyze simple substitution ciphers, including:

- **Frequency Analysis**: This method involves analyzing the frequency of letters in the ciphertext to determine the likelihood of certain letters being used as substitutions.
- **Chi-Squared Test**: This method involves calculating the chi-squared statistic to determine the likelihood of a particular substitution being used.
- **Kasiski Examination**: This method involves searching for patterns in the ciphertext to determine the length of the keyword used in the substitution cipher.
- **Brute Force Attack**: This method involves trying all possible substitutions to determine the correct ones.

## **Frequency Analysis**

Frequency analysis is a popular method used to cryptanalyze simple substitution ciphers. The idea behind frequency analysis is that certain letters appear more frequently in the English language than others.

### Step 1: Calculate the Frequency of Letters

To perform frequency analysis, we need to calculate the frequency of each letter in the ciphertext. We can do this by counting the number of occurrences of each letter in the ciphertext.

### Step 2: Compare the Frequency of Letters to the English Language

Once we have calculated the frequency of each letter in the ciphertext, we can compare it to the frequency of letters in the English language. We can do this by using a table of letter frequencies or by calculating the frequency of each letter in the ciphertext manually.

### Step 3: Identify the Most Common Letters

By comparing the frequency of letters in the ciphertext to the frequency of letters in the English language, we can identify the most common letters. These letters are likely to be the most common substitutions.

### Step 4: Use the Most Common Letters to Decrypt the Ciphertext

Once we have identified the most common letters, we can use them to decrypt the ciphertext. We can do this by substituting the most common letters with their corresponding plaintext letters.

## **Example**

Suppose we have a ciphertext that reads "Khoor Zruog". We can perform frequency analysis to determine the correct substitutions.

### Step 1: Calculate the Frequency of Letters

We can calculate the frequency of each letter in the ciphertext as follows:

| Letter | Frequency |
| ------ | --------- |
| K      | 1         |
| H      | 1         |
| O      | 1         |
| O      | 1         |
| R      | 1         |
| Z      | 1         |
| R      | 1         |
| U      | 1         |
| O      | 1         |
| G      | 1         |

### Step 2: Compare the Frequency of Letters to the English Language

We can compare the frequency of letters in the ciphertext to the frequency of letters in the English language as follows:

| Letter | Frequency in English | Frequency in Ciphertext |
| ------ | -------------------- | ----------------------- |
| E      | 12.7%                | 0%                      |
| T      | 9.05%                | 0%                      |
| A      | 8.17%                | 0%                      |
| O      | 7.51%                | 20%                     |
| I      | 6.97%                | 0%                      |
| N      | 6.75%                | 0%                      |
| S      | 6.33%                | 0%                      |
| H      | 6.09%                | 10%                     |
| R      | 5.99%                | 15%                     |
| D      | 4.25%                | 0%                      |

### Step 3: Identify the Most Common Letters

By comparing the frequency of letters in the ciphertext to the frequency of letters in the English language, we can identify the most common letters as "R" and "O".

### Step 4: Use the Most Common Letters to Decrypt the Ciphertext

We can use the most common letters to decrypt the ciphertext as follows:

- "K" becomes "E" (since "K" is not a common letter in the English language)
- "H" becomes "T" (since "H" is not a common letter in the English language)
- "O" becomes "A" (since "O" is a common letter in the English language)
- "R" becomes "N" (since "R" is a common letter in the English language)
- "Z" becomes "S" (since "Z" is not a common letter in the English language)
- "U" becomes "I" (since "U" is not a common letter in the English language)
- "O" becomes "A" (since "O" is a common letter in the English language)
- "G" becomes "D" (since "G" is not a common letter in the English language)

The decrypted text is "THE CAT SAT".
