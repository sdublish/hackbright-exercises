# put your code here.
import sys
from collections import Counter

file_name = sys.argv[1]


def word_count(filename):
    file = open(filename).read()
    list_of_words = file.rstrip().split()

    for i in range(len(list_of_words)):
        punctuation = ",.!?\"\'()[];_:-*#"
        list_of_words[i] = list_of_words[i].strip(punctuation).lower()

    word_counter = Counter(list_of_words)
    

    for word in sorted(word_counter):
        print(word, word_counter[word])


word_count(file_name)
