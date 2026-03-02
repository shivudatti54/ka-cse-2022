# Changing File Permissions in Linux/Unix - Summary

## Key Definitions and Concepts

- **File Permissions**: Access rights (read, write, execute) assigned to files and directories in Linux
- **Permission Categories**: Owner (u), Group (g), and Others (o)
- **chmod**: Command used to change file permissions
- **umask**: Default permission mask that subtracts from base permissions
- **SUID/SGID/Sticky Bit**: Special permission bits for enhanced access control

## Important Formulas and Theorems

- **Octal Values**: Read=4, Write=2, Execute=1
- **Permission Calculation**: Add values for each category
- **Common Patterns**:
  - 755 = rwxr-xr-x (standard executable)
  - 644 = rw-r--r-- (standard file)
  - 600 = rw------- (private file)
- **Default Permissions**: Files=666, Directories=777 (minus umask)
- **Special Permissions**: SUID=4, SGID=2, Sticky=1 (prepended to base 3 digits)

## Key Points

- File permissions determine who can read, write, or execute files
- Each file has owner, group, and others permissions
- The `ls -l` command displays a 10-character permission string
- The first character indicates file type (-, d, l, etc.)
- chmod supports both numeric (755) and symbolic (u+x) modes
- Special permissions appear as 's' or 't' in the execute position
- umask is typically 022, giving default file permission 644
- Always avoid 777 permissions for security reasons

## Common Mistakes to Avoid

- Using 777 permissions (security vulnerability)
- Forgetting that directory execute permission means "traverse"
- Not securing private keys with 600 permissions
- Forgetting to set SGID on shared directories for group collaboration
- Confusing file and directory permission interpretations

## Revision Tips

- Practice writing permission calculations: rwxr-xr-- = 754
- Memorize common permission patterns and their uses
- Remember: on files, w means modify; on directories, w means delete
- Review `ls -l` output from actual Linux systems
- Practice chmod commands in a virtual machine or online Linux terminal
