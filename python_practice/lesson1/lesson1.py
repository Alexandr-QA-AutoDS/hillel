print("Hello world!")

my_int = 10
another_int = my_int
print(id(another_int))

my_float = 15.3
print(type(my_float))

#my_sum = int(my_int + my_float)
my_sum = my_int + my_float
my_sum = int(my_sum)
print(my_sum)

my_string = "Hello"
my_list = [1, 2, 5.9, True, [1, 0], ]
my_tuple = (1, 2, None)
me_set = {1, 2, False}
my_dict = {"key": "value", "key2": {"sub_key": "sub_value"}}

my_bool = True
my_none = None

my_variable = None
print(my_variable)
my_variable = my_int + my_float
print(my_variable)

# ctrl + /

# snake_case - іменування змінних
# CamelCase - іменування класів
# UPER_SNAKE - з великої літери, _ між словами, іменування констант

MY_VARIABLE = 10
print(MY_VARIABLE)
MY_VARIABLE = "Hello"
print(MY_VARIABLE)

my_var = 10

_ = "Trash variable"

BASE_PAGE_URL = "google.com"
# ctrl + alt + l - формутувати код
sum_ = 5 + 10
diff_ = 15 - 10
mult = 5 * 12
div = 50 / 5

sum([1, 2, 3])

print(sum_)
print(diff_)
print(mult)
print(div)

# = - оператор присвоєння
# == - оператор порівняння, повертає True/False

'''
if sum_ == 15:
    print("sum is equal to 15")
    if div == 0:
        print("zero divination")
'''

my_name, my_age = "Alex", 30
# print("Hello", my_name, end="")
# print("Hello", my_name)

copy_age, copy_name = my_age, my_name

print("Hello my name is", my_name, "My age is", my_age)

print(copy_name,copy_age)