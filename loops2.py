answer="no"
say= "Say yes or no to these questions for your PC issues"
print("Does your computer switch on?\n")
while True:
    issue=str(input(say))
    if(issue==answer):
        print("Is the switch on for socket on?")
    elif(issue==answer):
        print("Is the power cable placed properly in the socket?")
    elif(issue==answer):
        print("Is the system unit switched on?")
    else:
        print("If not, please visit a computer technician to fix your computer")
        break;

statment="no"
say= "Say yes or no to these questions for your PC issues"
print("Does your computer audio have any problems?\n")
while True:
    issue=str(input(say))
    if(issue==statement):
        print("Is the sound on mute?")
    elif(issue==statement):
        print("Do you have the latest version on Windows?")
    elif(issue==statement):
        print("Are your drivers updated?")
    else:
        print("If not, please visit a computer technician to fix your computer")
        break;

s="no"
say= "Say yes or no to these questions for your PC issues"
print("Does your computer have any problems?\n")
while True:
    issue=str(input(question))
    if(issue==s):
        print("Is the sound on mute?")
    elif(issue==s):
        print("Do you have the latest version on Windows?")
    elif(issue==s):
        print("Are your drivers updated?")
    else:
        print("If not, please visit a computer technician to fix your computer")
        break;

