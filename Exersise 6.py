import random
n=1
flag1=0
flag2=0
while(n<=10 and n>=1):
    print("Enter either S,W or G")
    x=input()
    list=["S","W","G"]
    y=random.choice(list)
    n=n+1
    if y=="S" and x=="W":
        print("Computer wins the Round")

        flag1=flag1+1
    elif y=="S" and x=="G":
        print("You win this round")
        flag2=flag2+1
    elif y=="G" and x=="S":
        print("Computer wins this Round")
        flag1=flag1+1
    elif y=="G" and x=="W":
        print("You win this round")
        flag2=flag2+1
    elif y=="W" and x=="S":
        print("You win this Round")
        flag2=flag2+1
    elif y=="W" and x=="G":
        print("Computer wins this round")
        flag1=flag1+1
print(f"Computer wins {flag1} number of times ")
print(f"You win {flag2} number of times ")
if flag1>flag2:
    print("Computer is winner of the Game!!")
elif flag1<flag2:
    print("You are the winner of this game!!")
else:
    print("The match got tied!!")

