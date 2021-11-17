import pandas as pd
from collections import Counter

# find the top N words from snippets in given file

import sys

assert (
    len(sys.argv) == 3
), """


Usage:

python extract_top_words.py N filename

ex. Print top 25 words from java snippets

    python extract_top_words.py 25 snippets-java.csv
"""
N = int(sys.argv[1])
filename = sys.argv[2]
print(f"Processing {filename}...")
df = pd.read_csv(filename)
# fill in missing values with an empty string
df = df.fillna("")
# word_counts = pd.Series(" ".join(df["snippet"]).lower().split()).value_counts()[:100]
word_counts = Counter(" ".join(df["snippet"]).lower().split()).most_common(N)
print(f"Top {N} 'words'")
print(word_counts)
