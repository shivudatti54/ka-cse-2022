# Digital Authentication: Password-Based Security - Summary

## Key Definitions and Concepts

- **Authentication**: The process of verifying the identity of a user, process, or device before granting access to resources
- **Password-Based Authentication**: A knowledge-based authentication mechanism using secrets (passwords) known only to the user
- **Salt**: A random value generated for each user and combined with the password before hashing to prevent rainbow table attacks
- **Hash**: A one-way cryptographic function that transforms input data into a fixed-size string of characters
- **Rainbow Table**: Pre-computed tables used to reverse cryptographic hash functions

## Important Formulas and Theorems

- **Password Hashing**: `stored_hash = bcrypt(password + salt, cost_factor)`
- **Verification**: `verify(input_password) = (bcrypt(input_password + salt) == stored_hash)`
- **Entropy Calculation**: For password strength, entropy ≈ log₂(number_of_possible_combinations)
- **Cost Factor**: In bcrypt, the cost factor determines computational complexity (2^cost iterations)

## Key Points

- Passwords fall under "something you know" authentication factor
- Never store passwords in plaintext; always use salted hashes with algorithms like bcrypt, Argon2, or PBKDF2
- Salting prevents rainbow table attacks by ensuring each user's password hash is unique
- Common password attacks include brute force, dictionary attacks, rainbow tables, phishing, and credential stuffing
- Modern password policies should emphasize length over complexity (NIST guidelines)
- Password managers help users maintain unique, strong passwords for each service
- Multi-factor authentication provides significant security improvement over single-factor
- Constant-time comparison prevents timing attacks during password verification
- Account lockout policies help prevent brute force attacks but must be carefully configured to avoid denial-of-service

## Common Mistakes to Avoid

1. **Storing passwords in plaintext**: This catastrophic mistake exposes all user credentials if the database is compromised
2. **Using weak hashing algorithms**: MD5 and SHA-1 are cryptographically broken for password storage
3. **Not using salts**: Without unique salts, attackers can use pre-computed rainbow tables
4. **Ignoring timing attacks**: Using regular string comparison can leak password information
5. **Setting overly restrictive policies**: Complex rules + frequent changes lead to weaker passwords as users resort to predictable patterns

## Revision Tips

1. Practice explaining how salting prevents rainbow table attacks—this is a favorite exam question
2. Memorize the three authentication factors and be ready to classify examples
3. Understand why one-way hashing (not encryption) is used for passwords
4. Review the password verification流程 step-by-step
5. Remember NIST 2017 recommendations: longer passwords, no mandatory expiration, check compromised passwords
6. Be able to evaluate a password policy and identify both strengths and weaknesses
7. Know the difference between brute force and dictionary attacks