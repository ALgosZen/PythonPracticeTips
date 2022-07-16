len = 10
star = "ß" 
# for mac symbols refer to this page https://www.webnots.com/option-or-alt-key-shortcuts-to-insert-symbols-in-mac-os-x/

for i in range(len):
    for j in range(len-i): 
        # this inner loop is printing spaces before it prints the star char declared above end ensures no new line 
        print(" ", end='')
    print(star)
    star += "ßß"
