# Password Management in Linux/Unix Systems

## Introduction

The `/etc/passwd` file is one of the most fundamental configuration files in Linux and Unix-like operating systems. It serves as the primary user database, storing essential information about every user account on the system. Understanding the structure and management of user passwords is crucial for any computer science engineering student, as it forms the backbone of system security and user authentication mechanisms.

In the early Unix systems, the `/etc/passwd` file contained encrypted passwords, making it readable by all users for backward compatibility with older programs. However, this approach posed significant security risks since anyone could obtain the encrypted password hashes and attempt to crack them. Modern Linux distributions have addressed this vulnerability by implementing shadow password technology, where sensitive password information is stored in the separate `/etc/shadow` file accessible only to the root user.

This topic covers the complete spectrum of password management in Linux, from understanding the passwd file format to implementing secure authentication mechanisms. These concepts are essential for system administrators and developers working with Linux systems, and they form a significant portion of the syllabus for Operating Systems and Unix/Linux courses.

## Key Concepts

### The /etc/passwd File Structure

The `/etc/passwd` file is a text file that contains one record per user account, with each record consisting of seven fields separated by colons. The general format is:

```
username:password:UID:GID:GECOS:home_directory:shell
```

Each field has a specific meaning:

1. **Username**: A unique identifier for the user (1-32 characters, case-sensitive)
2. **Password**: Historically contained encrypted password; now shows 'x' indicating shadow password
3. **UID (User ID)**: A unique numerical identifier (0 for root, 1-999 for system accounts, 1000+ for regular users)
4. **GID (Group ID)**: The primary group ID number from `/etc/group`
5. **GECOS**: User information field (full name, office details, etc.)
6. **Home Directory**: The absolute path to the user's home directory
7. **Shell**: The absolute path to the user's login shell

Example entry:

```
john:x:1001:1001:John Smith,Room 301,9845012345:/home/john:/bin/bash
```

### The /etc/shadow File Structure

The `/etc/shadow` file provides enhanced security by storing password hashes separately from the public-readable passwd file. Each record contains nine fields:

```
username:password:last_change:min_age:max_age:warn:inactive:expire:reserved
```

- **password**: Encrypted password hash starting with $id$ (MD5, SHA-256, or SHA-512)
- **last_change**: Days since Unix epoch when password was last changed
- **min_age**: Minimum days before password can be changed
- **max_age**: Maximum days before password requires change
- **warn**: Days before expiration user is warned
- **inactive**: Days after expiration before account is disabled
- **expire**: Absolute date when account expires

### Password Hashing Algorithms

Modern Linux systems support multiple password hashing algorithms identified by the prefix in the password hash:

- **$1$**: MD5 algorithm (legacy, not recommended)
- **$2a$**: Blowfish algorithm
- **$5$**: SHA-256 algorithm (recommended)
- **$6$**: SHA-512 algorithm (most secure, default in modern distributions)

The `crypt()` function and its modern implementations handle the hashing process. When a user creates or changes a password, the system generates a random salt (2 characters for MD5, up to 16 for SHA-512) to ensure that identical passwords produce different hashes.

### The passwd Command

The `passwd` command is the primary tool for password management:

```bash
# Change own password
passwd

# Change another user's password (root only)
passwd username

# Lock/unlock user account
passwd -l username
passwd -u username

# Set password expiration
passwd -x 90 username # Maximum 90 days
passwd -n 7 username # Minimum 7 days between changes
passwd -w 7 username # Warn 7 days before expiration

# Delete password
passwd -d username
```

### User Authentication Process

When a user logs in, the authentication process follows these steps:

1. System prompts for username and password
2. Username is looked up in `/etc/passwd` to find UID, GID, and home directory
3. Password is read from `/etc/shadow` (or encrypted from `/etc/passwd` in old systems)
4. Input password is hashed with the same algorithm and salt
5. Generated hash is compared with stored hash
6. If match, user is authenticated and login shell is started

### User Management Commands

Beyond `passwd`, several commands manage user accounts:

```bash
# Create new user
useradd -m -s /bin/bash -c "Full Name" username

# Modify user properties
usermod -aG groupname username # Add to group

# Delete user
userdel -r username

# View user info
id username
groups username
```

## Examples

### Example 1: Analyzing /etc/passwd Entry

**Problem**: Explain the meaning of the following passwd entry:

```
admin:x:0:0:Administrator:/root:/bin/bash
```

**Solution**:

- **Username**: admin
- **Password field**: 'x' indicates password is stored in /etc/shadow
- **UID**: 0 (root/superuser privileges)
- **GID**: 0 (belongs to root group)
- **GECOS**: Administrator (user's full name or description)
- **Home Directory**: /root (root user's home)
- **Shell**: /bin/bash (bash shell)

This is the root account entry, with special UID 0 that grants full system privileges.

### Example 2: Setting Password Policy

**Problem**: Configure a password policy for user "student" that requires:

- Maximum validity: 60 days
- Minimum days between changes: 1
- Warning period: 7 days

**Solution**:

```bash
# Using passwd command
passwd -x 60 -n 1 -w 7 student

# Verify settings
chage -l student
```

Output shows:

```
Last password change : Jan 15, 2025
Password expires : Mar 16, 2025
Password inactive : never
Account expires : never
Minimum number of days between changes : 1
Maximum number of days between changes : 60
Number of days of warning before password expires : 7
```

### Example 3: Creating Password Hash

**Problem**: Manually generate SHA-512 hash for password "MySecurePass123"

**Solution**:

```bash
# Generate salt and hash using mkpasswd
mkpasswd -m sha-512 MySecurePass123

# Or using Python
python3 -c "import crypt; print(crypt.crypt('MySecurePass123', crypt.mksalt(crypt.METHOD_SHA512)))"

# Example output:
$6$rounds=656000$saltvalue12345678$hashedoutput...
```

The hash shows:

- $6$ = SHA-512 algorithm
- rounds=656000 = Number of iterations
- saltvalue12345678 = Random salt
- hashedoutput... = The actual password hash

## Exam Tips

1. **Remember the passwd file format**: The seven fields are username, password, UID, GID, GECOS, home directory, and shell. This is frequently asked in exams.

2. **Understand shadow passwords**: Know that /etc/shadow stores encrypted passwords and is readable only by root, while /etc/passwd is world-readable.

3. **UID values matter**: Remember that UID 0 is root, UIDs 1-999 are system accounts, and UIDs 1000+ are regular user accounts.

4. **Password hashing prefixes**: Be familiar with $1$, $2a$, $5$, and $6$ prefixes indicating MD5, Blowfish, SHA-256, and SHA-512 respectively.

5. **passwd command options**: Remember common options like -l (lock), -u (unlock), -d (delete), -x (max days), -n (min days), and -w (warn days).

6. **Authentication process**: Understand the step-by-step process of how login authentication works with password hashing and comparison.

7. **GECOS field**: Know that this field traditionally contains the user's full name and can be modified using the `chfn` command.

8. **Password aging commands**: The `chage` command is essential for managing password expiration; practice using `chage -l` to list and `chage` to modify settings.
