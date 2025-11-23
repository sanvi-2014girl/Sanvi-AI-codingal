print("Hi! I am an AI Bot.What's your name ? : ")

name = input()
print(f"Nice to meet you, {name}!")

print("How are you feeling today?(good/bad): ")
mood = input().lower()

if mood == "good":
        print("I am glad to hear that!")
    
elif mood == "bad":
        print("I am very sorry to hear that.Hope things get better soon.")
elif mood == "very good":
        print("Ohh greatt enjoy your day!")

else:
        print("I see.Sometimes it is hard to express feelings by words.")
print("What is your favourite color?(pink/green): ")
color = input().lower()
if color == "pink":
        print("that's my fav color too!")
elif color == "green":
        print("That's a great color!")
else:
        print("That matches you!")

print(f"it was nice chatting with you {name}.Goodbye!")