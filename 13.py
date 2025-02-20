a = int(input("Enter first number : " ))
b = int(input("Enter second number : " ))
print(f"GCD of {a} and {b} is =")
while b != 0 :
    temp = b
    b = a % b
    a = temp
print(a)
  
