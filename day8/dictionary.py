# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Bush'
dog['color'] = 'Brown'
dog['breed'] = 'Rotwhiler'
dog['legs'] = 4
dog['age'] = 5

# Create a student dictionary
student = {
    'first_name': 'Habib',
    'last_name': 'Yusuf',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'Android Development'],
    'country': 'Nigeria',
    'city': 'Kaduna',
    'address': 'No. 23 Shagalle Close, Kabala West, Kaduna'
}

# Get the length of the student dictionary
student_length = len(student)
print("Length of student dictionary:", student_length)

# Get the value of skills and check the data type, it should be a list
skills_value = student['skills']
print("Skills:", skills_value)
print("Data type of skills:", type(skills_value))

# Modify the skills values by adding one or two skills
student['skills'].extend(['HTML', 'CSS'])

# Get the dictionary keys as a list
keys_list = list(student.keys())
print("Dictionary keys as list:", keys_list)

# Get the dictionary values as a list
values_list = list(student.values())
print("Dictionary values as list:", values_list)

# Change the dictionary to a list of tuples using items() method
dict_to_tuples = list(student.items())
print("Dictionary as list of tuples:", dict_to_tuples)

# Delete one of the items in the dictionary
del student['address']
print("Dictionary after deleting an item:", student)

# Delete the entire student dictionary
del student

