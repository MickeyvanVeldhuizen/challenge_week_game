width = int(input("width"))
width_memory = width
heigth = int(input("heigth"))
line = ""
number = "o"

while heigth > 0:
    while width > 0:
        line += str(number) + " "
        number = "o"
        width -= 1
    width = width_memory
    print(line)
    line = ""
    heigth -= 1