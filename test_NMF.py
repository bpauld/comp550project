import numpy as np
from random import randint


random_state = randint(1,100)
tol = 1e-4
eps = 0

X = np.array([[1, 1],
				[2, 1],
				[3, 1.2],
				[4, 1]])



from sklearn.decomposition import NMF
model = NMF(n_components=2, init='random', random_state=random_state,solver='mu',alpha=0,tol=tol,beta_loss = 2)
W = model.fit_transform(X)
H = model.components_

print(W)
#print('separate')
print(H)


print(model.n_iter_)
print(model.reconstruction_err_)

#print(np.linalg.norm(X - np.dot(W,H),ord='fro'))

import NMF

print('########################################')

model2 = NMF.NMF(r=2,random_state=random_state,tol=tol)
W,H,n = model2.fit(X,eps=eps,distance='euclidean')



#print('separate')
print(W)
#print('separate')
print(H)
#print(np.linalg.norm(X - np.dot(W,H),ord='fro'))
print(n)


print('########################################')





"""
import nmf
res = nmf.nmf(X,random_state=random_state,eps=eps)
W = res[0]
H = res[1]
print(W)
print(H)
"""
