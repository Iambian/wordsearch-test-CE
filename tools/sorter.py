import collections
import pickle
import copy

wordlist = []
with open("wlist.txt") as fp:
    for line in fp.readlines():
        if line:
            wordlist.append(line.strip())

def getid(word):
    id = 0
    for idx,c in enumerate(word):
        c = ord(c)-ord('A')
        id += c * (26 ** idx)

def ham(w1,w2):
    return sum([a != b for a,b, in zip(w1,w2)])

newlist = list()
newlist.append((wordlist[0],0))
words_used = set()
words_used.add(wordlist[0])

for overiter in range(len(wordlist)):
    cur_word, saved_word, shortest = (newlist[-1][0], "", float("inf"))
    for word in wordlist[::-1]:
        if word in words_used:
            continue
        dist = ham(cur_word,word)
        if dist < shortest:
            shortest = dist
            saved_word = word
    if not saved_word:
        print("Iterations ended at {0}".format(overiter))
        break
    words_used.add(saved_word)
    newlist.append((saved_word,shortest))
    if not overiter%100:
        print("Progress at iteration {0}".format(overiter))





with open("sorted1.pkl","wb") as fp:
    pickle.dump(newlist, fp)
print("Sanity check. Wordlist len: {0} of {1}".format(len(newlist),len(wordlist)))
        




