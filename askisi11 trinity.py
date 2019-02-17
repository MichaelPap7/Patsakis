import random

text=open("temp.txt","r")

initial=text.read()
words=initial.split()
a=len(words)

while(len(words)>2):
    a=random.randint(0,len(words)-3)
    print (words[a-1], words[a], words[a+1],)
    del words[a-1]
    del words[a]
    del words[a+1]
