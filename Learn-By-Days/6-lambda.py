# A lambda function is a small anonymous function.
# * A lambda function can take any number of arguments, but can only have one expression.

d = {
    "a" : 2,
    "b" : 3,
    "c" : 1
}

x = dict(sorted(d.items(), key= lambda item : item[1]))
# print(d.items())


# ** Syntax
# ** lambda arguments : expression

def add_func(x):
    return x + 5 
# print(add_func(5))

# x = lambda a : a + 5
# print(x(5))

# y = lambda x : x * 10
# print(y(3))


# Lambda functions can take any number of arguments

multiply = lambda a, b : a + b 
# print(multiply(12, 8))

x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))


# * Why Use Lambda Functions?

# * The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

# def my_func(n):
#     return lambda a : a * n # anonymous function

# doubler = my_func(2)
# print(doubler(10))

def my_func(n):
    return lambda a : a * n

doubler = my_func(2)
tripler = my_func(3)

# print(doubler(10))
# print(tripler(10))



# *** Use lambda functions when an anonymous function is required for a short period of time.


lambda x,y : x + y # anonymous function
# lambda functions are not bound to identifiers 

add = lambda x,y : x + y
# print(add(5,10))

# IIFE
(lambda x,y : x + y)(10,20)
# print((lambda x,y : x + y)(10,20))


# return max value 

def max_func(a,b):
    if (a > b):
        return a   
    else:
        return b 

# print(max_func(10,5))
# print(max_func(10,50))


max_lambda = lambda x, y : x if x > y else y 
# print(max_lambda(10,5))
# print(max_lambda(10,50))


(lambda x, y : x if x > y else y )(50,100)
# print((lambda x, y : x if x > y else y )(50,100))



# ----------------------------------------------------------------------------------------------



# * recreating map function with lambda function 


# * return a list of result
def my_map(my_func, my_iter):
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return result

nums = [1,2,3,4,5]

cubed = my_map(lambda x : x**3, nums)
# print(cubed)




# * return a list of lambda functions 
def my_map(my_iter):
    result = []
    for item in my_iter:
        new_item = lambda x, item=item : item**x  # return lambda functions # hardcoded inside
        result.append(new_item)                   # appending lambda functions into result []
    return result

nums = [1,2,3,4,5]

cubed = my_map(nums)

# result = [lambda func, lambda func, ..... , lambda func]
for func in cubed: 
    pass
    # print(func(3))
    


# ----------------------------------------------------------------------------------------------




age_check = lambda age : True if age >= 18 else False
# print(age_check(20))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(x):
    return x ** 2

result = list(map(square, nums))
result1 = list(map(lambda x : x ** 2, nums))
# print(result)

values = [
    (1, "b", "hello"),
    (3, 'a', "world"),
    (2, "c", "ok")
]

sorted_values = sorted(values, key= lambda item : item[1])
# sorted_values = sorted(values, key= lambda item : item[1] + item[2])
# print(sorted_values)





