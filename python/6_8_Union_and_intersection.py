def union(list1, list2):
    # Make list1 and list2 as set
    list1 = set(list1)
    list2 = set(list2)

    # Print list1, list2
    print("List 1= ", list1)
    print("List 2= ", list2)

    # Using inbuilt function union print the result
    print("Union of two list: ", list1 | list2)


def intersection(list1, list2):
    # Make list1 and list2 as set
    list1 = set(list1)
    list2 = set(list2)

    # Using inbuilt function intersection print the result
    print("Intersection of two list: ", list1 & list2)


# Declare two empty list list1 and list2
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]

# call the function union
union(list1, list2)

# call the function intersection
intersection(list1, list2)
