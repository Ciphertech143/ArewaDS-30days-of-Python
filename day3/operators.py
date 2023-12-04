age: int = 25

height: float= 1.2
complex_number = 2-1j

b=float(input("enter base: "))
h= float(input("enter height: ")) 
area = (0.5 * b * h)
print(area)

a = int(input("enter side a: "))
b=int(input("enter side b: "))
c = int(input("enter side c: "))
print("The perimeter of the triangle is ", a+b+c)

#Get length and width of a rectangle
width = int(input("Enter length"))
length = int(input("Enter length"))
area=length*width
perimeter=2*(length+width)
print(area)
print(perimeter)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
 
length= int(input("input length"))
width=int(input("input width"))
area= length*width
perimeter = 2 * (length + width)

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = int(input("input radius"))
pi=3.142
area= pi*r*r
c=(2*pi*r)


# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope (m) refers to the coefficient of x
slope = 2

# y-intercept (b) is the constant term
y_intercept = -2

# To find the x-intercept, let y = 0
x_intercept = (0 - y_intercept) / slope

# Displaying the results
print(f"Slope (m): {slope}")
print(f"Y-intercept (b): {y_intercept}")
print(f"X-intercept: ({x_intercept}, 0)")

#Slope is (m=y2-y1/x2-x1). Find the slope and Euclidean distance between (2,2) and point (6,10)

x1= 2
x2= 6
y1=2
y2=10
m= ((y2-y1)/(x2-x1))
Ec_distance=  ((x1-y1)**2)+ ((x2-y2)**2)
print("slope is: ", m)
print("Euclidean distance is: ", Ec_distance)

# Compare the slopes in tasks 8 and 9.
print ("slope in 8  is same as slope in 9 ", slope==m)
print("slope in 8 is greater than slope in 9: ", slope>m)
print("slope in 8 is less than slope in 9: ", slope < m)

#calculate the value of y(y=x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

print("the below will calculate the value of y(y=x^2 + 6x + 9)" )
x= int(input("Enter value of x: "))
y= ((x**2)+ (6*x) +9)
print("the value of y is: ", y)

print("when x is -3 it makes y 0")
x=-3
y= ((x**2)+ (6*x) +9)
print("the value of y is: ", y)



#Find the length of 'python' and 'dragon' and make a falsy comparison statement
print(len("python"))
print(len("dragon"))
print(len("python")>len("dragon"))


#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on is in dragon and python is ", "on" in "dragon" and "on" in "python")



#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence
print("jargon" in "I hope this course is not full of jargon")


# There is no 'on ' in both dragon and python
print("There is no on in dragon and python is ", "on" not in "dragon" and "on" not in "python" )

#Find the length of the text python and convert the value to float and convert it to string.
print(str(float(len("python"))))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print("To check if a number is even you will use the modulus a sit returns a remainder")
xE = int(input("type number"))
if (xE % 2==0):
    print("The result shows its an even number as its remainder is zero", xE%2)
else:
    print("The result is odd")    

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print("floor division of 7 and 3 is ", 7//3)
print((7//3)==(2.7))

#Check if type '10' is equal to type of 10
print(type('10'))
print(type(10))
print(type('10')==type(10))

#Check if int('9.8) is equal to 10
print(int(9.8)==(10))

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour"))
print ("Your weekly earning: ", hours-rate_per_hour)


#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = input("Enter number of years you lived: ")
seconds_in_year = 365 * 24 * 60 * 60
total_second_lived = years * seconds_in_year
total_possible_seconds = years * seconds_in_year   
print("You have lived for:", total_possible_seconds, "seconds")


#Write a python script that displays the following table
def power (num, exp):
    return num**exp

print("1 1 1 1 1")
for i in range (2,6):
    output = f"{i} 1 {i} {power(i, 2)} {power(i,3)}"
    print(output)
