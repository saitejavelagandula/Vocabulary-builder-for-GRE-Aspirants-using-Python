#python module to get the copied word.
import pyperclip as pc

#keyboard module to capture the hotkey
import keyboard

#wordnet module is used as dictionary
from nltk.corpus import wordnet

import tkinter as tk

from tkinter import *

import pyautogui as pya

#function to get meaning of a copied word
def getMeaning():

	#wait till user triggers ctrl+shift+a

		keyboard.wait('ctrl + shift + a')

		pya.hotkey('ctrl', 'c')

		word = pc.paste()
		#get synsets of the copied word using wordnet
		word_synset = wordnet.synsets(word)
		meanings = []
		for synset in word_synset:
			meanings.append(synset.definition())

		# convert_list_to_string = [str(element) for element in meanings]

		# meanings_joined_string = ",\n".join(convert_list_to_string)

		window = tk.Tk()
		scrollbar = Scrollbar(window)
		width= window.winfo_screenwidth()               
		height= window.winfo_screenheight()
		window.title("Vocabulary Builder for GRE aspirants")
		window.geometry("%dx%d" % (width, height))
		mylist = Listbox(window, yscrollcommand = scrollbar.set)
		for i in meanings:
			mylist.insert(END, i)
		mylist.pack( side = LEFT, fill = BOTH, expand = 1)
		scrollbar.config( command = mylist.yview )			
		# name = tk.Label(window, text = )
		# name.pack()
		window.mainloop()
		#output the meaning of a word to console
		print(meaning[0].definition())

		getMeaning()
				

getMeaning()	
