n = int(input("Enter an integer : "))

def CheckDivisibleByFive(num):
    if num % 5 == 0:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

def CheckEven(num):
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

def CheckPrime(num):
    flag = False
    if num == 0 | num == 1:
        return False
    else:
        for i in range(2, num // 2):
            if num % i == 0:
                return False
    return True

if CheckPrime(n):
    print("Number is Prime")
else:
    print("Number is Not Prime")
CheckEven(n)
CheckDivisibleByFive(n)

