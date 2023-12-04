#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string. 'Thirty Days of Python'
print('Thirty ' + 'Days '+ 'Of '+ 'Python')
#Concatenate the string 'Coding' 'for' 'all' into a single string. 
print('Coding '+'for '+'all')
company= "coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company= "Coding For All"
capitalized_company= company.capitalize()
titlecase_company = company.title()
swapped_company= company.swapcase()


#Replace the word coding in the string 'Coding For All' to Python
company= "Coding For All"
replaced_coding= company.replace("Coding", "Python")
print(replaced_coding)



#Change Python for Everyone to Python for All using the replace method or other methods
variable = "Python for Everyone"
replaced_sentence = variable.replace("Python for Everyone", "Python for All")
print(replaced_sentence) 

#Split the string 'Coding For All using space as the seperator (split()).
company= "Coding For All"
splitted_company= company.split()
print(splitted_company) 


#'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' split the string at the comma.
companies= 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
splitted_companies= companies.split(sep=',')
print(splitted_companies)


#What is the character at index 0 in the string Coding For All.
print("What character is at index 0 in 'Coding For All'")
company = "Coding For All"
print(company[0])


#What is the last index of the string Coding For All
print("The last index in coding for all is the below")
variable1 = "Coding for all"
last_index = variable1.rfind("Coding for all")
print(last_index) 


#What character is at index 10 in Coding for all
print("The character at index 10 is ")
company = "Coding For All"
print(company[10])

#Create an acronym or an abbreviation for the name "Python for Everyone"
name = 'Python For Everyone'
abbreviation = ''.join(word[0].upper() for word in name.split())
print("abbreviation for Python for Everyone is: ", abbreviation)

#Create an acronym or an abbreviation for the name "Coding For all"
name = "coding For all"
acronym = ''.join(word[0].upper() for word in name.split())
print("acronym for coding for all is: ", acronym)



#Use index to determine the position of the first occurence of C in Coding for all
name= "Coding for all"
substring= 'C'
first_occurrence = name.index(substring)
print("the index of the first ocurence of c is:", first_occurrence)

#Use index to determine the position of the first occurrence of F in Coding for all.
name= "Coding For all"
substring2 = 'F'
first_occurrence= name.index(substring2)
print("the index where F first occurred is :",  first_occurrence)

#Use rfind to determine the position of the last occurrence of I in coding for all people. Therefore if not found it returns -1
new_example= "Coding for all people"
last_occurence= new_example.rfind('I')
print("the last occurrence of I in coding for all people is :", last_occurence)

 
#Use index or find to find the position of the first occurrence of the word "because" in the following sentence: "You cannot end a sentence with because because because is a conjunction"
sentence = "You cannot end a sentence with because because because is a conjunction"
position_of_first_occurrence = sentence.find("because")
print("because first occured at index: ", position_of_first_occurrence)

#Use rindex to find the position of the last occurrence of the word because in the following sentence: "You cannot end a sentence with because because because is a conjunction."
sentence2 = "You cannot end a sentence with because because because is a conjunction."
end_sentence = sentence2.rindex('because')
print("because occurred lastly at index: ", end_sentence)


#Slice out the phrase "because because because" in the following sentence: "You canot end a sentence with because because because is a conjunction"
sentence ="You cannot end a sentence with a because because because is a conjunction"
phrase_to_sllice ="because because because"
sliced_phrase=sentence.find(phrase_to_sllice)
end_index = sliced_phrase + len(phrase_to_sllice)
result = sentence[sliced_phrase:end_index]
print("sliced phrase is: ", result)




#Find out the position of the first ocurence of the word 'because' in the folloiwng sentence: 'You cannot end a sentence because because is a conjunction'.
sentence ="You cannot end a sentence with a because because because is a conjunction"
first_occurrence = "because"
output = first_occurrence.index(first_occurrence)
print("where because first occured is: ", output)

#Slice out the phrase "because because because"in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence='You cannot end a sentence with because because because is a conjunction'
to_be_sliced= "because because because"
sliced_phrase2= sentence.find(to_be_sliced)
end_index2= sliced_phrase2  + len(to_be_sliced)
result= sentence[sliced_phrase2:end_index2]
print(result)

#Does "Coding For All" start with a substring coding?
variable="Coding For All"
substring="Coding"
result=variable.startswith("Coding")
print("Coding for all starts with the substring coding is: ", result)

#Does "Coding For All" ends with a substring coding?
variable="Coding For All"
substring="Coding"
result=variable.endswith("Coding")
print("Coding for all starts with the substring coding is: ", result) 

#' Coding For All ' remove the left and right training spaces in the given string
string=' Coding For All '
print(string.strip())

#Which of the following variables return True when we use the method isindentifier()

variable11 = "30DaysOfPython"
variable12 = "thirty_days_of_python"
print ("The first one prints: ", variable11.isidentifier())
print("The second one prints: ", variable12.isidentifier())

#The following list contains the names of some python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_string= '*'.join(libraries)
print(joined_string)

# Use the new line escape sequence to seperate the following sentences. I am enjoying this challenge. I just wonder what is next
print("I am enjoying this challenge. \n I just wonder what is next")

# Use a tab escape sequence to write the following lines. Name Age Country City
print("Name \t\t", "Age \t\t", "Country \t\t", "City")
print("Asabeneh \t", "250 \t\t", "Finland \t\t", "Helsinki" )


# Use the string formatting method to display the following: radius = 10 area = 3.14 * radius**2 
radius = 10 
area = (3.14 * radius**2)
print(f"The area of a circle with radius {radius} is {area} square meters.")

#Make the following using string formatting methods:
no1=8
no2=6
add= no1+no2
sub = no1-no2
mult = no1*no2
div = no1/no2
mod = no1%no2
floor_div= no1//no2
esp= no1**no2
print(f"{no1}+{no2}={add}")
print(f"{no1}-{no2}={sub}")
print(f"{no1}*{no2}={mult}")
print(f"{no1}/{no2}={div}")
print(f"{no1}%{no2}={mod}")
print(f"{no1}//{no2}={floor_div}")
print(f"{no1}**{no2}={esp}")




