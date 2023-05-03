import numpy as np
name=input("enter your name :")
print("hello ",name)
print("***welcome to play the game bingo***")
print()
print("""
RULES TO PLAY THE GAME
1.the game have 5 rows and 5 coloumns 
2.first you tell one number and then computer tell another number
3.one who complete first the line
  i.row line
  ii.coloumn line
  iii.diagonal line""")
user_tables=np.random.choice(range(1,26),25,replace=False)
user_table=user_tables.reshape(5,5)
print(user_table)
#print(user_table(5))
