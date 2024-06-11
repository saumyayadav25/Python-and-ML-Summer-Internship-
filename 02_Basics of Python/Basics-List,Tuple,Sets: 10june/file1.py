# LIST
# Create a simple list
list1=[1,2,3,4,"abc", True,False, 11.89,4+5j]
print("list is:", list1)
# Creating an empty list
list2=[]
print(list2)
# List in python is also a class. A list object can be also instantiated by List class constructor by invoking list()
str1="Hello All!"
# To convert this string directly to list, we can invoke list()
newList=list(str1)
print("The list formed from str is:",newList)
# Properties of List: ordered, mutable, allows duplicate values
list1=[7,8,9,4,"abc", True,False, 11.89,4+5j]
print("first element of list1:", list1[0])
print("second element of list1:", list1[1])
print("last element of list1:", list1[-1])
print(list1[1:6])
print(list1[-8:])
print(len(list1))
list1.append("new value")
print(list1)
# To add new element at a specific position in list: insert()
list1.insert(3,20)
print(list1)
# extend()
list2=[7,8,9,'Go']
list1.extend(list2)
print("List1 after extend(): ",list1)
print("List concatenation:",list1+list2)
# List repetition
print("list repeat: ", list2*3)
# common operators for sequences: +, *, slicing index->[:]
# list modifications
print("original list:", list2)
list2[2]=30
print("updated list:",list2)
list1[2:5]=[30,'hello ', 'bye',11] #11 will be added while values on index 2,3,4 will be replaced
print(list1)
# Remove a particular element , eg: "bye"
list1.remove("bye")   #remove only first occurrence 
print(list1)
# count occurence of elements
print("Count of occurrence of 7: ", list1.count(7))
# sort a list: same datatype values
list3=[3,5,1,7,9,2,6,11,10,7,8]
list3.sort() 
print(list3)
# sort in descending order
list3.sort(reverse=True)
print(list3)
# create a copy of list
new_list = list1.copy()
print(new_list)
# check if both these lists are same or not
print(list1==new_list)

# TUPLE
tup1= (1,2,3,'helo',11.55,True,5+2j)
print(tup1)
new_tuple=tuple(list2)
print(new_tuple)
str1="hello"
new_tuple1=tuple(str1)
print(new_tuple1)
# create an empty tuple
tup1=()
print(tup1, type(tup1))
# create  tuple with only single element
tup2=(1)
print(type(tup2))
tup2=(1,)
print(tup2)
values=1,2,3,4,'hello' #tuple is default datatype in python
print(type(values))
# Properties of tuple: ordered, immutable, allows duplicate value
tup1= (1,2,3,'helo',11.55,True,5+2j)
print("first element of tup1:",tup1[0])
print(tup1[1:6])
print(tup1[-5:])
print(tup1[-5::-1])
# to find the number of elements in tuple
print(len(tup1))
# membership in tuple
print("Helo" in tup1)
print("hello" not in tup1)
# cannot remove element directly in tuple, but u can remove entire tuple
del tup2
# count(): count number of times an element occurs
# index(): search for index of 1st occurrence of an element , if not present then it gives error
tup3= (1,2,3,'helo',11.55,True,5+2j,'helo')
print(tup3.count('helo'))
print(tup3.index('helo'))

# SET  : unordered
# constructor call:set()
set1={1,2,3,4,"hello",1,2,True}
print(set1)
set2=set()
set3={}
print(type(set2),type(set3))
# To add new elements in set: add()
set1={1,2,3,4,5,6,7,8,9}
print(set1)
set1.add(10)
set1.add(99)
print(set1)
# update(): to add elements from another list or tuple in a set
set1.update(list2)
print(set1)
set2={222,333}
set1.update(set2)
print(set1)
# remove() : gives error if element not present
print(set1.remove(5))
print(set1)
# discard() : doesnt give error if element is not present
set1.discard(5)
print(set1)
# set operations: union, intersection, difference
