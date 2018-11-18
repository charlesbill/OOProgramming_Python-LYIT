#Question1
python_mission = (
    "The mission of the Python Software Foundation is to promote, protect, " +
    "and advance the Python programming language, and to support and facilitate" +
    "the growth of a diverse and international community of Python programmers"
)
print(python_mission.count('s'))
stringPosition = python_mission.find("Python", python_mission.find("Python") + 1)
print(str(stringPosition))
print("The word returned is: {}".format(python_mission[25:34]))
findDiverse = python_mission.find("diverse")
if findDiverse != -1:
    # Not reached.
    print("diverse found")
else:
    print("diverse not found")

myNumberTest = "12345"
print(myNumberTest.isnumeric())
noOfCounts = python_mission.count('Python')
#Question 2
lastPosition = python_mission.rfind("Python")
print(str(lastPosition))
#Question 3
print("L" + format(2211, '08d'))
#Question 4 - Using Slice
student = (
    "rlennon:x:1234:1001:Ruth Lennon:/users/rlennon:/bin/bash"
)
intfirst = student.index(":");
intsecond = student.index(":", intfirst + 1);
intThird = student.index(":", intsecond + 1);
intFour = student.index(":", intThird + 1);
intFive = student.index(":", intFour + 1);
intSix = student.index(":", intFive + 1);
print(student[0:intfirst])
print(student[intfirst+1:intsecond])
print(student[intsecond+1:intThird])
print(student[intThird+1:intFour])
print(student[intFour+1:intFive])
print(student[intFive+1:intSix])
#Using the Split Methods
studentDetails = student.split(':')
for attribute in studentDetails:
        # print the word
        print(attribute)

