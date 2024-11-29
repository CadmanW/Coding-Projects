# Cadman Warren
# 11/29/24
# CSC 1200 Travis Lee


# Add student
def addStudent(studentData):
    tnum = input("Enter new user ID number: ")
    name = input("Enter new user NAME field: ")
    username = input("Enter new user USERNAME field: ")
    major = input("Enter new user MAJOR field: ")

    if tnum in studentData.keys():
        print("User ID number already in use")
    else:
        studentData[tnum] = {
            "NAME": name,
            "USERNAME": username,
            "MAJOR": major
        }

# modify existing student
def modifyStudent(studentData):    
    tnum = input("Enter new user ID number: ")
    name = input("Enter new user NAME field: ")
    username = input("Enter new user USERNAME field: ")
    major = input("Enter new user MAJOR field: ")

    if tnum in studentData.keys():
        studentData[tnum] = {
            "NAME": name,
            "USERNAME": username,
            "MAJOR": major
        }
    else:
        print("User ID number does not exist")

# veiw students
def viewStudents(studentData):
    for studentID in studentData:
        print(f"\n{studentID}\n******\nNAME   -   {studentData[studentID]["NAME"]}\nUSERNAME   -   {studentData[studentID]["USERNAME"]}\nMAJOR   -   {studentData[studentID]["MAJOR"]}\n")

# remove existing student
def removeStudent(studentData):
    tnum = input("Please specify ID of student to remove: ")

    if tnum in studentData.keys():
        studentData.pop(tnum)
        print("Student Removed!")
    else:
        print("User ID number does not exist")

# print the UI options
def menu():
    print('''
TN Tech University Student Database
Please make a selection:
1. View all current students
2. Enter new student data
3. Remove student data
4. Modify student data
5. Quit
''')

# called after initializatiom
def main():
    studentData = {
        "T123": {
            "NAME":"Travis Lee",
            "USERNAME":"tlee",
            "MAJOR":"CSC"
        },
        "T124":{
            "NAME":"Jeremy Potts",
            "USERNAME":"jpotts",
            "MAJOR":"CHEM"
        }
    }

    # main loop
    while True:
        menu()
        userInput = input("Selection: ")

        match int(userInput):
            case 1:
                viewStudents(studentData)
            case 2:
                addStudent(studentData)
            case 3:
                removeStudent(studentData)
            case 4:
                modifyStudent(studentData)
            case 5:
                break
            case _:
                print("invalid input")

# call main
if __name__ == "__main__":
    main()