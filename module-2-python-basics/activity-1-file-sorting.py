"""
Module 2 — Activity: File Sorting with os and shutil
Student: John Brian O. Pecson
Date: 9/27/26

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]

- This program sorts files by file extension. It scans all the files in
a source folder, checks the file's extension, the part after the
dot, like .pdf or .jpg, and then moves the file into a subfolder
named after that extension.


============================================
KEY VOCABULARY
============================================
- os module: this is the module I used to actually talk to the file system — like getting a list of everything in a folder
- shutil module: this is the one that actually moves the files around.
- file path: this is the address of the file like for example Users/Folder/Folder2/file.txt
- directory: another term for folder
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

def sort_files_by_extension(source_dir):
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
 
        if os.path.isdir(source_path):
            continue
 
        if "." in filename:
            folder_name = filename.split(".")[-1].lower()
        else:
            folder_name = "other"
 
        destination_dir = os.path.join(source_dir, folder_name)
        os.makedirs(destination_dir, exist_ok=True)
 
        shutil.move(source_path, os.path.join(destination_dir, filename))
        print(f"Moved {filename} -> {folder_name}/")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================

- I might want to be watchful for this, running it twice in a row because of the
os.path.isdir check, without that check, the second run
would try to sort the pdf/jpg/etc. folders it just created

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""