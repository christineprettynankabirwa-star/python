reg_no = input("Enter your Reg No\n")
components = reg_no.split("/")
print(components[0])
print(components[1])
print(components[2])
if len(components) > 3:
    print(components[3])

students = { 
    "25/U/26619":{"name":"KAHUMA WALID", "age": 20, "hall":"Lumumba", "Town":"Hoima", "Sex":"M","Course":"BCSC"},
    "24/U/03567/PS" : "EMMANUEL MUHAME",
    "25/U/31546/PS" : "ONGOL CESTO",
    "24/U/26202" : "KATO TREVOR"
}
print ("Name",students ["25/U/26619"]["name"])
print ("Age",students ["25/U/26619"]["age"])


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