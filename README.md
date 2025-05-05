# File\_Tree

A micro‑sized **Python 3** script that walks through a chain of text files, gathers every word it finds, and then builds a *column‑by‑column* frequency analysis to reveal the **most common character in each position**. Think of it as a sideways histogram: instead of counting letters overall, it asks *“What is the most frequent 1st letter? the most frequent 2nd letter? …”*—handy for solving toy cryptography or word‑puzzle assignments.


## Problem Statement

Starting from an **entry file** (e.g. `test01/A.txt`) you must:

1. Read the *first* token—this is the *name of the next file* in the chain.
2. Treat the remaining tokens as **words** to analyse.
3. Repeat from that next file until the chain loops back to the original file.
4. After visiting the entire cycle, output one string where each character *`i`* is the letter that appeared most often in position *`i`* across **all** collected words. On ties, pick the lexicographically smaller letter.



## How It Works

### File‑Chaining Mechanism

```python
def open_next_file(filename):
    with open(filename, "r", encoding="utf8") as f:
        tokens = f.read().split()
    # tokens[0] → pointer to next file
    return tokens[1:], tokens[0]
```

* The first token acts like a **symlink** to the next file.
* The function returns both the **word list** and the **pointer**.
* A `while filename != newfilename:` loop follows the chain until it cycles. ([github.com](https://github.com/bgkcsav4/File_Tree/raw/main/program01.py))

### Frequency Computation

1. **Normalise** words into `(word, len)` tuples.
2. Compute `max_len` so the algorithm knows how many columns it needs.
3. For each column index `i` build a dictionary `ldict` → `{char: count}`.
4. Select the winner with `max(ldict.items(), key=get_max)` where

   ```python
   def get_max(item):
       char, count = item
       return (count, -ord(char))  # higher count, then alphabetically lower
   ```

The chosen character is appended to `string`, yielding the final signature (left as an exercise to return rather than print).

---
