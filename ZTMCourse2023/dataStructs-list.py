# list1 = ['i', 'am' ,'suresh']
# # copy list1 to list2
# list2 = list1[:]

# list2[2] = 'sam'
# print(list2)
# print(list1)

# # setting list2 as list1 will make both reference same . for modify
# list2 = list1 
# list2[2] = 'sridhar'
# print(list1)
# print(list1)


basket = ['a','b','x','p','o','y','j','c','z','s','r','t','h']
# syntax for sort :list.sort(reverse=True/False, key=myFunc)
basket.sort()
print(basket.sort()) #prints NONE 
print(basket) #prints sorted basket from previous sort method
basket_new = sorted(basket)
print(basket_new)

###############################
from collections import namedtuple

Runner = namedtuple('Runner', 'bibnumber duration')
# the data that needs to be captured is the runner’s bib number and the number of 
# seconds runner took to finish the race:

runners = []
runners.append(Runner('2528567', 1500))
runners.append(Runner('7575234', 1420))
runners.append(Runner('2666234', 1600))
runners.append(Runner('2425234', 1490))
runners.append(Runner('1235234', 1620))

runners.sort(key=lambda x:getattr(x, 'duration'))
top_five_runners = runners[:5]
