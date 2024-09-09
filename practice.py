# new_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# # [expression for item in iterables if condition == true]


# new_arr = ["hello world" for x in new_fruits]

# print(new_arr)


languages = ["JavaScript","Python","Java","PHP", "C++", "SQL", "Go","Ruby"]
vowels = "aeiou"


# for lang in languages:
#     has_vowel = False
    
#     for char in vowels:
#         if char in lang.lower():
#             has_vowel = True
#             break
        
#     if not has_vowel:
#         print(lang)




languages = ["JavaScript","Python","Java","PHP", "C++", "SQL", "Go","Ruby"]
# vowels = "aeiou"

# count_list = {}

# for lang in languages:
#     count_list[lang] = 0
    
#     for char in lang:
#         if char in vowels:
#             count_list[lang] += 1
       
            
# print(count_list)



# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,4,5,6,7]

# plt.plot(x,y, label = "Okkar's Graph")
# plt.legend()
# plt.show()


nums = [1,2,3,4,5]

new_list = list(map(lambda x : x ** 2, nums))

new_list = list(filter(lambda x : x % 2 == 1, nums))

# print(new_list)

# unpacking
# print(*nums)

[a, *b, c] = nums

# print(a , b, c)


def order_pizza(size, *toppings, **details):
    print(f"I want a {size}-sized pizza with the following toppings : ")
    for top in toppings:
        print(f"- {top}")
    
    print("\nDetails of the order : ")
    for k,v in details.items():
        print(f"- {k} : {v}")

# order_pizza("large", "cheese", "pepperoni", "sausage", delivery=True, tip=5)

