from nltk.corpus import wordnet
import sqlite3
import clipboard
import schedule
import time
from datetime import datetime
import tkinter as tk


def run():
	user_inp = []
	def display(e1):
		user_inp.append(e1)
		top.destroy()
	top = tk.Tk()
	top.title("Word Memory")
	top.geometry("500x200")
	text = clipboard.paste()
	name = tk.Label(top, text = "Meaning of the word : "+text)
	name.place(x = 0, y = 25)
	e1 = tk.Entry()
	e1.place(x = 200, y = 25)
	button = tk.Button(top,text="Enter", command = lambda: display(e1.get()))
	button.grid(row = 0, column = 0)
	button.pack()
	top.mainloop()

	dict = {}
	syn = wordnet.synsets(text)
	if (len(syn) != 0):
		dict[text] = syn[0].definition()


	def_ = []
	def_.append(dict[text])
	if (user_inp == def_) :
		print("You are right!")
	else :
		print("You missed it!")
		s = str(def_)
		print("Correct answer is : "+ s[2:len(s)-2])

schedule.every(5).seconds.do(run)

while 1:
	schedule.run_pending()
	time.sleep(1)

