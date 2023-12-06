# Given sets and list
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print("Length of it_companies:", len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("Updated it_companies:", it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Dell', 'HP'])
print("Multiple IT companies added:", it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print("Company removed:", it_companies)


print("What is the difference between remove and discard")
print("remove will raise an error if the element is not found in the set")
print("discard will not raise an error if the element is not found in the set")

 



# Join A and B
join_A_B = A.union(B)
print("Join A and B:", join_A_B)

# Find A intersection B
intersection_A_B = A.intersection(B)
print("A intersection B:", intersection_A_B)

# Is A subset of B
print("A is a subset of B:", A.issubset(B))

# Are A and B disjoint sets
print("A and B are disjoint sets:", A.isdisjoint(B))

# Join A with B and B with A
join_A_with_B = A.union(B)
join_B_with_A = B.union(A)
print("Join A with B:", join_A_with_B)
print("Join B with A:", join_B_with_A)

# What is the symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_difference)

# Delete the sets completely
del it_companies, A, B

# Convert the ages to a set and compare the length of the list and the set
age_set = set(age)
print("Length of age list:", len(age))
print("Length of age set:", len(age_set))



sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
num_unique_words = len(unique_words)
print("Number of unique words:", num_unique_words)

