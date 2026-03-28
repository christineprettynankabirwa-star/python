reg_no = input("Enter your Reg No\n")
components = reg_no.split("/")
print(components[0])
print(components[1])
print(components[2])
if len(components) > 3:
    print(components[3])

mark = input("Enter your mark or X to exit\n")
while mark.lower() != "x":
    mark = int(mark)
    if mark < 0 or mark > 100:
        print("This grade is invalid")
    elif mark < 31: 
        print("Your grade is", "F9")
    elif mark < 41:
        print("Your grade is ","P8")
    elif mark < 51:
        print("Your grade is ","P7")
    elif mark < 61:
        print("Your grade is ","C6")
    elif mark < 71:
        print("Your grade is ","C5")

    else :
        print("Your grade is", "D1")
    mark = input("Enter your mark or X to exit\n")
print("Exiting, you entered X")