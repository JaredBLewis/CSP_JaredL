# Jared Lewis, Strings Notes Python

#string is a data type that holds any info surrounded by qoutation marks  "" ''

#print("Hello World")
#note ="Hello World"
note ='Hello World'

name = input("What is your first name?:\n").srtip().lower().capitalize()

#print(f"hello {name} wlcome to my program!")
print("this is your name"+ name)

sentance = "The quick brown fox jumps over the lazy dog"

#print(len(sentance))
#print(sentance[4])
#print(sentance.find("brown"))
#print(sentance[10:15])
start = sentance.find("brown")
length = len("brown fox")
print(sentance[start:start+length])