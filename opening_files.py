
text = "r for read file, w for write, a for append"

with open("test.txt", "w") as file:      # w for write file, r for read file, a for append/add new text
    file.write(text)