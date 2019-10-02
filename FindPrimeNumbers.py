from datetime import datetime

inputNumber = int(input("Enter a number : "))
primeNumbers = []

# Function to list prime numbers
def getPrimeNumbers(inputNumber):
    beginDateTime = datetime.now()
    print("Begin time : ", beginDateTime)
    for j in range(2, inputNumber):
        for k in range(2, j):
            if j % k == 0:
                break
        else:
            primeNumbers.append(j)
    endDateTime = datetime.now()
    print("End time : ", endDateTime)
    print("Total time taken : ", endDateTime - beginDateTime)


for i in range(2,inputNumber):
    if inputNumber % i == 0 and i < inputNumber:
        print("Entered number", inputNumber, "is a composite number")
        break
else:
    print("entered number", inputNumber, "is a prime number")

getPrimeNumbers(inputNumber)
print("There are total of", len(primeNumbers), "prime numbers")
#print(primeNumbers)

