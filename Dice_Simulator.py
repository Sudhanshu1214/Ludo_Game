#import turtle           used for graphics....
#import colorsys         used to color....
import random
n=int(input("enter the number of players"))
list=[]
dict={}
for i in range(n):
    player=input(f"enter the name of player {i+1} ")
    list.append(player)
# print(list)
final={}
for i in list:
    final.update({i:0})
dice=int(input("enter the number of dice"))
for i in range(dice):
    for j in list:
        c=random.randint(1,6)
        dict.update({j:c})
        final[j]=final[j]+c
    print(dict)
print("\n")
print("\t\t",final)
d=max(final.values())
# Q=max(d.key())
print("\n\t\t\t",f"Hence the winner is {d}")
# print("\n\t\t\t",f"Hence the winner is {Q}")