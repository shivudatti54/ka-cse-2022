# **Becoming the Super User: su Command**

## **Definition**

- The super user, also known as the root user, is the most powerful user in a Unix system.
- The `su` command is used to become the super user.

## **Key Points**

- **Syntax:**
  - `su [options] [username]`
- **Options:**
  - `-`
  - `-c` (execute a command with super user privileges)
  - `-s` (specify a shell to use as the super user)
  - `-l` (log out and become the super user)
- **Examples:**
  - `su` (become the super user)
  - `su -` (become the super user without a shell)
  - `su -c "ls"` (execute the `ls` command with super user privileges)
  - `su -l` (log out and become the super user)

## **Theorem**

- The `su` command uses the password of the super user to authenticate the user trying to become the super user.

## **Important Formulas/Definitions**

- None

## **Revision Tips**

- Remember the syntax and options of the `su` command.
- Practice using the `su` command to become the super user.
- Be aware of the security implications of using the `su` command.
