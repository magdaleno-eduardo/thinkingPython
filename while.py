def test():
    product = 2
    while product <= 1000:
        product = 2 * product
        print(product)


def average_testScore():
#pseudocode
    #set total to zero
    #set grade counter to one
    #while grade countr is less than or equal to ten
        #input next grade
        #add grade into total
        #add one to grade count
    #set the class average to the total divided by ten
    #print the class average

    total = 0
    gradeCounter = 1

    #while function
    while gradeCounter <=10:
        grade = input("Enter grade: ")
        grade = int(grade) #convert input into integer
        total = total + grade
        gradeCounter = gradeCounter + 1

    #calculate average and print
    average = total / 10
    print("Class average is ", average)

#test()
average_testScore()