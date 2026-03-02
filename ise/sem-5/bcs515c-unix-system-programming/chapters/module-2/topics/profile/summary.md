# **UNIX SYSTEM PROGRAMMING: Profile**

## **Key Points**

- **Definition:** A profile is a script that stores the current user's environment settings, including variables, aliases, and functions, in a file.
- **Purpose:** To save and load the user's environment settings to and from a file.
- **Commonly used with:**
  - `source` and `.` commands
  - `profile` and `bash_profile` files
- **Files involved:**
  - `~/.bash_profile` (Bash)
  - `~/.profile` (Unix)
  - `~/.bashrc` (Bash)
  - `~/.tcshrc` (TCsh)

## **Importance**

- **Environment settings:** Profiles allow users to store and load environment settings, such as PATH variables, Aliases, and Functions.
- **Convenience:** Profiles simplify the process of setting up and maintaining environment settings for multiple users.

## **Syntax**

- `profile` command:

```bash
profile
```

- `source` command:

```bash
source ~/.bash_profile
```

- `.` command:

```bash
. ~/.bash_profile
```

- `export` command:

```bash
export VARIABLE="value"
```

- `unset` command:

```bash
unset VARIABLE
```
