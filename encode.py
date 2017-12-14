import numpy as np
from operator import itemgetter

class encode():

	def __init__(self):
		self.max_number_of_words_per_document = 128
		self.max_number_of_charac_per_word = 256

	def fit(self,X):
		"""
		param X: for now assumed to be a list of document, each document being a string
		returns: a list containing the matrix representation of each document, as described in the paper
		"""

		#first we rank of each character in the corpus
		ranked_characters = self._getRankOfCharacters(X)

		#now get mapping from character to compress code
		mapping = self._getMappingCharToCompressCode(ranked_characters)

		return mapping





	def _getRankOfCharacters(self,X):
		
		#first we get count of each character
		count = {}
		for document in X:
				for charac in document:
					if charac in freq:
						count[charac] += 1
					else:
						count[charac] = 1


		list_count = []
		for charac in count:
			list_count.append((charac,count[charc]))

		#sort in decreasing order
		list_count.sort(reverse=True, key=itemgetter(1))

		ranked_characters = []
		for i in range(len(list_count)):
			ranked_characters.append(list_count[i][0])

		return ranked_characters


	def _getMappingCharToCompressCode(self, ranked_characters):
		"""
		param ranked_characters: list of characters in decreasing order of frequency in the corpus
		returns: a dictionnary mapping each character to its compress code
		"""

		mapping = {}
		for rank in range(len(ranked_characters)):
			mapping[ranked_characters[rank]] = self._createCompressCode(rank)
		return mapping


	def _createCompressCode(self,rank):
		"""
		param rank: rank of the character in the corpus
		returns: compress code corresponding to that character, as a numpy array
		"""

		compress_code = [1]
		for i in range(rank):
			compress_code.append(0)
		compress_code.append(1)
		return np.asarray(compress_code)


