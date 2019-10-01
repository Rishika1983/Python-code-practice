#Implement the unique_names method. When passed two lists of names,
# it will return a list containing the names that appear in either or both lists.
#The returned list should have no duplicates.


def unique_name(namelst1,namelst2):
    uniquelst = list(set(namelst1+namelst2))
    return (uniquelst)

list1 = ['jam', 'ram', 'ragul']
list2 = ['sita', 'ragul', 'sita']
print(unique_name(list1,list2))
