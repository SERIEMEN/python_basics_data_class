file = 'name.txt'

with open(file,'w') as digs:
    digs.write('oseriemen\n')
#print contents/ writing to the file

with open(file, 'r') as f_obj:
    for line in f_obj:
        print(line)
#reading from the file correctly, the r means you only want to look at the data not change it or overwrite it
# the with as block is called a content manager,
# Opening files takes up system memory,
# If your program opens a file and crashes before closing it, it can cause memory leaks or lock the file.
# The with block automatically handles closing the file for you the exact second the indented block of code finishes running,
# even if an error occurs.