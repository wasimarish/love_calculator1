name1=  input("Enter your  Name\n")
name2= input("Enter Your partners name\n")

name=name1+name2;
lowercase_name=name.lower()

t=lowercase_name.count("t")
r=lowercase_name.count("r")
u=lowercase_name.count("u")
e=lowercase_name.count("e")

true = t+r+u+e

l=lowercase_name.count("l")
o=lowercase_name.count("o")
v=lowercase_name.count("v")
e=lowercase_name.count("e")

love=l+o+v+e

percent = int(str(true)+str(love))

if percent <10 or percent>90:
    print(f"Your love score is {percent} you go together like coke and mentos")
elif percent>=40  or percent <=50:
    print(f"Your love score is {percent} you are alright together")
else:
    print(f"Your love score is {percent }.")