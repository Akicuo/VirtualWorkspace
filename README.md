# VirtualWorkspace

**VirtualWorkspace** is a Python package that allows users to create, manage, and organize files and directories in a virtual workspace. It consists of three main classes: `File`, `Directory`, and `Workspace`, which work together to provide a structured environment for file management.

## Features

- Create and manage files with customizable content and emoji icons.
- Organize files within directories, allowing for nested structures.
- Easily list contents of directories and files.
- Search for files by name within directories.

## Installation

To install the VirtualWorkspace package, you can use pip:

```bash
pip install vws
```

## Usage
Here’s a quick example of how to use the VirtualWorkspace package:

```python
from vws import Workspace

# Create a new workspace
my_workspace = Workspace("My Workspace")

# Create directories
my_workspace.create_directory("Documents")
my_workspace.create_directory("Images")

# Create files
my_workspace.create_file("resume.pdf", "This is my resume content.")
my_workspace.create_file("photo.jpg", "This is a photo content.")

# List contents of the root directory
print(my_workspace.list_contents())

# List contents of a specific directory
print(my_workspace.list_directory_contents("Documents"))

# Read file content
print(my_workspace.read_file_content("resume.pdf"))
```
## Classes
File
Represents a file with a name, content, and an optional emoji icon.

## Directory
Represents a directory that can contain files and/or subdirectories. It provides methods to add files and directories, find files by name, and list its contents.

## Workspace
Represents a virtual workspace with a root directory. It allows users to create files and directories and provides methods to list and read contents.

## Contributing
If you would like to contribute to the development of VirtualWorkspace, feel free to fork the repository and submit a pull request. Any contributions, whether bug fixes, enhancements, or documentation improvements, are welcome!


## Author
Lyan
Email: admin@blackcoffee.lol
GitHub: Akicuo
