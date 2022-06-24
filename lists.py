# Lists are very similar to arrays. 
# They can contain any type of variable, and 
# they can contain as many variables as you wish
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

# accessing list items
print(mylist[0])
print(mylist[1])

# Iterating over a list
for x in mylist:
    print(x) # 1,2,3

# Lists can be joined with the addition operators:
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers) # [1,3,5,7,2,4,6,8]

# Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:
print([1,2,3] * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]