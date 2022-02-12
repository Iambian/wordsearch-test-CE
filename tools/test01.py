import pickle

wordlist = []
with open("wlist.txt") as fp:
    for line in fp.readlines():
        if line:
            wordlist.append(line.strip())

#Assume both words are same length. Find hamming distance.
def ham(w1,w2):
    return sum([a != b for a,b, in zip(w1,w2)])

#Okay. Let's objectively measure something.
#First, we'll start with a lexographically-sorted thing.
#(idk how to spell the lexo-thingamabobber and too in the zone to google it)

wordlist1 = wordlist[:]
wordlist1.sort()
wordlist1_hamsum = 0

for idx,w in enumerate(wordlist1[:-1]):
    w2 = wordlist1[idx+1]
    wordlist1_hamsum += ham(w,w2)

#Then we'll use our super-special sorted thinger to see if that made
#any kind of difference whatsoever. I'm hoping it did. Took an hour of
#awful O(n^2m) runtime to do.

print("Loading presorted...")
with open("sorted1.pkl","rb") as fp:
    wordlist2 = pickle.load(fp)
print("Presorted list loaded.")
wordlist2_hamsum = 0
for i in wordlist2:
    if isinstance(i,tuple):
        if len(i)>1:
            wordlist2_hamsum += i[1]
#debug
print(wordlist2[0],wordlist[-1])
print(len(wordlist1),len(wordlist2))
print(wordlist1_hamsum,wordlist2_hamsum)


