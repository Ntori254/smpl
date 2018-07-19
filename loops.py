answer=23
question= "What number an I thinking of?"
print("Let us play a simple game\n")
while True:
    guess=int(input(question))
    if(guess<answer):
        print("A little higher")
    elif(guess>answer):
        print("A little lower")
    else:
        print("Hurray! You guessed my number right")
        break;