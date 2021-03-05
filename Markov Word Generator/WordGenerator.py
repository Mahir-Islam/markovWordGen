import random
import string
from tkinter import *

root = Tk()
root.title("Word Generator")
root.minsize(600,450)

WORDS = open("common_words.txt","r")
A = WORDS.read()
WORDS.close()

def push(rng):
	InfoBox.insert(END,rng)

def replace(rng):
    InfoBox.delete(1.0,END)
    InfoBox.insert(END,rng)
""""""

wordList = "".join([i for i in A])
wordList = wordList.replace("\n",',')
wordList = wordList[3:]

assoc = {
	'a':[],
	'b':[],
	'c':[],
	'd':[],
	'e':[],
	'f':[],
	'g':[],
	'h':[],
	'i':[],
	'j':[],
	'k':[],
	'l':[],
	'm':[],
	'n':[],
	'o':[],
	'p':[],
	'q':[],
	'r':[],
	's':[],
	't':[],
	'u':[],
	'v':[],
	'w':[],
	'x':[],
	'y':[],
	'z':[]
}

a = ","

for w in wordList:
	if a != "," and w != ",":
		assoc[a.lower()].append(w)

	a = w


def CreateWord(length):

	characs = string.ascii_letters
	characs = characs[:26]
	characs = characs.replace('x','') #prevents x from being first letter

	length -= 1
	genString = ""
	genString += random.choice(characs).lower()

	for x in range(length):
		genString += random.choice(assoc[genString[-1].lower()])

	return genString

a = ""
for x in range(100):
	a += CreateWord(7)+" "

''''''

def push(rng):
	InfoBox.delete(1.0,END)
	InfoBox.insert(END,rng)

def replace(rng):
    InfoBox.delete(1.0,END)
    InfoBox.insert(END,rng)

def get():
	return NumLen.get(1.0,END)

''''''

TITLE = Label(root,text="Markov Word Generator",fg="#161648",bg="#fff",font="Arial 32")
TITLE.place(relx=0.5,rely=0.1,anchor='center')

InfoBox = Text(root, width=46,height=8, bg="white", fg="black", font="Arial 14")
InfoBox.place(relx=0.5, rely=0.4, anchor='center')
InfoBox.insert(END,"Welcome to my program! By Mahirul Islam.\nJust give a word length in the input below and the program\nwill generate a new psuedo-English word.")

NumLen = Text(root, width=46,height=2, bg="white", fg="black", font="Arial 14")
NumLen.place(relx=0.5, rely=0.675, anchor='center')
NumLen.insert(END,"Enter an integer here")

GENBTN = Button(root,text="Generate",bg="#ccc",fg='#222',font="Arial 30",borderwidth=0,command=lambda: push( CreateWord(int(get())) +'\n'))
GENBTN.place(relx=0.5,rely=0.85,anchor='center')

root.mainloop()