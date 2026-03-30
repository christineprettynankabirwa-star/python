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