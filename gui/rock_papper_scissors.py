import random
print("***welcome to rock papper scissior game***")
print()
user_score=0
computer_score=0
tie=0
name=input("enter your name :")
print("""
RULES TO PLAY A GAME
1.rock vs papper -> papper
2.papper vs scissor ->scissor
3.scissor vs rock ->rock""")
print()
while True:
        print("""
        ENTER USER COICES
        1.rock
        2.papper
        3.scissor""")
        print()
        choice=int(input("enter the choice above :"))
        if choice==1:
            user_choice="rock"
        elif choice==2:
            user_choice="papper"
        else:
            user_choice="scissor"
        print()
        print("user choice is :",user_choice)
        print()
        computer_choices=random.randint(1,3)
        print()
        if computer_choices==1:
            computer_choice="rock"
        elif computer_choices==2:
            computer_choice="papper"
        else:
            computer_choice="scissor"
        print("computer choice is :",computer_choice)
        print()
        if (user_choice=="rock" and computer_choice=="papper" or user_choice=="papper" and computer_choice=="rock"):
            win="papper"
        elif (user_choice=="papper" and computer_choice=="scissor" or user_choice=="scissor" and computer_choice=="papper"):
            win="scissor"
        elif (user_choice==computer_choice):
            win="tie"
        else:
            win="rock"
        if win==user_choice:
            winner="user"
            user_score +=1
        elif win==computer_choice:
            winner='computer'
            computer_score +=1
        elif win=="tie":
            tie+=1
        u=input("user you want to play again:")
        if u==("no"or"NO"):
            break
print("user score:",user_score)
print()
print("computer score:",computer_score)
print()
print("how many ties:",tie)
print()
if user_score>computer_score:
    print(name," won the match")
elif user_score < computer_score:
    print(name," are loss")
else:
    print("the game is tie")