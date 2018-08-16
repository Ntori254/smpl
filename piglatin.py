#pig latin translators
original ="Andersen"
pgy= "ay"

word= original.lower()
#check for starting letter using regular expressions
first=word[0]

newword = word+first+pgy
print(newword[1:])