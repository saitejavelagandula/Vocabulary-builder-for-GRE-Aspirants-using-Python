#import python module to get the copied word.
import pyperclip as pc

#import python keyboard module to capture the hotkey
import keyboard

#import python wordnet package is used as dictionary
from nltk.corpus import wordnet

#import python GUI package 
from tkinter import *

import tkinter as tk

#import python automation package
import pyautogui as pya

#function to get meaning of a copied word
def getMeaning():

		#wait till user triggers ctrl+shift+a
		keyboard.wait('ctrl + shift + a')

		#execute ctrl+c on selected text
		pya.hotkey('ctrl', 'c')

		#assign copied word to a variable
		word = pc.paste()

		#get list of synsets of the copied word using wordnet
		word_synsets = wordnet.synsets(word)

		#create a list
		meanings = []

		#iterate through synsets list, get meaning of each synset and append meaning to the meanings list
		for synset in word_synsets:
			meanings.append(synset.definition())

		#creates a window
		window = Tk()			

		#get width and height of user screen
		width= window.winfo_screenwidth()               
		height= window.winfo_screenheight()

		#creates window based on user's screen dimensions
		window.geometry("%dx%d" % (width, height))

		#title of the window
		window.title("Vocabulary Builder for GRE aspirants")

		label = Label(window, text = word, font=("Arial", 15))

		label.pack(side= TOP, anchor="w")

		#creates a vertical scrollbar widget for the window
		vertical_scrollbar = Scrollbar(window)

		#creates a horizontal scrollbar widget for the window
		horizontal_scrollbar = Scrollbar(window, orient = tk.HORIZONTAL)

		#creates list widget
		mylist = Listbox(window, yscrollcommand = vertical_scrollbar.set, xscrollcommand = horizontal_scrollbar.set, font=("Arial", 12))

		#insert meaning from meanings list into list widget 
		for i in meanings:
			mylist.insert(END, i)

		mylist.pack( side = LEFT, fill = BOTH, expand = 1, padx = 10, pady = 5)

		vertical_scrollbar.config( command = mylist.yview )

		horizontal_scrollbar.config(command = mylist.xview)

		window.mainloop()

		getMeaning()
				
getMeaning()
