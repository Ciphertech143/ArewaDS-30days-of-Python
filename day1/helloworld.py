# Day 1 Challenge
    # The following are Exercises for Level 1 in the Python for 30days challenge
 

    #Question 2
print("addition of 3 and 4 is =", 3+4) #addition(+)
print("subtraction of 3 and 4 is =",3-4) #subtraction (-)
print("multiplication of 3 and 4 is =",3*4) #multiplication (*)
print("remainder of 3 and 4 is =",3%4) #modulus (%)
print("division of 3 and 4 is =",3/4) #division (/)
print ("exponent of 3 and 4 is =",3**4) #exponential (**)
print("floor divisionof 3 and 4 is =",3//4) #floor division (//)

    #Question 3
name = "Habib Yusuf"
family_name ="Yusuf's family"
country = "Nigeria"
joy = "I am enjoying 30 days of python"
print(name)
print(family_name)
print(country)
print(joy)

#Question 4: Checking data types of the following data
print(type(10))
print(type(9.8))
print(type (3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type (name))
print (type(family_name))
print (type(country))

#Exercise Level 3
# Number: Integer
num_integer = 3 + 4

# Number: Float
num_float = 3.0 + 4.0

# Number: Complex
num_complex = 3 + 4j

# String
my_string = "The sum of 3 and 4 is " + str(3 + 4)

# Boolean
is_valid = 3 < 4

# List
my_list = [3, 4, 5, 6]

# Tuple
my_tuple = (3, 4, 5, 6)

# Set
my_set = {3, 4, 5, 6}

# Dictionary
my_dict = {'3': 'three', '4': 'four'}



#Find an Euclidian distance between (2, 3) and (10, 8)
import math

# Define the coordinates of the two points
first_point= (2, 3)
second_point = (10, 8)

# To calculate the Euclidean distance using the distance formula
euclidean_distance = math.sqrt((second_point[0] - first_point[0]) ** 2 + (second_point[1] - first_point[1]) ** 2)

print(f"The Euclidean distance between {first_point} and {second_point} is {euclidean_distance:.2f}")



