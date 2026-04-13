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
    

    numbers = [1,2,3,4,5,6]
for n in numbers:
    if n%2 != 0:
        print(n)

for i in range(2,12,2):
    print(i)     

x = 3
for j in range(x):
    for i in range(x):
        print(i)

x = 3
for j in range(x):
    for i in range(x):
        print(i)

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('work_supervisor', 'Workplace Supervisor'),
        ('acad_supervisor', 'Academic Supervisor'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    university_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
        