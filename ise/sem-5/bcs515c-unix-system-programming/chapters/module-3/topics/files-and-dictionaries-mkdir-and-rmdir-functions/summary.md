# **Files and Dictionaries: mkdir and rmdir Functions**

- **mkdir function:**
  - Creates a new directory with the specified name.
  - Returns 0 if successful, non-zero otherwise.
  - Example: `mkdir new_directory`
- **rmdir function:**
  - Deletes an empty directory with the specified name.
  - Returns 0 if successful, non-zero otherwise.
  - Example: `rmdir empty_directory`

## **Key Concepts:**

- **Directory**
  - A collection of files and subdirectories.
  - Created using `mkdir`
- **Subdirectory**
  - A directory contained within another directory.
  - Example: `/home/user/documents/subdir`
- **Empty directory**
  - A directory with no files or subdirectories.
  - Can be deleted using `rmdir`

## **Important Formulas and Definitions:**

- **Directory creation formula:** `mkdir dir_name`
- **Directory deletion formula:** `rmdir dir_name`
- **File system hierarchy standard (FHS) definition:** "A file system is a collection of files and directories that are stored on a storage device."

## **Theorems:**

- **Dir creation theorem:** If `mkdir dir_name` is executed successfully, then `dir_name` exists in the file system.
- **Dir deletion theorem:** If `rmdir dir_name` is executed successfully, then `dir_name` does not exist in the file system or is empty.
