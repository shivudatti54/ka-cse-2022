# **Meaning of Internal and External Commands**

## **Introduction**

In the UNIX operating system, commands are the building blocks of a user's interface. These commands are used to interact with the operating system, perform various tasks, and manage files and directories. There are two types of commands in UNIX: internal commands and external commands. In this document, we will explore the meaning, differences, and applications of both internal and external commands.

## **Internal Commands**

Internal commands are programs that are written specifically for the UNIX operating system. They are usually shorter and more efficient than external commands. Internal commands are run by the shell (the command-line interpreter) and are executed in the user's current shell session.

**Characteristics of Internal Commands:**

- They are written specifically for the UNIX operating system.
- They are executed in the user's current shell session.
- They have a shorter syntax and are more efficient than external commands.
- They do not have a separate executable file.
- They do not require a separate shell to be executed.

**Examples of Internal Commands:**

- `cd`: Changes the current directory.
- `pwd`: Prints the current working directory.
- `set`: Sets the value of a shell variable.
- `export`: Expands the value of an environment variable.
- `unset`: Unsets the value of an environment variable.

## **External Commands**

External commands are programs that are written for other operating systems, such as MS-DOS or Windows. They are usually longer and less efficient than internal commands. External commands are run by the shell and are executed in a separate process.

**Characteristics of External Commands:**

- They are written for other operating systems, such as MS-DOS or Windows.
- They are executed in a separate process.
- They have a longer syntax and are less efficient than internal commands.
- They require a separate executable file.
- They require a separate shell to be executed.

**Examples of External Commands:**

- ` gzip`: Compresses a file.
- `tar`: Archives a file or directory.
- `scp`: Copies a file from one location to another.
- `ssh`: Securely connects to a remote host.
- `ls`: Lists the files in a directory.

## **History of Internal and External Commands**

The UNIX operating system was first developed in the 1970s by Ken Thompson and Dennis Ritchie. The first UNIX system was called UNIX 1.0, and it included a set of internal commands that were written specifically for the operating system. These internal commands were designed to be efficient and easy to use, and they quickly became the standard for the UNIX community.

In the 1980s, the UNIX operating system was ported to other platforms, such as MS-DOS and Windows. This led to the development of external commands that were written for these platforms. These external commands were often designed to be compatible with the UNIX commands, and they quickly became popular among UNIX users.

## **Modern Developments**

In recent years, there has been a trend towards the use of internal commands in UNIX systems. This is due in part to the increasing use of scripting languages, such as Perl and Python, which allow users to write complex commands in a more readable and maintainable way.

Additionally, the UNIX operating system has become increasingly modular, with many components written as separate programs. This has led to the development of internal commands that can be easily added or removed as needed.

## **Case Studies**

- **Scripting:** A system administrator uses internal commands to automate a series of tasks, such as backing up files and sending emails. The administrator writes a script that uses internal commands to perform these tasks, and then schedules the script to run automatically at regular intervals.
- **File Management:** A user uses internal commands to manage a large directory of files. The user uses the `cd` command to navigate the directory, and the `ls` command to list the files. The user also uses the `mkdir` command to create new directories, and the `rm` command to delete files.
- **Network Management:** A network administrator uses external commands to manage a network of computers. The administrator uses the `scp` command to copy files from one computer to another, and the `ssh` command to securely connect to remote computers.

## **Applications**

Internal and external commands have a wide range of applications in the UNIX operating system.

- **Automation:** Internal commands can be used to automate repetitive tasks, such as backing up files or sending emails.
- **File Management:** Internal commands can be used to manage files and directories, such as creating new directories or deleting files.
- **Network Management:** External commands can be used to manage a network of computers, such as copying files or securely connecting to remote computers.
- **Scripting:** Internal commands can be used to write complex scripts that perform a series of tasks.

## **Diagrams**

Here is a diagram that shows the relationship between internal and external commands:

```markdown
+---------------+
| Shell |
+---------------+
|
|
v
+---------------+
| Internal |
| Commands |
| (e.g. cd, |
| pwd, set) |
+---------------+
|
|
v
+---------------+
| External |
| Commands |
| (e.g. gzip, |
| tar, scp) |
+---------------+
```

## **Further Reading**

- UNIX System Administration, 4th Edition by David A. Korn, Brian W. Kernighan, and P.J. Plauger
- UNIX Command-Line Tools and Scripts by William Shotts
- UNIX Internals: Designing and Building Operating Systems by Adrian B. Colledge and John F. Woods

In conclusion, internal and external commands are fundamental components of the UNIX operating system. Internal commands are written specifically for the UNIX operating system and are executed in the user's current shell session. External commands are written for other operating systems and are executed in a separate process. Understanding the differences between internal and external commands is essential for effective use of the UNIX operating system.
