def test():
    product = 2
    while product <= 1000:
        product = 2 * product
        print(product)


def average_testScore():
    # pseudocode
    # set total to zero
    # set grade counter to one
    # while grade countr is less than or equal to ten
    # input next grade
    # add grade into total
    # add one to grade count
    # set the class average to the total divided by ten
    # print the class average

    total = 0
    gradeCounter = 1

    # while function
    while gradeCounter <= 10:
        grade = input("Enter grade: ")
        grade = int(grade)  # convert input into integer
        total = total + grade
        gradeCounter = gradeCounter + 1

    # calculate average and print
    average = total / 10
    print("Class average is ", average)


def average_testScoreV2():
    # psuedocode for class average with sential controlled repetition

    # Initialize total to zero
    # Initialize counter to zero

    # Input the first grade (possibly the sentinel)
    # While the user has not as yet entered the sentinel
    # Add this grade into the running total
    # Add one to the grade counter
    # Input the next grade (possibly the sentinel)

    # If the counter is not equal to zero
    # Set the average to the total divided by the counter
    # Print the average
    # else
    # Print “No grades were entered”

    # python code
    total = 0
    gradecounter = 0

    # process phase
    grade = input("Enter grade, -1 to end: ")
    grade = int(grade)
    while grade != -1:
        total = total + grade
        gradecounter = gradecounter + 1
        grade = input("Enter grade, -1 to end: ")
        grade = int(grade)

    # termination phase
    if gradecounter != 0:
        average = float(total) / gradecounter
        print("Class average is ", average)
    else:
        print("No grades were entered.")

def average_testScoresV3():
    total = 0
    gradecounter = 0

    # process phase

    while 1:
        grade = input("Enter grade, -1 to end: ")
        grade = int(grade)

        #exit loop if user inputs -1
        if grade == -1:
            break

        total += grade
        gradecounter += 1

    # termination phase
    if gradecounter != 0:
        average = float(total) / gradecounter
        print("Class average is ", average)
    else:
        print("No grades were entered.")




# test()
# average_testScore()
#average_testScoreV2()
average_testScoresV3()
