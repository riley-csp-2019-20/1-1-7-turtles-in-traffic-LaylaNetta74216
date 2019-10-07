#   a117_grades.py

my_courses = ["English", "Math", "CS"]

check_grades = 0
while (check_grades < 0):
    print("Hello student.") 
    print("Enter your points for", my_courses, ".")

a = int(input("Points ->"))
for course in my_courses:
    if (a >= 90):
        print("A")
    elif (a >= 80):
        print("B")
    elif(a >= 70):
        print("C")
    elif (a >= 60):
        print("D")
    else:
        print("F")
    redo = input("Do you need to re-do these grades? (yes/no)")
    if (redo == "yes"):
        a = int(input("Points ->"))
    else:
        print("Ok, good job!")
        
