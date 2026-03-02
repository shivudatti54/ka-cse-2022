# Protection - Summary

## Key Definitions and Concepts

- PROTECTION: Mechanisms that control access to files and directories, preventing unauthorized users from reading, writing, or deleting data.

- ACCESS MATRIX: A two-dimensional model where rows represent domains (users/groups) and columns represent objects (files), with cells containing access rights.

- ACCESS CONTROL LIST (ACL): An object-centric protection mechanism that associates a list of users and their permissions with each file or directory.

- CAPABILITY LIST: A user-centric mechanism where each user has a list of objects they can access along with permitted operations.

## Important Formulas and Techniques

- UNIX Permission Calculation: read = 4, write = 2, execute = 1
- Permission Categories: Owner, Group, Others
- Numeric Permissions: rwx = 7, rw- = 6, r-x = 5, r-- = 4, -wx = 3, -w- = 2, --x = 1, --- = 0

## Key Points

- Protection ensures data security in multi-user environments by controlling who can access what.
- ACLs are attached to objects (files), while capability lists are attached to subjects (users).
- UNIX uses a 9-bit permission scheme divided into three categories.
- Extended ACLs provide finer granularity than basic UNIX permissions.
- Explicit deny rules in ACLs override allow rules.
- Special bits include setuid (run as owner), setgid (run as group), and sticky (prevent deletion).
- The access matrix provides a theoretical framework for understanding protection.

## Common Mistakes to Avoid

- CONFUSING owner and others categories when reading permissions
- FORGETTING that execute permission on directories allows entering (cd) the directory
- NOT remembering that root/user typically bypasses permission checks
- ASSUMING numeric permissions directly convert to decimal (they are octal)

## Revision Tips

- PRACTICE converting between symbolic (rwxr-x---) and numeric (750) permission representations.
- MEMORIZE the permission values: r=4, w=2, x=1 for quick calculations.
- DRAW the access matrix for small examples to solidify understanding.
- UNDERSTAND the difference between ACL and capability list implementations conceptually.