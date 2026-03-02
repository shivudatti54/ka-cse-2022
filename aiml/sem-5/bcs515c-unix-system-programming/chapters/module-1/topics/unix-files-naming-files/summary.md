# Unix Files: Naming Files

### Key Concepts

- **File name**: a sequence of characters that uniquely identifies a file
- **File system**: a way of organizing and storing files on a Unix system

### File Naming Rules

- **File name length**: maximum of 255 characters (excluding directory path)
- **Characters allowed**: alphanumeric characters (a-z, A-Z, 0-9), periods (.), underscores (\_)
- **Special characters**: not allowed (e.g. /, \, :, \*, ?, <, >, |, )

### Path and Directory Naming Rules

- **Path length**: maximum of 4096 characters (excluding file name)
- **Directory name length**: maximum of 255 characters
- **Characters allowed**: same as file names
- **Special characters**: not allowed

### Important Formulas and Definitions

- **File name format**: `/path/to/directory/file_name`
- **File system hierarchy**: `/`, `/usr`, `/bin`, `/lib`, etc.
- **Path separator**: `/`

### Theorems

- **No two files can have the same name**: uniqueness of file names is guaranteed by the file system
- **No two directories can have the same name**: uniqueness of directory names is guaranteed by the file system

### Quick Revision Tips

- Use only alphanumeric characters, periods, and underscores in file and directory names
- Keep file and directory names short (less than 255 characters)
- Use forward slashes (`/`) as path separators
- Avoid using special characters in file and directory names
