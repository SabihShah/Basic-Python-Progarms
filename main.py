# Swap Two Numbers

a = 5
b = 6

(a, b) = (b, a)

print("a =", a, "b =", b)

------------------------------------------

# Calculator

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

operations = input("Enter operation: ")

if operations == "+":
    print(x, "+", y, "=", x+y)
elif operations == "-":
    print(x, "-", y, "=", x-y)
elif operations == "*":
    print(x, "*", y, "=", x*y)
elif operations == "/":
    print(x, "/", y, "=", x/y)
else:
    print("Invalid Operation")
    
-------------------------------------------

# Fibonacci Series

x = int(input("Enter number of iterations: "))

a = 0
b = 1

print(a)
print(b)

for i in range(2,x):
    c = a + b
    a = b
    b = c
    print(c)
   
---------------------------------------------

# Factorial

x = int(input("Enter number: "))
a = 1
for i in range(1, x+1):
    a = a*i
    
print(a)

-----------------------------------------------

# Check String Operations

a = "Sabih Shah"

print(len(a))
print(a[0])
print(a[-1])
print(a[::])
print(a[0:len(a):2])

-------------------------------------------------

# Maze

print("")
print("Welcome to the game!")
print("")

turn_1 = str(input("Left or Right: "))
if turn_1 == "right" or "Right":
    print("Continue to right")
else:
    print("Wrong Choice, Game Over")
    quit()

turn_2 = str(input("Left or Right: "))
if turn_2 == "left" or "Left":
    print("Continue to left")
else:
    print("Wrong Choice, Game Over")
    quit()

turn_3 = str(input("Left or Right: "))
if turn_3 == "right" or "Right":
    print("Continue to right")
else:
    print("Wrong Choice, Game Over")
    quit()

turn_4 = str(input("Left or Right: "))
if turn_4 == "right" or "Right":
    print("Continue to right")
else:
    print("Wrong Choice, Game Over")
    quit()

turn_5 = str(input("Left or Right: "))
if turn_5 == "right" or "Right":
    print("Congratulations")
else:
    print("Wrong Choice, Game Over")
