

def main1():
    grade = input("Please Enter student\'s grade: ")
#pseudocode for testing if student passed examen
    #if student's grade is greater than or eual to 60
        #print "passed"
    #else
        #print "failed"

    #In Python
    grade = int(grade)
    if grade>= 60:
        print("Passed")
    else:
        print("failed")


def main2():
    grade = input("Please Enter student\'s grade: ")
#pseudocode for student's examen grade
    #If student’s grade is greater than or equal to 90
        #Print “A”
    #else
        #If student’s grade is greater than or equal to 80
            #Print “B”
    #else
        #If student’s grade is greater than or equal to 70
            #Print “C”
    #else
        #If student’s grade is greater than or equal to 60
            #Print “D”
    #else
        #Print “F”

#code in python
    grade=int(grade)
    if grade >= 90:
        print("Test Result: A")
    elif grade >= 80:
        print("Test Result: B")
    elif grade >= 70:
        print("Test Result: C")
    elif grade >= 60:
        print("Test Result: D")
    else:
        print("Test Result: F")

main1()
main2()

