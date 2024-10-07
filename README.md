# Folder Sync Tool

![Python](https://img.shields.io/badge/python-3.x-blue)

## Description
The **Folder Sync Tool** is a Python script that synchronizes the contents of a source folder with a replica folder. It ensures:
- **One-way synchronization** where the replica folder is an exact copy of the source.
- **File operations** like copying, updating, and removing files or folders.
- **Logging** all operations to a file and the console.

## Features
- Periodic folder synchronization.
- MD5-based file comparison.
- Automatic creation and removal of files and folders.
- Detailed logging of all actions.

## Requirements
- Python 3.x (no external libraries required).

## How to Install
1. Clone the repository:
    ```bash
    git clone https://github.com/JoaoLopes1234/folder-sync-tool.git
    cd folder-sync-tool
    ```
2. Ensure Python 3.x is installed:
    ```bash
    python --version
    ```

## How to Use
1. Navigate to the `src` folder:
    ```bash
    cd src
    ```

2. Run the script with the required arguments:
    ```bash
    python .\src\Folder_sync.py tests\origin tests\replica 5 src\log_file.txt
    ```

### Example Command
```bash
python .\src\Folder_sync.py tests\origin tests\replica 5 src\log_file.txt

```

## Logging

The **Folder Sync Tool** logs all operations to both the console and a specified log file. This logging feature provides visibility into file and folder operations during synchronization.

### Logging Features:
- **Operations Logged**: 
  - File copied or updated
  - File deleted
  - Directory created
  - Directory removed
