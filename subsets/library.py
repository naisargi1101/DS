import itertools  
# Define the set  
s = [1, 2, 3, 4]  
k = 2  
# Find all subsets of size k using map and itertools.combinations  
subsets = list(map(lambda x: list(itertools.combinations(s, x)), range(0, len(s)+1)))  
# Flatten the list of subsets  
result = [item for sublist in subsets for item in sublist]  
# Print the subsets  
print(result)  