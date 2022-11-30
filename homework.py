# Make a variable named item0 and set its value to the first item in the list below
mylist = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78]
item0 = 1

# Print the last item in this list
mylist = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78]
print(mylist[-1])

# The append() method allows you to add items to your lists. add the string "R" to the below list with append() method
mylist = ["Julia", "Python"]
mylist.append("R")
print(mylist)
# Add ["SQL", "Scala"] as a list to mylist
mylist.append(["SQl, Scala"])
print(mylist)
# insert "C++" to mylist to the index 1
print(mylist.insert(1, "C++"))
# Remove "Julia" from mylist
mylist.remove("Julia")
print(mylist)
# Reverse mylist
mylist.reverse()
print(mylist)
# Count how many "0" is there in list1
list1 = [0, 0, 1, 0, 0, 1, 6, 0, 1, 0, 2, 1, 6, 6, 1, 0, 16, 1, 18, 0,
         6, 2, 22, 1, 0, 6, 3, 6, 28, 1, 15, 0, 2, 16, 6, 1, 3, 18, 6,
         0, 5, 6, 21, 2, 1, 22, 46, 1, 42, 0, 16, 6, 13, 3, 2, 6, 18,
         28, 58, 1, 60, 15, 6, 0, 6, 2, 33, 16, 22, 6, 35, 1, 8, 3, 1,
         18, 6, 6, 13, 0, 9, 5, 41, 6, 16, 21, 28, 2, 44, 1]
count = 0
for i in list1:
    if i == 0:
        count += 1

print(count)
print(sum(list1))
