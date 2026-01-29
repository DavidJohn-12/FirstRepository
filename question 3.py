def power(x, y): #function for finding power
    return x**y

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]

valid_results=[] #empty list to store valid powers
for i,j in pairs: #iterating over each pair in the list
    if j < 0:
        continue #skips negative y values
    valid_results.append(power(i,j))

print(valid_results)