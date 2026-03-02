### Learning Purpose: `su` command

**1. Why is this topic important?**
The `su` (substitute user) command is a fundamental security and administrative tool. Understanding its proper use is critical for system security, preventing unauthorized access, and enabling controlled privilege escalation for system maintenance. Misuse can lead to severe security breaches.

**2. What will students learn?**
Students will learn the syntax, functionality, and key options (`-`, `-c`) of the `su` command. They will distinguish between gaining a root shell and executing a single command as another user. The concept of the wheel group and its role in restricting `su` access will also be covered, emphasizing security best practices.

**3. How does it connect to other concepts?**
This topic directly builds upon core concepts of user management, file permissions (`chmod`, `chown`), and the principle of least privilege. It is a precursor to learning more sophisticated tools like `sudo` and is foundational for understanding user authentication, process ownership, and secure system administration.

**4. Real-world applications**
System administrators use `su` daily to perform tasks requiring root privileges, such as software installation, service configuration, and log file inspection. It is essential for managing multi-user systems, implementing security policies, and performing controlled administrative actions without sharing the root password.