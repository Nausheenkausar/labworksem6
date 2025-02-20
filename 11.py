n = int(input("Enter a number: "))
chk = False
if n == 0:
    chk = True
fib = 0
a, b = 0, 1
while fib < n:
    fib = a + b
    if fib == n :
        chk = True
        break
    a = b
    b = fib
if chk:
    print(f"{n} is a fibonacci number")
else:
    print(f"{n} is not fibonacci number")
