import os
import shutil

# os.remove("test.txt")

path = "test.txt"
shutil.rmtree(path)             #deletes all files in the directory

try:
    os.remove("test.txt")
except FileNotFoundError:
    print(path + " path was not found")
except PermissionError:
    print("Permission not given")
else:
    print(path + "was deleted")


# to delete empty folder/directory

partdir = "C:\\Users\\xdido\\PycharmProjects\\pythonExcercises\\venv\\testdir"

try:
    os.rmdir(partdir)
except FileNotFoundError:
    print(partdir + " path was not found")
except PermissionError:
    print("Permission not given")
else:
    print("path was deleted")