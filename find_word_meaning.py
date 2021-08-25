from nltk.corpus import wordnet
class Find_word_meaning:
	
	def word_meaning(word):
		print("here")
		meaning = wordnet.synsets(word)
		return meaning[0].definition()
