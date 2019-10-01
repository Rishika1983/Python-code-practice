#Implement a group_by_owners function that:
#Accepts a dictionary containing the file owner name for each file name.
#Returns a dictionary containing a list of file names for each owner name, in any order.


def group_by_owner(fileData):
    groupedResult = {}

    for i in fileData.items():

        if i[1] in groupedResult.keys():
            groupedResult[i[1]].append(i[0])
        else:
            groupedResult[i[1]] = [i[0]]

    return groupedResult


fileData = {'a.txt':'john', 'a.pdf':'rekha', 'b.txt': 'john', 'c.txt': 'john','d.txt': 'john', 'b.pdf': 'rekha', 's.txt': 'Sam'}
print(group_by_owner(fileData))