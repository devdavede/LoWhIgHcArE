# LowHighCare

## Overview
This Python script helps to identify and rename duplicate files within a specified directory and its subdirectories. It groups files with the same lowercase names and appends index numbers to the duplicates to distinguish them. The script recursively traverses the directory structure, identifying and renaming duplicate files to avoid conflicts.

## Prerequisites
- Python 3.x
- Operating system compatible with Python's `os` module

## Usage
1. Make sure you have Python installed on your system.
2. Download the script (`LowHighCare.py`) to your local machine.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script using the following command:

    ```
    python LowHighCare.py <directory_path>
    ```

    Replace `<directory_path>` with the path of the directory you want to scan for duplicate files.

6. The script will recursively search through the specified directory and its subdirectories, identifying duplicate files by their lowercase names. It renames the duplicate files with unique index numbers prefixed with underscores to avoid conflicts.

## Important Note
- Exercise caution while using this script, as it modifies file names within the specified directory. Make sure to double-check the directory path before executing the script.
- Ensure you have appropriate permissions to rename files within the specified directory.

## License
This script is released under the MIT License. See the [LICENSE](LICENSE) file for more details.
