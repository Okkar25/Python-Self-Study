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

# print(os.getlogin())
# print(os.getpid())
# print(os.getppid())


# with open("stary night.jpg", "rb") as file:
#     content = file.read()
#     print(content)
    


# --------------------------------------------------------------------------------------------------

# net ninja
# fileObject.seek(offset[, whence])


characters = ["Mario", "Luigi", "Mushroom", "Toad", "Peach", "Yoshi"]
more_characters = ["Diddy Kong", "Donkey Kong", "Wuffle"]


def write_characters_to_file(filename):
    # open file
    # file = open(filename, "w")
    file = open(filename, "w+") # can also read and write
    
    # write to file
    for name in characters:
        file.write(name + "\n")
        
    # append to file
    file = open(filename, "a+")
    for name in more_characters:
        file.write(name + "\n")
        
    # read the file
    # file = open(filename, "r")
    # content = file.read()
    # print(content)
    
    file.seek(0,0)
    content = file.read()
    print(content)
    
    # close the file
    file.close()
    
    return

def main():
    write_characters_to_file("characters.txt")


if __name__ == "__main__":
    # main()
    pass
    
    

# =========================================================


# pathlib module (can also use os module)
# from pprint import pprint
# import pathlib

# pprint(dir(pathlib))


# * parents=True
# Purpose: This argument ensures that if any of the parent directories in the path do not exist, they are also created.
# For example, if you are trying to create the directory "A/B/C", but "A" and "B" do not exist, setting parents=True will create both "A" and "B" as well as "C". If you do not use parents=True, the operation will fail if the parent directories don’t exist.


# * exist_ok=True
# Purpose: This argument allows the program to ignore the error that would occur if the directory already exists.
# Without exist_ok=True, calling mkdir() on an existing directory would raise a FileExistsError. By setting exist_ok=True, the method ensures that if the directory already exists, the program will proceed without any issues.


from pathlib import Path

file = open("characters.txt", "r")

def create_path():
    script_dir = Path(__file__).parent
    # print(script_dir.parent)
    # print(script_dir)
    
    # file path
    path = script_dir / "characters"

    # making the directory
    path.mkdir(parents=True, exist_ok=True) 

    return 

def main():
    create_path()

if __name__ == "__main__":
    main()



# =========================================================



from pathlib import Path

def create_path():
    script_dir = Path(__file__).parent
    
    path = script_dir / "characters"
    path.mkdir(parents=True, exist_ok=True) 
    
    path = path / "delta.txt"
    # file = open(path, "w")
    file = path.open("w")
    file.write("Supernova")
    
    file = path.open("a+")
    file.write(" is a hero")
    
    # file.seek(0,0)
    # content = file.read()
    # print(content)
    
    file = path.open("r")
    content = file.read()
    print(content)
    
    file.close()
    
    # easy way
    path.write_text("This is writing into file directly")
    content = path.read_text()
    print(content)
    
    return 

def main():
    create_path()

if __name__ == "__main__":
    # main()
    pass


# =========================================================


from pathlib import Path 

def open_file():
    path = Path(__file__).parent
    
    path = path / "does" / "not" / "exist"
    
    # path.open("w") # create folder and files 
    try:
        file = path.open("r")
        content = file.read9
        print(content)
        file.close()
    except FileNotFoundError:
        print(f"{path} does not exist")
    except Exception as e:
        print(f"Unexpected error : {e}")

def main():
    open_file()
    
if __name__ == "__main__":
    # main()
    pass


# =========================================================



from pathlib import Path 

def open_file():
    path = Path(__file__).parent / "characters" / "characters.txt"
    
    data = ["apple", "orange", "peach", "grape", "melon"]

    # context manager 
    with path.open("w+") as file:
        for fruit in data:
            file.write(fruit + "\n")
           
        file.seek(0,0) 
        content = file.read()
        print(content)
        
def main():
    open_file()
    
if __name__ == "__main__":
    # main()
    pass


# =========================================================


from pathlib import Path
import json
from pprint import pprint

characters = {
    "characters" : [
        {"id": 1, "name":"Zhask", "role":"Mage"},
        {"id": 2, "name":"Khaleed", "role":"Fighter"},
        {"id": 3, "name":"Lesley", "role":"Marksman"},
        {"id": 4, "name":"Atlas", "role":"Tank"},
        {"id": 5, "name":"Angela", "role":"Support"},
    ]
}

path = Path(__file__).parent / "characters.json"

def write_json():
    with path.open("w") as json_file:
        json.dump(characters, json_file, indent=4)

def read_json():
    with path.open("r") as json_file:
        # content = json_file.read()     # return str 
        content = json.load(json_file) # return dict
        return content


def main():
    write_json()
    data = read_json()
    print(data, type(data))

if __name__ == "__main__":
    main()
    
    
1,920,000
    
1,818,750

101,250


