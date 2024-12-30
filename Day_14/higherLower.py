from game_data import famous_people
from random import randint

data= famous_people
score=0

while True:

    per1=famous_people[randint(0,len(data)-1)]
    per2=famous_people[randint(0,len(data)-1)]

    while per1==per2:
        per2=famous_people[randint(0,len(data)-1)]


    print(f"compare A: {per1["name"]}, {per1["description"]}, from {per1["country"]}")

    print(f"against B: {per2["name"]}, {per2["description"]}, from {per2["country"]}")

    ans = "A" if per1["follower_count"]>per2["follower_count"] else "B"

    user=input("who has more followers? tyoe a or b or q to quit: ")

    if user.lower()==ans.lower():
        score+=1
        print("right answer")
    elif user=="q":
        break
    else:
        print("wrong answer")