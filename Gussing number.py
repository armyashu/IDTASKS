# gussing number
import random
computernumber=random.randint(1,100)
usernumber=int(input("enter the value : "))
if usernumber>computernumber:
    print("computer number=",computernumber)
    print("user number is too higher then computer number !")
    print("user win !")
elif usernumber<computernumber:
    print("computer number =", computernumber)
    print("computer number is too higher then user number!")
    print("computer win!")
else:
    print("computer number = ", computernumber)
    print("user and computer number is equal!")
    print("No one is win the game!")
