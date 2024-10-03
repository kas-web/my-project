#Quiz Game
print("Welcome to my Computer Quiz!")

playing = input("Do you want to play? ")
 
if playing != "yes":
    quit()

print("Okay ! Let's play :)")
score =0

answer = input("1.What does CPU stand for?")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1

else:
    print("Incorrect!")

answer = input("2.What do you mean by SQL?")
if answer.lower() == "structured query language":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("3.ALU stands for?")
if answer.lower() == "arithmetic logic unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("4.What is software?")
if answer.lower() == "instructions that tell the hardware what to do":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("5.Which of the following are types of computer hardware ? a)Hard drive  b)RAM c)Mozilla Firefox d) Keyboard") 
    
if answer.lower() == "Keyboard":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("6.The computer’s main circuit board is called a ________.?")
if answer.lower() == "motherboard":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("7.Python was invented by?")
if answer.lower() == "Guido Van Rossum":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("8.Extension name of Python file?")
if answer.lower() == ".py":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You scored" + str(score) +" answers correct!")
print("You scored" + str((score / 8) * 100) +"%")

    