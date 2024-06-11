# -----SET-----
# builtin methods of set
# all()->checks for the True set of boolean values;gives false if 0 is given
set1={True,True,True,1,1,0}
res=all(set1)
print(res)
list1=[True,True,1,1,-4,5]
res1=all(list1)
print(res1)
# any()->returns True if any of the element is True
res=any(set1)
print(res)
print(len(set1))
# max() and min()
set1={1,2,3,77,99,-11}
print(max(set1))
print(min(set1))
# sum()
print(sum(set1))

# Mathematical set operations: union, Intersection, Symmetric Difference, Subtraction
set1={1,2,3,4,5}
set2={4,5,6,7,8,9}
# union() and | operator
print("using union():",set1.union(set2))
print("using | operator:", set1 | set2)
# intersection() and & operator
print("using intersection():",set1.intersection(set2))
print("using & operator:",set1 & set2)

# difference() A-B:the elements of A subtratcting the common elements with B
# the result must contain those elements of A which are not present in B
# difference() and - operator
print("using difference() A-B:",set1.difference(set2))
print("using - operator:",set1 - set2)
print("using difference() B-A:",set2.difference(set1))
print("using - operator:",set2 - set1)
# intersection_update(), union_update(), difference_update()
set1.intersection_update(set2)
print(set1)
set1={1,2,3,4,5}
set2={4,5,6,7,8,9}
set2.difference_update(set1)
print(set1)
print(set2)
# update()
set2.update(set1)
print(set1)
print(set2)
# symmteric_difference(): returns all the values present in given set data structures except the common values between them
set1={1,2,3,4,5}
set2={4,5,6,7,8,9}
print("symmetric difference:",set1.symmetric_difference(set2))
set1.symmetric_difference_update(set2)
print(set1)

# issuperset(), issubset(), isdisjoint()
set1={1,2,3,4,5}
set2={1,2,3,4,5,6,7,8,9,10}
set3={11,22,33,44}
print("if set1 is a subset of set2:", set1.issubset(set2))
print("if set1 is a superset of set2:", set1.issuperset(set2))
print("if set2 is a subset of set1:", set2.issubset(set1))
print("if set2 is a superset of set1:", set2.issuperset(set1))
print("if set1 and set2 are disjoint or not:", set1.isdisjoint(set2))
print("if set1 and set3 are disjoint:", set1.isdisjoint(set3))   #disjoint: no common elements

# pop():randomly deletes a value from set
set1={1,2,'abc',11.5,3,4,22,66,9}
print("the removed value is:", set1.pop())
print("the removed value is:", set1.pop())
print("the removed value is:", set1.pop())
set5={9}
set5.pop()
print(set5)
# set5.pop() ->gives error: pop from an empty set


# -----DICTIONARY-----
dict1={}
print(type(dict1))
dict1={'Ename':'Saumya', 'Age':19,'salary':1000000,'Houseno':20}
print("the dict values are:", dict1)
# access elements in dict
# with the help of keys
print("the emp name:", dict1['Ename'])
print("the salary is:", dict1['salary'])
# add new values to dictionary
dict1['Degree']=['B.Tech','MBA']
print(dict1)
print("The degrees are:", dict1['Degree'])
# update existing value
dict1['Age']=20
print(dict1)
# remove salary: use del property
del dict1['salary']
print(dict1)
# pop() method
res=dict1.pop('Age')
print("the popped value is:",res)
print(dict1)
print(len(dict1))
print("the keys are:", dict1.keys())
print("the values are:", dict1.values())
print("the items are:",dict1.items())

# get() method: to get a value corresponding to a key
print("the value of houseno:", dict1.get('Houseno'))
