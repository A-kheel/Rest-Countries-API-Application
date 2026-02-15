import random
with open("jokes.txt", "r", encoding="utf-8") as file:
    jokes = [line.strip().split("?", 1) for line in file if "?" in line]

user = input("Type 'alexa tell me a joke' for a joke, or 'quit' to exit:")
b = 'y'
while b == 'y':

    if user == "quit":
        break
    elif user == "alexa tell me a joke":
        setup, punchline = random.choice(jokes)
        print("\n" + setup + "?")
        input("say what rn: ")
        print(punchline + "\n")

        b = input('do you want more?(y/n):')
    else:
        break
