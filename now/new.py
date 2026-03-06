reg_no = input("Enter your Reg No\n")
components = reg_no.split("/")
print(components[0])
print(components[1])
print(components[2])
if len(components) > 3:
    print(components[3])