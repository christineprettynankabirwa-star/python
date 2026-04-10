

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
print(f"You are most welcome, {name}!")
print(f"You are {age} years old now")


letters_list = ['a','b','c','d']
print(f"Letter in position 3 of list is {letters_list[2]}")
print ("Items in the set")
for letter in letters_set:
    print(letter)
print ("Items in the list")
for letter in letters_list :
    print(letter)
try:
    print(f"Letter in position 3 of list is {letters_set[2]}")
except Exception as e:
    print (e)