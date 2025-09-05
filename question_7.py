list1 = [5, 4, 5, 1, 4, 6, 0, 7, 9]
list2 = [5, 8, 2, 8, 9, 4, 6, 3]

intersection = []
for item in list1:
    if item in list2 and item not in intersection:
        intersection.append(item)

print("Intersection:", intersection)