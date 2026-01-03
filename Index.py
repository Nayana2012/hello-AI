print("hello! i am ai bot.What is your name?")
name=input()
print("nice to be meeting you",name)
print("how are you feeling today (good/bad):")
mood=input().lower()
if mood=="good":
    print("i am glad to hear this!")
elif mood=="bad":
    print("i am sorry to hear that.Hope things get better soon!")
else:
    print("i see sometimes it hard to put our feelings into words.")