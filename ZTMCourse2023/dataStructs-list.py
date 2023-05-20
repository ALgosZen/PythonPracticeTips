list1 = ['i', 'am' ,'suresh']
# copy list1 to list2
list2 = list1[:]

list2[2] = 'sam'
print(list2)
print(list1)

# setting list2 as list1 will make both reference same . for modify
list2 = list1 
list2[2] = 'sridhar'
print(list1)
print(list1)
