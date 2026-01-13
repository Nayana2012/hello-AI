print("👋Hello and Welcome to sentimental spy🕵️!")
username=input("Please enter your name:").strip()
if not username:
    username="sentimental spy🕵️"
conversation_history=[]
print(f"Hello spy {username}!")
print(f"I will analyze your sentiment based on the pharse you will select:('i am having fun'/'i am angry'/'i am fine')")
user_input = input("Enter your sentiment: ").strip()
if user_input == 'i am having fun':
    print("color = GREEN")
    print("emoji = 😀")
    print("emotion = happy")
elif user_input == 'i am angry':
    print("color = RED")
    print("emoji = 😡")
    print("emotion = frustrated")
elif user_input == 'i am fine':
    print("color = YELLOW")
    print("emoji = 😣")
    print("emotion = neutral")
print("Thank you for using sentimental spy🕵️!")