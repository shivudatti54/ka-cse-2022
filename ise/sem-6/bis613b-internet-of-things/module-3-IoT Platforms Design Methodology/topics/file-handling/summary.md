# File Handling in Python for IoT

=====================================

### Overview

File handling in Python is essential for IoT applications that need to log sensor data, store device configurations, buffer data during network outages, and manage structured data in CSV and JSON formats. The with statement (context manager) is the recommended approach for safe file operations.

### Key Points

- **File Modes:** r (read), w (write/overwrite), a (append), r+ (read/write), rb/wb (binary); append mode is most common for IoT logging
- **Context Managers:** Always use the with statement to ensure files are properly closed even if exceptions occur
- **Reading Methods:** read() for entire file, readline() for single line, readlines() for list of lines, iteration for line-by-line processing
- **CSV Handling:** Use csv.writer/csv.reader for structured tabular sensor data; DictReader enables named field access
- **JSON Handling:** Use json.dump/json.load for IoT configuration files and data exchange; JSON is the standard IoT data format
- **Data Buffering:** Store sensor readings locally in files when network connectivity is unavailable, then transmit when restored
- **Exception Handling:** Always handle FileNotFoundError, PermissionError, and JSONDecodeError in IoT file operations

### Important Concepts

- CSV for time-series sensor data storage and export
- JSON for device configuration files and data interchange
- Data buffering pattern: write locally when offline, read and transmit when online, clear buffer after success
- Log rotation to prevent disk full conditions on resource-constrained IoT devices

### Notes

- Always use context managers (with statement) rather than manual open/close to prevent resource leaks
- Choose the right format: JSON for configuration and API payloads, CSV for time-series data logs
- Implement proper exception handling for all file operations, as IoT devices may have unreliable storage
