#Day 2: 30 days of python programming
firstname = "Habib"
lastname = "Yusuf"
fullname = firstname + lastname
country = "Nigeria"
city = "Kaduna"
age = 25
year = 1998
is_married= True
is_true = True
is_light_on = True
department,level = "Computer Science", 400

print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(department))
print(type(level))

#to find the length of the firstname
print(len(firstname))
#the below line is used for comparing between the two variables
print(firstname==lastname)

#Declare 5 as num_one and 4 as num_two
num_one, num_two = 5,4
#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)
#Subtract num_two from num_one and assign the value to a variable diff
diff=num_one-num_two
print(diff)
#Multiply num_two and num_one and assign the value to a variable product
product = num_two*num_one
print(product)
#Divide num_one by num_two and assign the value to a variable division
division = num_one/num_two
print(division)
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two%num_one
print(remainder)
#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one**num_two
print(exp)
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division=num_one//num_two
print(floor_division)



#The radius of a circle is 30 meters.
radius = 30
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
pi =22/7
area_of_a_circle= (pi * (radius**2))
print(area_of_a_circle)
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle= (2*pi*radius)
print(circum_of_circle)

#Take radius as user input and calculate the area.
radius=int(input("input radius"))
area_of_a_circle= (pi*(radius**2))
print(area_of_a_circle)


#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

firstname= input("Enter first name")
lastname= input("Enter lastname")
country= input("Enter the name of your country")
age=int(input("Enter your age ")) 
print(firstname)
print(lastname) 
print(country)
print(age)

