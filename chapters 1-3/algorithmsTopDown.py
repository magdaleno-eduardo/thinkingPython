def raiseTuition():
    #Initialize passes to zero
    #Initialize failures to zero
    #Initialize student counter to one

    #While student counter is less than or equal to ten
        #Input the next exam result
        #If the student passed
        #    Add one to passes
        #else
         #   Add one to failures
       #Add one to student counter

    #Print the number of passes
    #Print the number of failures

    #If more than eight students passed
    #    Print “Raise tuition”

    #inicial varibales
    passes = 0
    failures = 0
    studentCount = 1

    #calculations
    while studentCount <= 10:
        result = input("Enter result (1 = pass, 2 = fail): ")
        result = int(result)
        if result == 1:
            passes = passes + 1
        else:
            failures = failures + 1
        studentCount = studentCount +1

    print("Passed: ", passes)
    print("Failed: ", failures)

    if passes > 8:
        print("Raise tuition")
    else:
        print("Start expelling Students")


raiseTuition()

