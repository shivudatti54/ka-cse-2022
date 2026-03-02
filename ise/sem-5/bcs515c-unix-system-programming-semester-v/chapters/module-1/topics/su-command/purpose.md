# Learning Purpose: `su` command

### 1. Importance

The `su` (substitute user) command is a fundamental security and administration tool. Understanding its proper use is critical for managing system security, permissions, and user privileges on a multi-user UNIX system. It is a primary mechanism for performing administrative tasks, making it vital for any system programmer or administrator to master.

### 2. Learning Outcomes

Students will learn the syntax and functionality of the `su` command to switch user identities. This includes understanding the difference between a login (`-l` or `-`) and a non-login shell, how environment variables change, and the crucial distinction between `su` and `sudo`. They will also learn to verify the current user context using commands like `whoami` and `id`.

### 3. Connection to Other Concepts

This topic connects directly to core UNIX concepts of file permissions, user and group IDs (UIDs/GIDs), and process ownership. It is foundational for understanding privilege escalation, a key principle in system security. Mastery of `su` is essential before learning more advanced tools like `sudo`, which provides more granular and auditable control.

### 4. Real-World Applications

System administrators use `su` daily to perform tasks requiring root privileges, such as installing software, modifying system configurations, and managing user accounts. Developers might use it to test applications under different user permissions or to manage services. It is an indispensable tool for secure and efficient system management.
