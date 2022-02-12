import pickle
import sys

sys.setrecursionlimit(13000)

def ham(w1,w2):
    return sum([a != b for a,b, in zip(w1,w2)])

print("Loading wordlist...")
with open("wordmap.pkl","rb") as fp:
    wordlist = pickle.load(fp)
print("Wordlist loaded.")

wordset = set()
print("Detecting if distance-1 is possible.")
for k in wordlist:
    nlist = [(w,d) for w,d in wordlist[k] if d < 2]
    wordset.update([w for w,d in nlist])
print("wordset length: {0}".format(len(wordset)))
print("Dictionary length: {0}".format(len(wordlist)))


print("Forming possible structure...")


#0-26 = letter
#27=2 28=3 29=4 30=5
#
'''
with open("newmap.pkl","wb") as fp:
    pickle.dump(newmap, fp)
'''
