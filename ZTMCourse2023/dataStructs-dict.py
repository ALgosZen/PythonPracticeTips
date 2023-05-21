# dictitionary can hold more info, and does not require to be sorted
##### built-in Methods ####
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

car = {
    "brand" : "ford",
    "model" : "Mustang Mache",
    "year" : "2023",
    "color" : "red"
}

car.update({"color":"green"})
print(car.get("year"))
# print(car.get['color']) #TypeError: object is not subscriptable
car.popitem()
car.popitem()
car.popitem()
print(car)