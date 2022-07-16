my_String = "  blablaPython    Boys"

# wrong way modifying string.

"""my_String.strip()
my_String.removeprefix("blabla")
my_String.removesuffix("Boys")
print(my_String)"""

# right way assigment.

my_String = my_String.strip()
my_String = my_String.removeprefix("blabla")
my_String = my_String.removesuffix("Boys")
print(my_String)