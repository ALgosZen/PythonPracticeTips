count = int(input("enter a number for size of diamond: "))
star = "*"
#Loop to Draw a Pyramid of given size
for i in range(count):
    for j in range(count-i):
        print(" ", end='')
    print(star)
    star += "**"
# Loop to Draw reverse Pyramid (second half)
count -= 1  
space = 1
starNum = count*2 - 1
stars =  "*" * starNum

for i in range(count):
    print(" "+ space * " "+ stars)
    starNum -= 2
    stars = "*" * starNum
    space += 1

    



