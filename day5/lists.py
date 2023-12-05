# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
list_more_than_5 = [1, 2, 3, 4, 5, 6, 7]

# Find the length of your list
length_list_more_than_5 = len(list_more_than_5)
print(length_list_more_than_5)

# Get the first item, the middle item, and the last item of the list
first_item = list_more_than_5[0]
middle_item = list_more_than_5[length_list_more_than_5 // 2]
last_item = list_more_than_5[-1]
print(first_item, middle_item, last_item)

# Declare a list called mixed_data_types
mixed_data_types = ["YourName", 25, 170, "Single", "YourAddress"]



# Declare a list variable named it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
num_companies = len(it_companies)
print(num_companies)

# Print the first, middle, and last company
first_company = it_companies[0]
middle_company = it_companies[num_companies // 2]
last_company = it_companies[-1]
print(first_company, middle_company, last_company)

# Print the list after modifying one of the companies
it_companies[0] = "NewCompany"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("NewITCompany")

# Insert an IT company in the middle of the companies list
it_companies.insert(num_companies // 2, "MiddleITCompany")

# Change one of the it_companies names to uppercase (IBM excluded!)
for i in range(len(it_companies)):
    if it_companies[i].lower() != 'ibm':
        it_companies[i] = it_companies[i].upper()

# Join the it_companies with a string '#; '
joined_companies = '#; '.join(it_companies)
print(joined_companies)

# Check if a certain company exists in the it_companies list
company_to_check = "Google"
company_exists = company_to_check in it_companies
print(company_exists)

# Sort the list using sort() method
it_companies.sort()

# Reverse the list in descending order using reverse() method
it_companies.reverse()

# Slice out the first 3 companies from the list
first_3_companies = it_companies[:3]

# Slice out the last 3 companies from the list
last_3_companies = it_companies[-3:]

# Slice out the middle IT company or companies from the list
middle_company_or_companies = it_companies[num_companies // 2]

# Remove the first IT company from the list
it_companies.pop(0)

# Remove the middle IT company or companies from the list
it_companies.remove(middle_company_or_companies)

# Remove the last IT company from the list
it_companies.pop()

# Remove all IT companies from the list
it_companies.clear()

# Destroy the IT companies list
del it_companies



front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Joining the lists
full_stack = front_end + back_end

# Inserting Python and SQL after Redux
index_of_redux = full_stack.index('Redux')
full_stack.insert(index_of_redux + 1, 'Python')
full_stack.insert(index_of_redux + 2, 'SQL')

print(full_stack)



