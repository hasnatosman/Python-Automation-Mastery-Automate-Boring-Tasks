import os
import shutil
from pathlib import Path

file_exists = os.path.exists('example.txt')
print(f"Does example.txt exist? {file_exists}")

folder_exists = os.path.exists('my_folder')
print(f'Does my_folder exist? {folder_exists}')