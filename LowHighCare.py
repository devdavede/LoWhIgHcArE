#!/usr/bin/python

import os
import sys

def walk(dir):
    # Dictionary to store files grouped by their lowercase names
    files = {}
    # List to store subdirectories
    directories = []

    # Print current directory being traversed
    print("Walk " + dir)
    
    # Iterate over items in the directory
    for path in os.listdir(dir):
        full_path = os.path.join(dir, path)  # Full path of the item
        if os.path.isfile(full_path):  # If it's a file
            # Store the file name in the files dictionary using lowercase name as key
            files.setdefault(path.lower(), []).append(path)
        elif os.path.isdir(full_path):  # If it's a directory
            # Add the directory to the list of directories
            directories.append(path)

    # Loop through files grouped by lowercase names
    for filename, paths in files.items():
        # If there are multiple files with the same lowercase name (i.e., duplicates)
        if len(paths) > 1:
            # Iterate over duplicate files, starting from the second one
            for i, path in enumerate(paths[1:], start=1):
                # Generate a new filename for duplicate file by prefixing it with "_<index>_"
                new_filename = "_" + str(i) + "_" + filename
                # Print renaming operation
                print("Rename " + os.path.join(dir, path) + " to " + os.path.join(dir, new_filename))
                # Rename the duplicate file
                os.rename(os.path.join(dir, path), os.path.join(dir, new_filename))

    # Recursively traverse subdirectories
    for directory in directories:
        walk(os.path.join(dir, directory))

if __name__ == "__main__":
    # Check if a directory path is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)
    # Start traversing the directory
    walk(sys.argv[1])
