import shutil

# copyfile() = copies contents of file
# copy() = copyfile + permission mode + destination can be a dictionary
# copy2() = copy() + copies metadata (files creation and modification times

shutil.copyfile("C:\\Users\\xdido\\Desktop\\UID.txt", "test.txt")         #source, destination    copies source at destination
