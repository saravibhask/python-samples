def checkPrime(n):
    for x in range(2, n):
        if n % x == 0:
            print(n, "is NOT a prime number"); #x, 'n/x :', n/x);
            break;
    else:
        # loop fell through without finding a factor
        print("Yes!", n, "is a prime number.");
    return;

num = int(input("Enter a number : "));

if num == 1:
    print("A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.")
elif num < 2 and num != 1:
    print("Enter a number greater than 1.");
else:
    checkPrime(num);
