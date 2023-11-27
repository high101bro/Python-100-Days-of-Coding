#! /usr/bin/env python3

import os

# Iterate through range
for i in range(1,101):
    # Format the dir name
    dir_name = f"{os.getcwd()}/{i:03d}"
    # print(dir_name)

    # Create the dirs
    os.makedirs(dir_name, exist_ok=True)
print(f"Directories created: {os.listdir()}")

