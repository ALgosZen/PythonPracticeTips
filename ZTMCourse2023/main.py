#Data Types
# int, float, bool, str, list, tuple, set, dict
# import math
import datetime

# print( 5 // 4)

# #Math functions
# print(round(3.5))
# print(abs(-8.9))
# print(math.exp(3))
# print(3 ** 2)
# print( 3 * 2)
# print(math.ceil(3.21321312321321))
# print(math.copysign(2,3))
# # operator precedence
# # ** is highest, then multiplication/division, then addition/subtraction

# # guess output
# print((5 + 4) * 10 / 2) #45
 
# print(((5 + 4) * 10) / 2) #45

# print((5 + 4) * (10 / 2)) #45

# print(5 + (4 * 10) / 2) #25

# print(5 + 4 * 10 // 2) #25


# # augmented assignment operator
# counter = 0

# counter += 1
# counter += 1
# counter += 1
# counter += 1
# counter -= 1
# counter *=2

# #Before you click RUN, guess what the counter variable holds in memory!
# print(counter)

# # string concatenation

# # escape sequences
# weather = "\t It\'s \"kind of\" awesome \n \t sunny \r never"
# print(weather)

# formatted string
# name = 'sam'
# age = 22
# print(f"hi {name} . i'm {age} old")
# print("hi {0} . i'm {1} old".format('sam','22'))
# print("hi {name} . i'm {age} old".format(name='sam',age='22'))

# name = 'Cindy'
# amount = 50
# print(f"Hello {name}, your balance is {amount}.")


# print("Hello {}, your balance is {}.".format("Cindy", 50))

# print("Hello {0}, your balance is {1}.".format("Cindy", 50))

# print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

# print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))





# string is immutable , can be indexed and sliced
selfie = "0121213213217657abrakadabra"
#slicing
#selfie[start:stop:stepover]

# print(selfie[5])
# print(selfie[:2])
# print(selfie[18:])
# print(selfie[::2])
# print(selfie[:4])
# print(selfie[2:8])

birth_year = input('what year were you born?')
current_year = datetime.date.today().year
# print(type(current_year))
# print(type(birth_year))

age = current_year - int(birth_year)
print(f"you are {age} years old")
