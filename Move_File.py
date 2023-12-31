import os
import shutil

from_dir = "F:/1-Whitehat Jr/PYTHON/C-102/project/Downloads"
to_dir = "F:/1-Whitehat Jr/PYTHON/C-102/project/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, ext = os.path.splitext(file_name)

    if ext == '':
        continue

    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/'
        path3 = to_dir + '/' + file_name

        if not os.path.exists(path2):
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)
