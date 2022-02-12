Python Tools For Data Mangling
==============================

THE CONTENTS OF THIS FOLDER IS NOT MEANT FOR DIRECT USE. This whole thing is a
huge hack thrown together for me to try and fail to turn this into
a(n approximation of) the traveling salesman problem in order to find the
optimal ordering of the word list for use in ... whatever compression method
this is. Someone can give me the correct name later.

Either way, the method is basically taking an input word and then transforming
it by one or more letters to arrive at a new word. The output data file
contains codes which indicates which letter to change and what its delta is.

Either way, here are the files that I wrote or tried to use, in order, to
make this go brrrrrt.

* `dothething.py` : Outdated. Was used for experimentation
* `morething.py`  : Also outdated. Was used for experimentation.
* `christofides.py` : Copied from someplace on the internet when I Googled
  "Christofides Algorithm" to try to find something more optimal than what I
  had. I failed because my skill was not enough.
* `sorter.py` : So I went the lazy route and just did a blind sort.
  Outputted `sorted1.pkl`
* `resorter.py` : Resort the list until the results stop getting better.
  Intended to be iterative but was lazy with inputs and outputs. You need to
  manually modify the relevent filenames each time you run this thing. Because
  I didn't feel like making an actual loop and possibly waiting forever.
* `databuild.py` : Takes in `sorted3.pkl` and generates both `OUTPUT.bin` and
  `OUTASM.txt`, doing basic integrity checks to ensure it can decompress what
  it compressed.
* `OUTASM.txt` : The data that was used. Needs some modification, which was
  pasted into...
* `match.z80` : Contains non-working code and the data set. There are subtle
  differences between this and the stuff in `src/search.asm`.

Maybe someone could sort the list more efficiently since I did the thing in a
really lazy way. That way, `databuild.py` might spit out something smaller.
And as a consequence, faster-running.



