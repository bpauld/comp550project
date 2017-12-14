""" Get the 20 news groups data """
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pickle

from random import randint


random_state = randint(1,100)

cats = ['alt.atheism', 'sci.space']
newsgroups = fetch_20newsgroups(shuffle=True, random_state=1, subset="train",
                                remove=("headers", "footers", "quotes"))



""" Prepare input """
n_features = 2000
vectorizer = TfidfVectorizer(max_features=n_features, stop_words="english")

# Word counts per document matrix (input for sklearn)
W_counts = vectorizer.fit_transform(newsgroups.data)

# Keep track of vocabulary to visualize top words of each topic
vocabulary = vectorizer.get_feature_names()





#now try our model
#import NMF

from sklearn.decomposition import NMF

model2 = NMF(n_components=10)
#W,H,n = model2.fit(W_counts,distance='euclidean')
model = NMF(n_components=12, init='random',solver='cd',alpha=0,beta_loss = 2,random_state=random_state)
W = model.fit_transform(W_counts)
H = model.components_



def vizualizeTopic(H,numberOFWords,vocabulary):
	"""
	param W: matrix W obtained from nmf
	"""

	(r,n_features) = H.shape

	for topic in range(r):
		#topic_words = W[:,topic]
		l = [(i[0],i[1]) for i in sorted(enumerate(H[topic,:]), key=lambda x:x[1], reverse=True)]
		#print (l)
		print("Topic "+ str(topic))
		print(" ".join(vocabulary[l[rank][0]] for rank in range(numberOFWords)))


vizualizeTopic(H,12,vocabulary)








