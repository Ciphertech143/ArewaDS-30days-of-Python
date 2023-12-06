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


ages = [19,22,19,24,20,25,26,24,25,24]
# Sort the list and find the min and max age
sorted_age= ages.sort()
print(sorted_age)
min_age = min(ages)
print(min_age)
max_age = max(ages)
print(max_age)
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
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',]
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

