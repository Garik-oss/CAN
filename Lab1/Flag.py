red = "\033[41m"
white = "\033[47m"
blue = "\033[44m"
reset = "\033[0m"

for j in range(1, 6):
    for i in range(0, 10):
        if j % 2 == 0:
            print(blue + " *" + reset, end="")
        else:
            print(blue + "* " + reset, end="")
    for i in range(0, 40):
        if j % 2:
            print(white+"  "+reset, end="")
        else:
            print(red +"  "+reset, end="")
    print("\n")
    
for j in range(6, 14):
    for i in range(0, 50):
        if j % 2 == 1:
            print(white + "  " + reset, end="")
        else:
            print(red + "  " + reset, end="")
    print("\n")
