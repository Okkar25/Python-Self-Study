# import csv

# def load_data(filename):
#     data = []
    
#     with open(filename) as file:
#         person_data = csv.reader(file, delimiter=",")
#         next(person_data) # skip the header
        
#         for row in person_data:
#             data.append(row)
            
#         return data
    
# new_list = load_data("data.csv")
# print(new_list) 

# for line in new_list:
#     print(line)


# Name,Age,City
# Alice,30,New York
# Bob,25,Los Angeles
# Charlie,35,Chicago

# [
#   ["Alice", "30", "New York"],
#   ["Bob", "25", "Los Angeles"],
#   ["Charlie", "35", "Chicago"]
# ]

import csv 

# with open("names.csv", mode="w") as csvfile:
#     fieldnames = ["id","first_name", "last_name"]
    
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     writer.writeheader()
#     writer.writerow({"id":1,"first_name":"Okkar", "last_name": "Aung"})
#     writer.writerow({"id":2,"first_name":"Bobby", "last_name": "Hudson"})
#     writer.writerow({"id":3,"first_name":"Alex", "last_name": "Mason"})


# import csv 

# names = [
#     {"id":1,"first_name":"Okkar", "last_name": "Aung"},
#     {"id":2,"first_name":"Bobby", "last_name": "Hudson"},
#     {"id":3,"first_name":"Alex", "last_name": "Mason"}
# ]
    
# with open("names.csv", mode="w") as csvfile:
#     fieldnames = names[0].keys()
    
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     writer.writeheader()
#     # for row in names:
#     #     writer.writerow(row)

#     writer.writerows(names)


# --------------------------------------------------------------------------------------

    
read_csv = open("numbers.csv").read()
read_csv = open("numbers.csv").readline()
read_csv = open("numbers.csv").readlines()

read_csv = open("numbers.csv").readlines()[2]
read_csv = open("numbers.csv").readlines()[2][3]

read_csv = open("numbers.csv").readlines()[2].split(",")
read_csv = open("numbers.csv").readlines()[2].split(",")[1]

read_csv = eval(open("numbers.csv").readlines()[2].split(",")[1])

# print(read_csv, type(read_csv))


def get_cell(col_index, row_index, filename):
    with open(filename) as csvfile:
        return eval( csvfile.readlines()[row_index].split(",")[col_index] )

# # print(get_cell(2, 4, "numbers.csv"))


# --------------------------------------------------------------------------------------


import csv 

def get_value(filename, row_index, col_index):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        
        return data[row_index][col_index]

value = get_value("numbers.csv", 3, 1)
# print(value)


# custom context manager 

# class MyContextManager:
#     def __enter__(self):
#         print("Entering the context")
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting the context")

# # Usage
# with MyContextManager() as cm:
#     print("Inside the context block")


# ----------------------------------------------------------------------------------------



# import csv 

# with open("names.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)
    
#     for row in csv_reader:
#         print(row[2])


# * reading from a csv file and writing to new csv file and then reading it again 

# import csv 

# with open("names.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
    
#     with open("new_names.csv", "w", newline="") as new_file:
#         csv_writer = csv.writer(new_file, delimiter="-")
        
#         for row in csv_reader:
#             csv_writer.writerow(row)
            
# with open("new_names.csv", "r") as new_csv:
#     new_reader = csv.reader(new_csv, delimiter="-")
#     next(new_reader)
    
#     for line in new_reader:
#         print(line)

# import csv 

# with open("names.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
    
#     with open("new_names.csv", "w", newline="") as new_file:
#         csv_writer = csv.writer(new_file, delimiter="\t")
        
#         for row in csv_reader:
#             csv_writer.writerow(row)
            
# with open("new_names.csv", "r") as new_csv:
#     new_reader = csv.reader(new_csv, delimiter="\t")
#     next(new_reader)
    
#     for line in new_reader:
#         print(line)


# * using DictReader and DictWriter 

# import csv 

# with open("names.csv") as csv_file:
#     # csv_reader = csv.reader(csv_file, delimiter=",")
#     csv_reader = csv.DictReader(csv_file, delimiter=",")
    
#     for row in csv_reader:
#         print(row)
        # print(row["email"])
        # print(row.items())
        # print(row.keys())
        # print(row.values())

# import csv 

# with open("names.csv") as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter=",")
    
#     with open("second_names.csv", "w") as new_file:
#         fieldnames = ["id", "name", "email"]
        
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",")
        
#         csv_writer.writeheader()
        
#         for row in csv_reader:
#            csv_writer.writerow(row) 


# with open("second_names.csv") as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter=",")
    
#     for row in csv_reader:
#         print(row)


# * Pros of using DictReader / DictWriter => can filter out unwanted data  

# import csv 

# with open("names.csv") as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter=",")
    
#     with open("second_names.csv", "w") as new_file:
#         fieldnames = ["id", "name"] # deleting the email header 
        
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",")
        
#         csv_writer.writeheader()
        
#         for row in csv_reader:
#            del row["email"] # deleting the specific lines (email)
#            csv_writer.writerow(row) 


# with open("second_names.csv") as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter=",")
    
#     for row in csv_reader:
#         print(row)


# * json

import json 

my_data = {
    "name" : "Okkar Aung",
    "age": 23,
    "occupation": "Software Developer"
}

with open("output.json", "w+") as json_file:
    json.dump(my_data, json_file, indent=4)
    
    json_file.seek(0,0)
    content = json_file.read()
    print(content)


