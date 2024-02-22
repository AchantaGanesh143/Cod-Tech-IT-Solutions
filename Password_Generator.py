import string
import random
def gen():
    len=int(input("enter length of the pasword:"))
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.digits
    s4=string.punctuation
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    password=(" ".join(s[0:len]))
    print("the password is: ")
    print(password)
gen()
