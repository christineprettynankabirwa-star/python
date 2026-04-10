

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