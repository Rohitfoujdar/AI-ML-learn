set = {1, 7, 9, 88, "Rohit"}

set.add(966)
set.remove(1)
print(set, type(set))

s1= {0, 1, 2, 3, 4, 5}
s2= {6, 7, 8, 9, 0}
print(s1.union(s2))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} (all unique elements)
print(s1.intersection(s2))  # {0} (common elements)
print(s1.symmetric_difference(s2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9} (either in s1 or s2, but not both)