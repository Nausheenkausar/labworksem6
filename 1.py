from statistics import mean 
num = [1,2,4,6,7]
average1 = sum(num)/len(num)
print(f"average is {average1}")
average2 = mean(num)
print("average",round(average2,3))

def conversion(c):
    f = (c * 1.8) + 32  # Convert Celsius to Fahrenheit
    return f

# Get the Celsius temperature from the user
celsius = float(input("Enter temperature in Celsius: "))

# Call the conversion function with the Celsius value
fahrenheit = conversion(celsius)

# Print the result
print(f"\nFahrenheit = {fahrenheit}")

def findPeri(a, b):
    p = 2*(a+b)
    return p

print("Enter Length and Breadth of Rectangle: ", end="")
l = float(input())
b = float(input())

res = findPeri(l, b)
print("\nPerimeter = {:.2f}".format(res))
