# __name__ == "__main__" 
# to check whether a Python file is being run directly or being imported as a module in another file

# When a Python file is executed, Python sets the __name__ variable

# If the file is being run directly (e.g., python myfile.py), __name__ is set to '__main__'.

# If the file is being imported as a module in another script (e.g., import myfile), __name__ is set to the name of the module ('myfile' in this case).

def greeting():
    print("This is from mymodule")

if __name__ == "__main__":
    # This block will only run if this file is executed directly
    print("This is running directly")
    greeting()
    
    
# print("This is running directly")
# greeting()

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

import random
# print(random.choice(houses))





    
