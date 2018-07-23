answer="yes"
print("Does your computer switch on?")
while True:
    issue=str(input())
    if(issue==answer):
        print("Is the switch on for socket on?")
    elif(issue==answer):
        print("Is the power cable placed properly in the socket?")
    elif(issue==answer):
        print("Is the system unit switched on?")
    else:
        print("If not, please visit a computer technician to fix your computer\n")
        break;


answer="yes"
print("Does your computer audio have any problems?\n")
while True:
    issue=str(input())
    if(issue==answer):
        print("Is the sound on mute?")
    elif(issue==answer):
        print("Do you have the latest version on Windows?")
    elif(issue==answer):
        print("Are your drivers updated?")
    else:
        print("Please instal a different Windows version and if the issue still there, visit a computer specialist\n")
        break;


answer="yes"
print("Does your computer screen issues?\n")
while True:
    issue=str(input())
    if(issue==answer):
        print("Is the computer powered on?")
    elif(issue==answer):
        print("Did you properly connect the PC to the socket?")
    elif(issue==answer):
        print("Did you perhaps damage the screen?")
    else:
        print("If no, you need to replace your screen with a new one\n")
        break;

