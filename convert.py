#program to convert celsius temp to fahr.

def main():
    celsius= int(input("What is the C Temperature?"))
    fahrenheit= 9.0 / 5.0 * celsius + 32
    print ("the temperature is", fahrenheit, "degrees Fahren.")

main()