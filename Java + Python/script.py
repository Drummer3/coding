import sys

first = sys.argv[1]
second = sys.argv[2]


file = open("output.txt","w")
text = first + " " + second
file.write(text)
file.close()