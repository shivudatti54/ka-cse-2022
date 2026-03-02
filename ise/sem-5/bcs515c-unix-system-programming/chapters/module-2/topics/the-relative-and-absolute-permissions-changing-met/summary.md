# **The Relative and Absolute Permissions Changing Methods**

- **Relative Permissions Changing Methods:**
  - Using `chmod u+x file` to add execute permission to the owner
  - Using `chmod g+x file` to add execute permission to the group
  - Using `chmod o+x file` to add execute permission to others
  - Using `chmod u+x file` to remove execute permission from the owner
  - Using `chmod g+x file` to remove execute permission from the group
  - Using `chmod o+x file` to remove execute permission from others

- **Absolute Permissions Changing Methods:**
  - Using `chmod 755 file` to change permissions to:
    - `u` (owner) `rwx` (read, write, execute)
    - `g` (group) `r-x` (read, execute)
    - `o` (others) `r-x` (read, execute)
  - Using `chmod 644 file` to change permissions to:
    - `u` (owner) `rwx` (read, write)
    - `g` (group) `r-x` (read, execute)
    - `o` (others) `r-x` (read, execute)

- **Octal System:**
  - Octal system is based on base 8 number system
  - Each digit in the octal system represents the permission for a user (u), group (g), or others (o)

- **Bitwise Operations:**
  - The permissions can be modified using bitwise operations (AND, OR, XOR)
  - The `chmod` command uses bitwise operations to modify permissions

- **Important Formulas and Theorems:**
  - The formula for changing permissions is:
    - `chmod mode file` (where `mode` is the new permissions)
  - The theorem for the octal system is:
    - `u` (owner) = 4 (4^2) + 2 (2^2) + 0 (0^2)
    - `g` (group) = 4 + 2
    - `o` (others) = 4
