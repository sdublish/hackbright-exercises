"""Generate Markov text from text files."""

from random import choice
import sys

file_name = sys.argv[1]
n_gram = int(sys.argv[2])


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    return open(file_path).read()


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    words_lst = text_string.split()
    chains = {}

    for i in range(len(words_lst) - n):
        key = tuple(words_lst[i:i+n])
        chains[key] = chains.get(key, [])
        chains[key].append(words_lst[i+n])

    return chains


def make_text(chains, n):
    """Return text from chains."""

    words = []

    keys_lst = list(filter(lambda x: x[0][0].isupper(), chains.keys()))
    # keys_lst = list(chains.keys())
    # creates a list of keys which start with a capital letter

    # fill list with tuples
    init_key = choice(keys_lst)
    # assign random the whole tuple-key
    # while init_key[0][0].islower() or not init_key[0][0].isalpha():
    #     init_key = choice(keys_lst)

    words.extend(init_key)
    # add the tuple-key to word list

    next_word = choice(chains[init_key])
    # picking value-word, assign to next_word

    words.append(next_word)
    # adding value-word to our generated sentence

    while True:
        next_key = tuple(words[-n:])

        if next_key in chains:
            next_word = choice(chains[next_key])
            # checks dict for key match, then gets the next word (if applicable)
            words.append(next_word)
            if next_word[-1] in '.!?':
                break
        else:
            break

    print(words)

    return " ".join(words)


# Open the file and turn it into one long string
input_text = open_and_read_file(file_name)

# Get a Markov chain
chains = make_chains(input_text, n_gram)

# Produce random text
random_text = make_text(chains, n_gram)

print(random_text)
