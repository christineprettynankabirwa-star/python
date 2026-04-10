

my_age = 12
id(my_age)


import datetime
today = datetime.datetime.today().replace(microsecond=0)
print ("This is " + str(today)) 
print ("Today is " + str(today)) # quite easily done 
print(today)

import keyword
print (keyword.kwlist)