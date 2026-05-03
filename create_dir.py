import os
import shutil
from pathlib import Path

os.makedirs('my_folder', exist_ok=True)
print('Directory created')

os.makedirs('parent_folder/child_folder/grandchild_folder', exist_ok=True)
print('Nested directories created successfully.')