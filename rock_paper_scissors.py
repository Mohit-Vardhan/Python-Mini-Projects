import random
usel= input("Enter your choice: (R)rock, (P)paper or (S)scissors:")
csel= random.choice(['R', 'P', 'S'])
print("Computer selected:"+ csel)
if(usel=='R' and csel=='S' or usel=='S' and csel=='P' or usel=='P' and csel=='R'):
    print("Yayy, you won!!")
elif(usel==csel):
    print("Tie!")
else:
    print("You Lost")