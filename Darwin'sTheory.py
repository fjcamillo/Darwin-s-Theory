try:
    userInput = raw_input("Type a number that you want to reduce to 1: ")
    tracker = 0
    while(int(userInput)!=1):
        if (int(userInput)%2==0):
            userInput = int(userInput)/2
            print userInput
            tracker += 1
        elif(int(userInput)%2!=0):
            userInput = int(userInput)*3+1
            print userInput
            tracker += 1

    print "The Answer is now finished"
    print tracker
    input()
except:
    print "You typed something wrong"
