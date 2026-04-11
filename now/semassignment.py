
import os
your_reg_number = '2024/' #update your registration number
your_name = 'John Doe' #update your name

def print_menu():
    print("--------------------Menu--------------------")
    print("1 - Add student with marks")
    print("2 - Delete student, given an admin_no")
    print("3 - View statistics about the grades")
    print("4 - View student grades")
    print("5 - Edit student grades")
    print("6 - Print Gradebook")
    print("m - Print menu")
    print("c - Clear Screen")
    print("q - Quit system\n")

print()
print(f"Welcome to students Gradebook\nBy".upper())
print(f"{your_name} - {your_reg_number}\n")
import os
your_reg_number = '2024/' #update your registration number
your_name = 'John Doe' #update your name

def print_menu():
    print("--------------------Menu--------------------")
    print("1 - Add student with marks")
    print("2 - Delete student, given an admin_no")
    print("3 - View statistics about the grades")
    print("4 - View student grades")
    print("5 - Edit student grades")
    print("6 - Print Gradebook")
    print("m - Print menu")
    print("c - Clear Screen")
    print("q - Quit system\n")

print()
print(f"Welcome to students Gradebook\nBy".upper())
print(f"{your_name} - {your_reg_number}\n")

#Print menu for first time
print_menu()

#Print menu for first time
print_menu()

#initialize the gradebook
grade_book = dict()

while True:
    choice = input("\n--------------------\nEnter your choice\n")
    
    if choice == '1':
        #Code to add a student. Teacher/User should supply admin_no, name and optionally marks for SST, Maths, science and Eng

        print("Student added.") #Include details for added student and current number of students in grade book.
    
    elif choice == '2':
        #Add Code to delete a student. Teacher/User admin_no for student to delete
        print("Student deleted")
    
    elif choice == '3':
        #Add Code give the following gradebook statistics
        print("Mean marks for Maths: ")
        print("Mode mark for Maths: ")
        print("Modal frequency for Maths: ")
        print("Lowest mark for Maths: ")
        print("Highest mark for Maths: ")
        #Repeat the above output for SST and Eng
    
    elif choice == 'm':
        print_menu()
    
    elif choice == 'c':
        os.system('cls') #Only for windows
        
    elif choice == 'q':
        print('Bye bye')
        break
    
