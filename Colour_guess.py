import random
ucolour = input("Enter the colour you want to choose - R(red), G(green) & B(blue):")
ccolour = random.choice(['R', 'G', 'B'])
print("Computer selected:"+ ccolour)
if ucolour== ccolour:
    print("You Won")
else:
    print("You Lost")