#module to get the copied word.
import pyperclip as pc
#keyboard module
import keyboard
from nltk.corpus import wordnet
from find_word_meaning import Find_word_meaning

def check():
	keyboard.wait('ctrl + shift + a')

	find_word_meaning_class_obj = Find_word_meaning

	print(find_word_meaning_class_obj.word_meaning(pc.paste()))

	check()

check()	
