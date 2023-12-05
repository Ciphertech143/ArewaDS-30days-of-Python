# Level 1
# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of siblings
brothers = ('John', 'Alex')  # Imaginary brothers
sisters = ('Emily', 'Sophie')  # Imaginary sisters

# Join brothers and sisters tuples
siblings = brothers + sisters

# Count the number of siblings
num_siblings = len(siblings)

# Modify the siblings tuple and add parents' names
father = 'Michael'
mother = 'Sarah'
family_members = siblings + (father, mother)

# Level 2
# Unpack siblings and parents from family_members
siblings = family_members[:num_siblings]
parents = family_members[num_siblings:]

# Create tuples for different types of food
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('meat', 'eggs', 'milk')

# Join the three tuples
food_stuff_tp = fruits + vegetables + animal_products

# Change food_stuff_tp tuple to a list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items
middle_item = food_stuff_lt[len(food_stuff_lt)//2]

# Slice out the first three items and last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# Delete the food_stuff_tp tuple completely
del food_stuff_tp
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)

# Add the min age and the max age again to the list
ages.extend([min_age, max_age])

# Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    median_age = ages[n // 2]

# Find the average age
average_age = sum(ages) / len(ages)

# Find the range of ages
age_range = max_age - min_age

# Compare the value of (min - average) and (max - average), use abs() method
min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)

# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_countries = countries[len(countries) // 2 - 1 : len(countries) // 2 + 1]

# Divide the countries list into two equal lists
if len(countries) % 2 == 0:
    first_half = countries[:len(countries) // 2]
    second_half = countries[len(countries) // 2:]
else:
    first_half = countries[:len(countries) // 2 + 1]
    second_half = countries[len(countries) // 2 + 1:]

# Unpack the first three countries and the rest as scandic countries
country1, country2, country3, *scandic_countries = countries

print(f"Sorted Ages: {ages}")
print(f"Min Age: {min_age}, Max Age: {max_age}")
print(f"Median Age: {median_age}")
print(f"Average Age: {average_age}")
print(f"Age Range: {age_range}")
print(f"Min-Average Difference: {min_average_diff}")
print(f"Max-Average Difference: {max_average_diff}")
print(f"Middle Countries: {middle_countries}")
print(f"First Half: {first_half}")
print(f"Second Half: {second_half}")
print(f"First Three Countries: {country1}, {country2}, {country3}")
print(f"Scandic Countries: {scandic_countries}")

