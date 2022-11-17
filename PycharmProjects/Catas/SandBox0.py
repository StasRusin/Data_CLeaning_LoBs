from collections import Counter

# input of list
lst = [1, 2, 3, 1, 2, 5, 3, 4, 3, 6]
print("Input list : ", lst)

lst1 = Counter(lst).keys()
print("output list : ", lst1)
print("No of unique elements in the list are:", len(lst1))