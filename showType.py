import vowel

listNum = [1,2,3,4,5]
dictNum = {'a':1,'b':2}
setNum = {1,2,3,4,5}
tupleNum = (1,2,3,4,5)
tupleSingle = ('Python',)

print("Type listNum : ", type(listNum))
print("Type dictNum : ", type(dictNum))
print("Type setNum : ", type(setNum))
print("Type tupleNum : ", type(tupleNum))
print("Type tupleSingle : ", type(tupleSingle))

print(vowel.search4letters("I'm very happy", "apy"))