Wordle Word Search Test Program
===============================

For the *TI-84 Plus CE* graphing calculator.

This is a performance test of a data and search algorithm. Which can be used
elsewhere. Or in their own ez80 implementation.

Contents:

* `src/main.c` : Basic tests. Uses constants that was pulled from interactive
  session by running `tools/databuild.py` in order to verify goodness of data.
  Then it runs a perf test by running the code in worst case 100 times. Uses
  a big chunk of the stopwatch example program to time things and output
  data to the screen.
* `search.asm` : Contains routines to perform search. TODO: Add routine to
  retrieve a word based on index. Index can be generated from pieces of code
  used in `tools/databuild.py`

