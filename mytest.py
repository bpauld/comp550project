l = [1,4,2,7,34,12]
l = [(i[0],i[1]) for i in sorted(enumerate(l), key=lambda x:x[1], reverse=True)]


print(l)