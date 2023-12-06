# Level 1
# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of siblings
brothers = ('Abubakr', 'Luqman')  
sisters = ('Maryam', 'Tawakkaltu', 'Napheesah', 'Sakeenah')   
print(brothers,sisters)

# Join brothers and sisters tuples
siblings = brothers + sisters
print(siblings)

# Count the number of siblings
num_siblings = len(siblings)
print(num_siblings)

# Modify the siblings tuple and add parents' names
father = 'Yusuf'
mother = 'Madinah'
family_members = siblings + (father, mother)
print(family_members)

# Level 2
# Unpack siblings and parents from family_members
siblings = family_members[:num_siblings]
parents = family_members[num_siblings:]
print (parents)

# Create fruits, vegetables and animal product tuples and join the three tuples and assign it to a variable called food_stuff_tp.  
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('meat', 'eggs', 'milk')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change food_stuff_tp tuple to a food_stuff_list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items
middle_item = food_stuff_lt[len(food_stuff_lt)//2]

# Slice out the first three items and last three items from food_stuff_lt
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# Delete the food_stuff_tp tuple completely
print(del food_stuff_tp)
 
