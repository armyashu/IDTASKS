import random
import string
print("welcome to random password generator")
lenght =int(input("enter the lenght of password you want : "))
lowerD = string.ascii_lowercase
upperD=string.ascii_uppercase
digitD=string.digits
symbolD=string.punctuation
combine=lowerD+upperD+digitD+symbolD
x=random.sample(combine,lenght)
password="".join(x)
print(password)