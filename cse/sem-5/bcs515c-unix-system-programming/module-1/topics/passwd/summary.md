# Password Management in Linux/Unix - Summary

## Key Definitions and Concepts

- **/etc/passwd**: The user account database file containing seven fields: username, password placeholder, UID, GID, GECOS, home directory, and login shell

- **/etc/shadow**: Secure password storage file containing encrypted password hashes with additional security fields like expiration dates

- **UID (User ID)**: Unique numerical identifier where 0 = root, 1-999 = system accounts, 1000+ = regular users

- **Password Hashing**: Converting plaintext passwords to irreversible encrypted strings using algorithms like MD5 ($1$), SHA-256 ($5$), SHA-512 ($6$)

- **Salt**: Random data added to passwords before hashing to ensure identical passwords produce different hashes

## Important Formulas and Concepts

- **passwd file format**: `username:password:UID:GID:GECOS:home:shell`
- **shadow file format**: `username:hash:last_change:min:max:warn:inactive:expire:reserved`
- **Password aging**: Controlled via `passwd -x days -n days -w days username` or `chage` command

## Key Points

1. The /etc/passwd file is world-readable for system compatibility but should never contain actual password hashes in modern systems

2. The /etc/shadow file provides enhanced security by restricting read access to root only

3. SHA-512 ($6$) is the recommended password hashing algorithm for modern Linux systems

4. UID 0 grants superuser (root) privileges regardless of the username

5. The 'x' in the password field of /etc/passwd indicates the actual password is in /etc/shadow

6. Password policy can enforce minimum/maximum age, expiration warnings, and account locking

7. The authentication process compares the hashed input password with the stored hash using the same algorithm and salt

## Common Mistakes to Avoid

- Confusing /etc/passwd with /etc/shadow - they serve different purposes
- Using weak hashing algorithms like MD5 for password storage
- Setting password minimum age to 0 when security is a concern
- Forgetting that the root account has UID 0 regardless of the username

## Revision Tips

1. Practice reading and interpreting actual /etc/passwd and /etc/shadow entries from a Linux system

2. Memorize the seven fields of /etc/passwd using: "UPGHGS" (Username, Password, GECOS, Home, Group, Shell, UID) - remember order matters

3. Use the `id` and `finger` commands to view user information in different formats

4. Review the `man passwd`, `man shadow`, and `man chage` pages for complete command reference
