num = int(input("Enter a number: "))

if num == 0 or num == 1:
    print(num, "is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            print("Factor:", i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

    
