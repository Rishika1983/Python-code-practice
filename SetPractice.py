# Convert the list ['rap','house','electronic music', 'rap'] to a set:

L1 = ['rap','house','electronic music', 'rap']
s1 = set(L1)
print("Converting list to set")
print (s1)

# Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) = sum(B)

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print("Addition is differeent in list and set")
print("the sum of A is:", sum(A))
print("the sum of B is:", sum(B))

#Create a new set album_set3 that is the union of album_set1 and album_set2:

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
print("Union of sets")
print(album_set3)

# Find out if album_set1 is a subset of album_set3:
print(" checking Subset")
if album_set1.issubset(album_set3):
    print("Set1 is the subset of set3")
else:
    print("Set1 is not the subset of set3")
