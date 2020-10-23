#use the for structure to sum all the even integers from 2 to 100
def sumItAllUp():
    sum = 0
    for number in range( 2, 101, 2):
        sum += number

    print("Sum is: ", sum)


#A person invests $1000 in a savings account yielding 5 percent interest. Assuming that all
#interest is left on deposit in the account, calculate and print the amount of money in the
#account at the end of each year for 10 years. Use the following formula for determining
#these amounts:
#a = p ( 1 + r ) n
#where
#p is the original amount invested (i.e., the principal),
#r is the annual interest rate,
#n is the number of years and
#a is the amount on deposit at the end of the nth year.

def compoundInterest():
    principal = input("Enter inicial investment: ")
    principal = int(principal)

    rate = input("Enter interst rate: ")
    rate = int(rate) / 100

    print("Year %21s" % "amount on deposit")

    for year in range(1, 11):
        amount = principal * (1.0 + rate) ** year
        print("%4d%21.2f" % (year, amount))



#sumItAllUp()
compoundInterest()