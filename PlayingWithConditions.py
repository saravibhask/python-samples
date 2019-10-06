# Author : Savith K
# Date : 9/20/2019
# Learning Python programming following Microsoft python tutorials

country = "India" #input("Enter your country : ");

if country.lower() == "usa":
    state = input("Enter your state :");

    if state.lower() in("az", "nm"):
        print("You live in South Western region of USA!");
    elif state.lower() in("ca", "nv"):
        print("You live in Western region of USA!");
    else:
        print("I'm sure you live somewhere in USA!");
else:
    print("Hmmm... you live in "+ country + " nice!");


def checkPrime(n):
    for x in range(2, n):
        if n % x == 0:
            #print(n, "is NOT a prime number"); #x, 'n/x :', n/x);
            break;
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number');

for i in range(2, 100):
    checkPrime(i);
    