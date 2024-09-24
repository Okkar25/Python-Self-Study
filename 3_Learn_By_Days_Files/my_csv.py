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

# print(get_cell(2, 4, "numbers.csv"))