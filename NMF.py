import numpy as np
from math import sqrt

class NMF():

	def __init__(self, r=10,random_state=None, tol=0):
		self.r = r
		if random_state is not None:
			np.random.seed(random_state)

		self.tol = tol

	def fit(self, X,distance="euclidean",max_iter=200,eps=1e-8):
		"""
		param X = result of a countvectorizer
		"""

		#transpose because we want each line to represent a word, each column to be a document
		X = X.T

		(p,n) = X.shape


		#initialize W and H randomly
		#W = np.random.rand(p,self.r)*sqrt(X.mean()/self.r)
		#H = np.random.rand(self.r,n)*sqrt(X.mean()/self.r)

		H = np.random.rand(self.r,n)
		W = np.random.rand(p,self.r)


		number_iteration = 0

		for i in range(max_iter):
			if distance == "euclidean":
				W, H = self._euclideanUpdate(X,W,H,eps=eps)
				number_iteration += 1
				if np.linalg.norm(X-np.dot(W,H),ord='fro') < self.tol:
					break
			else:
				W, H = self._KLUpdate(X,W,H,eps=eps)

		return W, H, number_iteration



	def _euclideanUpdate(self,X,W,H,eps=1e-8):

		W = np.multiply(W,np.divide(np.dot(X, H.T) ,(np.dot(W,np.dot(H,H.T)) + eps)))
		H = np.multiply(H,np.divide(np.dot(W.T, X), (np.dot(np.dot(W.T, W), H) + eps)))

		return W, H


	def _KLUpdate(self,X,W,H,eps=1e-8):

		#first update H
		sum_columns_W = np.reciprocal((np.sum(W,axis=0)+eps))
		W_transpose = W.T
		Y = np.divide(X+eps,np.dot(W,H)+eps)
		Z = np.dot(W_transpose,Y)
		updated_H = np.multiply(H,Z)
		updated_H = np.multiply(updated_H,sum_columns_W[:,np.newaxis])

		#now update W
		sum_lines_H = np.reciprocal((np.sum(H,axis=1)+eps))
		H_transpose = H.T
		Y = np.divide(X+eps,np.dot(W,H)+eps)
		Z = np.dot(Y,H_transpose)
		updated_W = np.multiply(W,Z)
		updated_W = np.multiply(updated_W,sum_lines_H)

		return updated_W, updated_H
