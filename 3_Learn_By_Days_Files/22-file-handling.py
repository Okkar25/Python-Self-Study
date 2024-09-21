# Python File Open

# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.

# * File Handling

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# f = open("demofile.txt")

# f = open("demofile.txt", "rt")


# --------------------------------------------------------------------------------------------------


# Python File Open

# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("C:/Users/Okkar Aung/OneDrive/Desktop/Python_Learn/3_Learn_By_Days_Files/demofile.txt", "r")
# f = open("./demofile.txt", "r")
# print(f.read())

import os 
# print(os.getcwd())


# * Read Only Parts of the File

# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

f = open("C:/Users/Okkar Aung/OneDrive/Desktop/Python_Learn/3_Learn_By_Days_Files/demofile.txt", "r")
# print(f.read(6))


# * Read Lines

f = open("C:/Users/Okkar Aung/OneDrive/Desktop/Python_Learn/3_Learn_By_Days_Files/demofile.txt", "r")
# print(f.readline())
# print(f.readline())
# print(f.readlines())


# * By looping through the lines of the file, you can read the whole file, line by line:

# for line in f:
#     print(line)


# * Close Files
# It is a good practice to always close the file when you are done with it.
# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

f = open("C:/Users/Okkar Aung/OneDrive/Desktop/Python_Learn/3_Learn_By_Days_Files/demofile.txt")
# print(f.readline())
f.close()

with open("C:/Users/Okkar Aung/OneDrive/Desktop/Python_Learn/3_Learn_By_Days_Files/demofile.txt", "r") as f:
    data = f.read()
    # print(data)

 
# --------------------------------------------------------------------------------------------------


# * Python File Write
# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
# Note: the "w" method will overwrite the entire file.

# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# f = open("demofile2.txt", "w")
# f.write("I am writing something new.")
# f.close()

#open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())


# * Create a New File

# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

# f = open("myfile.txt", "x")

# f = open("myfile.txt", "w")
# f.write("This wil be my newly created file.")
# f.close()

# f = open("myfile.txt", "a")
# f.write("This wil be my newly created file.")
# f.close()

# f = open("myfile.txt", "r")
# print(f.read())
# f.close()


# --------------------------------------------------------------------------------------------------


# * Python Delete File
# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:

# import os
# print(os.getcwd())
# os.remove("hello.txt")


# * Check if File exist:

import os

# if os.path.exists("hello1.txt"):
#     os.remove("hello1.txt")
# else:
#     print("The file cannot be found.")


# * Delete Folder / Build new folder

# To delete an entire folder, use the os.rmdir() method:

# print(os.path.exists("hello.txt"))

# print(os.listdir())

# os.mkdir("file_editor")
# os.rmdir("file_editor")

# print(os.getcwd())
# print(os.listdir())
# os.rename("file_photoshop", "file_editor")


# ======================== Problem ========================


# os.mkdir("file_editor")
# current_dir = os.getcwd()

# new_dir = os.path.join(current_dir, "file_editor")
# os.chdir(new_dir)

# # current_dir = os.getcwd()
# # print(current_dir)

# open("new_file.txt", "x")

# f = open("hello.txt", "w")
# f.write("Hello World!")
# f.close()

# f = open("hello.txt", "r")
# print(f.read())


# =========================================================


# * 1. File and Directory Operations:

# os.getcwd()           : Returns the current working directory.
# os.chdir(path)        : Changes the current working directory to path.
# os.listdir(path)      : Lists all files and directories in the specified directory.
# os.mkdir(path)        : Creates a new directory at the specified path.
# os.remove(path)       : Removes (deletes) the file at the specified path.
# os.rmdir(path)        : Removes the directory at the specified path (only if it's empty).
# os.rename(src, dst)   : Renames a file or directory from src to dst.


# * 2. Path Manipulation:
# os.path.join(path, *paths): Joins one or more path components into a single path.
# os.path.exists(path): Checks whether the given path exists.
# os.path.isfile(path): Returns True if the path is a regular file.
# os.path.isdir(path): Returns True if the path is a directory.
# os.path.basename(path): Returns the base name of the file (the last part of the path).
# os.path.dirname(path): Returns the directory name of the path.

import os

cur_dir = os.getcwd()
new_dir = os.path.join(cur_dir, "myfile.txt")
# print(new_dir)

x = os.path.isfile(cur_dir)
x = os.path.isfile(new_dir)

x = os.path.isdir(cur_dir)
x = os.path.isdir(new_dir)
# print(x)


# C:\Users\Okkar Aung\OneDrive\Desktop\Python_Learn\3_Learn_By_Days_Files
#["C:\Users\OkkarAung\OneDrive\Desktop\Python_Learn\", "3_Learn_By_Days_Files"]
# ["3_Learn_By_Days_Files"]

cur_dir = os.getcwd() 
x = os.path.dirname(cur_dir) 
y = os.path.basename(cur_dir) 

# print("current name - ",cur_dir)
# print("dirname - ", x) 
# print("basename - ", y) 

print(os.getlogin())
# print(os.getpid())
# print(os.getppid())

