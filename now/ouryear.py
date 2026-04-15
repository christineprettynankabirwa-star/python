

my_age = 12
id(my_age)


import datetime
today = datetime.datetime.today().replace(microsecond=0)
print ("This is " + str(today)) 
print ("Today is " + str(today)) # quite easily done 
print(today)

import keyword
print (keyword.kwlist)

yob = input("Enter your year of birth \n")
def compute_age(yob):
    age = 2025-int(yob)
    return age
age = compute_age(yob)   

print(f"You are {age} years old now")


letters_list = ['a','b','c','d']
print(f"Letter in position 3 of list is {letters_list[2]}")
print ("Items in the set")
for letter in letters_list:
    print(letter)
print ("Items in the list")
for letter in letters_list :
    print(letter)

    
try:
    print(f"Letter in position 3 of list is {letters_list[2]}")
except Exception as e:
    print (e)

# items = ['cow', 'needle', 'hay', 'key']
# for item in items:
# 	if item == 'needle':
#                 print ('Needle found')

# def add_shipping(subtotal):
#     subtotal = subtotal/5
#     return subtotal

# units=50
# firstTotal= units *5
# total = add_shipping(firstTotal)
# print("your total is", total)

# def f(x):
#     global y
#     y=1
#     x = y+x
#     return x
    
# x=3
# y=4
# z=f(x)
# print('x is ',x)
# print('y is ',y)
# print('z is ',z)

# p=  int(input('Enter p \n'))
# q=  int(input('Enter q \n'))
# r=  int(input('Enter r \n'))
# if  (p % 2 ==1):
#     print(f"r = {p}")
# else:
#     print ('q')