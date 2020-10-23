def main():
    #introduction
    print("This program calculates the future value of a 10-year investment")

    #valuue of capital
    capital = input("Enter inicial investment: ")

    #anual percentage rate
    apr = input("Enter the anual interest rate: ")

    #anual inflation
    inflation = input("Enter the anual inflation rate: ")

    #calculations of purchesing power of investment
    for i in range(10):
        apr = int(apr) / 100
        capital = int(capital)
        inflation = int(inflation) / 100
        capital = (capital / (1 + inflation)) * (1 + apr)
    print ("the amount in ten years is: ", capital)

main()