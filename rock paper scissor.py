import random
l=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""","""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""","""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
n=int(input("enter 0 for rock, 1 for paper and 2 for scissor"))
print(f"your choice{n}")
print(l[n])
m=random.randint(0,2)
print(f"computer chose{l[m]}")
u=l[n]
if(n==m):
    print("draw")
elif n==0 and m==2:
    print("you win!")
elif m>n:
    print("you loose!")
elif n>m :
    print("you win")
elif n==2 and m==0:
    print("you loose!")
else:
    print("you typed an invalid number , you loose!")
    

    
