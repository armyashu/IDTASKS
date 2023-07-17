1# rock ,paper , Scissor

# winnig rules follow:
# rock vs paper = win paper
# paper vs scissor = win scissor
# rock vs scissor = rock
import random
l=["Rock " , "Paper", "Scissor"]

while True:
    Comcount=0
    usrcount=0
    UserEnter=int(input('''
    enter the game and start...!
    1 yes
    2 No / Exit
    '''))
    if (UserEnter==1):
        for a in range(1,6):
            Userinput=int(input('''
            1 Rock
            2 Scissor
            3 Paper
            
            '''))
            if (Userinput==1):
                userchoise="Rock"
            elif(Userinput==2):
                userchoise="Scissor"
            elif(Userinput==3):
                userchoise==3

            computerchoise=random.choice(l)
            if(computerchoise==userchoise):
                print("computer value", computerchoise)
                print("user value", userchoise)
                print("Draw the Match")

                usrcount=usrcount+1
                Comcount=Comcount+1

            elif(userchoise=="Rock" and computerchoise=="Scissor") or(userchoise=="Paper" and computerchoise=="Rock") or(userchoise=="Scissor" and computerchoise=="Paper"):
                print("computer value", computerchoise )
                print("user value", userchoise)
                print("User win the Game!")
                usrcount=usrcount+1
            
            else:
                print("computer value",computerchoise)
                print("user value",userchoise)
                print("Computer win the Game!")
                Comcount=Comcount+1
            
            if(usrcount==Comcount):
                print("Final Gamew is Draw!")
                print("user score",usrcount)
                print("computer score",Comcount)

            elif(usrcount>Comcount):
                print("Final User Win the Game1")
                print("user score",usrcount)
                print("computer score",Comcount)
            
            else:
                print("Computer win the Game!")
                print("user score",usrcount)
                print("computer score", Comcount)

    else:
        break

         
    
