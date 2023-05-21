
# A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.
######### Method	Description #############
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

myTuple = (1,2,3,8,6,8,2,5,9,1,2)
print(myTuple[1]) 
print(3 in myTuple) # returns bool

print(myTuple.index(2))
print(myTuple.count(2))

