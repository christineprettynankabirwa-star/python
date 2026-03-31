ages = [20,30,3,25,16,1,20]
sorted_ages = sorted(ages)
print(f"Ages: {ages}")
print(f"Sorted Ages: {sorted_ages}")
print(f"Lowest Age: {sorted_ages[0]}")
print(f"Highest Age: {sorted_ages[len(sorted_ages)-1]}")

print()
letters_set = {'a','e','b','c','a','d'}
i = 0
for letter in letters_set:
    print(f"Letter in position {i} is {letter}")
    i += 1

letters_list = list(letters_set)
i = 0
while i<5:
    print("--------")
    print ("Letters_set",letters_set)
    print ("Letters_list",letters_list)
    i += 1
print("End") 

a,b,c = 1,15,10
if b < c:
    print('b is less than c')
    if a<b:
        print('a is less than b')
else:
    print('c is greater than b')
    