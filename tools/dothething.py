# This python script does the thing against the word list in wordle.
# Which hopefully results in the thing being smaller.
# Phrases to watch out for include the following:
# Hamming-weight, 
#
import pickle

wordlist = []
with open("wlist.txt") as fp:
    for line in fp.readlines():
        if line:
            wordlist.append(line.strip())

wordmap = dict()    #words: list(words_sorted_by_hamming_dist_no_more_than_2)


#Assume both words are same length. Find hamming distance.
def ham(w1,w2):
    return sum([a != b for a,b, in zip(w1,w2)])

#FFFF
size_expanded = 0

for idx,word in enumerate(wordlist):
    hamming_list = []
    for word2 in wordlist:
        if word != word2:
            hamming_list.append((word2,ham(word,word2)))
    #Do not consider words that are more than 2 letters different.
    hamming_list = [pair for pair in hamming_list if pair[1] <= 3]
    hamming_list.sort(key=lambda a: a[1])
    wordmap[word] = hamming_list
    size_expanded += len(hamming_list)
    if not idx % 100:
        print("Word list expansion: {0} to {1} by {2}".format(idx,size_expanded,len(hamming_list)))

with open("wordmap.pkl","wb") as fp:
    pickle.dump(wordmap, fp)


