# Error Logging in Unix System Programming - Summary

## Key Definitions
- **Syslog**: A standard logging facility in Unix that provides a centralized mechanism for programs to report events
- **Facility**: An identifier indicating which system component generated a log message (LOG_USER, LOG_DAEMON, LOG_AUTH, etc.)
- **Priority**: The severity level of a log message (LOG_EMERG, LOG_ALERT, LOG_CRIT, LOG_ERR, LOG_WARNING, LOG_NOTICE, LOG_INFO, LOG_DEBUG)
- **syslogd**: The system daemon that receives and processes log messages from applications

## Important Formulas
- Priority construction: priority = facility | priority_level (e.g., LOG_USER | LOG_ERR)
- openlog() options can be combined using bitwise OR: LOG_CONS | LOG_PID | LOG_NDELAY

## Key Points
1. The syslog facility provides a standardized, centralized logging mechanism independent of terminal devices
2. Three main functions constitute the syslog API: openlog(), syslog(), and closelog()
3. openlog() is optional but recommended for setting program identity and logging options
4. The %m format specifier in syslog automatically inserts the error message corresponding to errno
5. For daemon processes, syslog is the only reliable method for reporting errors since they have no terminal
6. Common facilities include LOG_USER (user-level programs), LOG_DAEMON (system daemons), LOG_AUTH (security/authorization)
7. Log files are typically stored in /var/log with system-specific organization
8. LOG_PID option should be used to include process IDs in log messages for debugging multi-process applications

## Common Mistakes
1. Forgetting to call closelog() - this is not critical but good practice for resource cleanup
2. Using wrong facility codes - LOG_KERN should not be used by user programs
3. Not checking if openlog() succeeded - it returns void, so failures cannot be detected
4. Mixing up priority levels - LOG_DEBUG (7) is the lowest priority, not the highest
5. Trying to use stdout/stderr in daemon processes instead of syslog