def addStudent(studentData):
    studentData
# make this function add a student to the "database"
# this function will only add a student if there is no student associated with the new T-number
def modifyStudent(student_dict):    
    pass
# make this function modify an existing student in the "database"
# this function is roughly the same as addStudent() except the check for the T-number is the opposite. we can only modify if the T-number already exists
def viewStudents(student_dict):
    pass
# make this function list all of the students in the "database"
# this should be organized in a nice and neat way
# do not just print the dictionary, traverse through both the inner and outer dictionaries and print each item on a new line, like my example
def removeStudent(student_dict):
    pass
# make this function remove a student, given the T-number
# this function should only remove a student if the T-number exists
def menu():
    print(
'''TN Tech University Student Database
Please make a selection:
1. View all current students
2. Enter new student data
3. Remove student data
4. Modify student data
5. Quit'''
    )

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
    while True:
        menu()
        userInput = input("Selection: ")
    # call menu() to print options
    # use input() to get user input
    # use an if / elif block to decide which other function to call
    # NOTE: remember that dictionaries are passed by alias/referenc

if __name__ == "__main__":
    main()