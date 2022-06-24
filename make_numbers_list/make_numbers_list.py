# Creates a text file "inventory.txt" in an existing folder "inventory" in
# the user's home directory if this file does not already exist and fills it
# with numbers "1:", "2:", ..., "10:", each separated by two newlines.

import os
import sys

user_file_path: str = os.path.expanduser("~")
dirname: str = "inventory"
filename: str = "inventory.txt"
absolute_filepath: str = os.path.join(user_file_path, dirname, filename)
number: int = 10

if os.path.isfile(absolute_filepath):
    print(f"The file {absolute_filepath} already exists. Do you want to override it [y|n]?")
    answer: str = input()
    if answer != "y" and answer != "Y":
        sys.exit(0)

with open(absolute_filepath, "w") as inv_file:
    inv_file.writelines("\n")
    for i in range(1, number+1):
        inv_file.writelines(f"{i}:\n\n\n")
