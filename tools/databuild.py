# Builds the data file for use with the dictionary decompressor/reader

import pickle
from re import L

def ham(w1,w2):
    return sum([a != b for a,b, in zip(w1,w2)])
def diffidx(w1,w2):
    arr = [a != b for a,b, in zip(w1,w2)]
    rarr = list()
    for idx,i in enumerate(arr):
        if i:
            rarr.append(idx)
    return rarr

#Delta is always w2-w1, because we start with w1 and want to add
#the delta to get w2. Thus we start with w1+X=w2, and the formation that
#satisfies this is w2-w1 = X. If the result is less than 0, add 26.
#The returned number will always be somewhere between 0 and 25, inclusive.
def getdelta(w1,w2,index):
    c1 = ord(w1[index])
    c2 = ord(w2[index])
    r = c2-c1
    if r < 0:
        r += 26
    return r

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

data = bytearray()

curword = wordlist[0]
data.extend(bytearray(curword, encoding="ASCII"))
''' Data byte format:
    0b_FFFD_DDDD
    Where F = Offset into word, (e.g. in "WORD", 0='W', 2="R", etc.)
    Where D = Delta from current letter. mod 26 math is used.
    Special note:
        Where D = 27, 28, 29, and 30 indicates that the next 2, 3, 4, or 5
        bytes shall apply to te same word. No other action is taken with this
        command code.
        D = 31 is a reserved value. idk what i'll use it for but it seems like
        a good thing to keep around.
'''
import copy
for idx,word in enumerate(wordlist[1:]):
    dist = ham(curword,word)
    if dist == 1:
        #single byte entity
        r = diffidx(curword,word)
        F = r[0]
        D = getdelta(curword,word,F)
        data.append(((F&7)<<5) | (D&31))
    else:
        if not dist:
            raise ValueError("Illegal distance encountered.")
        #mutlibyte stuffs.
        r = diffidx(curword,word)
        data.append(27-2+len(r))
        for F in r:
            D = getdelta(curword,word,F)
            data.append(((F&7)<<5) | (D&31))
    curword = copy.copy(word)
data.append(0)  #EOF

print("Datastream length: {0}".format(len(data)))



with open("OUTPUT.bin","wb") as fp:
    fp.write(data)

import io
fp = io.BytesIO(data)

wordlist2 = []
fp.seek(0)
word = bytearray(fp.read(5))
wordlist2.append(str(word, encoding = "ASCII"))
while True:
    c = fp.read(1)
    if c == b'':
        break
    c = c[0]
    if not c:
        break
    F = (c>>5)&7
    D = c&31
    if D >= 27:
        #multiletter
        for _ in range(D-27+2):
            c = fp.read(1)[0]
            F = (c>>5)&7
            D = c&31
            r = word[F]+D
            if r > ord('Z'):
                r -= 26
            word[F] = r
    else:
        r = word[F]+D
        if r > ord('Z'):
            r -= 26
        word[F] = r
    wordlist2.append(str(word, encoding="ASCII"))


idx = 0
for a,b in zip(wordlist, wordlist2):
    if a != b:
        print("Difference detected in {0}: {1} vs {2}".format(idx,a,b))
        break
    idx += 1
else:
    print("Both datastreams match perfectly.")


asmdata = ""
tempstring = ""
counter = 0
for n in data:
    if not tempstring:
        tempstring = ".db "
    tempstring += "${0:02X}".format(n)
    if counter < 16:
        tempstring += ", "
        counter += 1
    else:
        asmdata += tempstring + "\n"
        counter = 0
        tempstring = ""
if tempstring:
    asmdata += tempstring + "\n"

with open("OUTASM.txt","w") as fp2:
    fp2.write(asmdata)


    













