import collections
import pickle
import copy


def ham(w1,w2):
    return sum([a != b for a,b, in zip(w1,w2)])

wordlist = []
hdist_initial = 0
with open("sorted3.pkl","rb") as fp:
    tmp  = pickle.load(fp)
    for item in tmp:
        if isinstance(item,tuple):
            hdist_initial += item[1]
            wordlist.append(item[0])
        else:
            wordlist.append(item)


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





with open("sorted4.pkl","wb") as fp:
    pickle.dump(newlist, fp)
print("Sanity check. Wordlist len: {0} of {1}".format(len(newlist),len(wordlist)))
        
wordlist2_hamsum = 0
for i in newlist:
    if isinstance(i,tuple):
        if len(i)>1:
            wordlist2_hamsum += i[1]

print("Comparison: Before {0}, after {1}".format(hdist_initial, wordlist2_hamsum))

