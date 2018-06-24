"""A Markov chain generator that can tweet random messages."""

import os
import sys
from random import choice
import twitter


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

    proto_markv = " ".join(words)[:280]
    if proto_markv[-1] not in '.!?':
        proto_markv_lst = proto_markv.split()
        proto_markv_lst[-2:] = []
        proto_markv = " ".join(proto_markv_lst) + "..."

    return proto_markv


def tweet(chains, n_gram):
    """Create a tweet and send it to the Internet."""

    # Use Python os.environ to get at environmental variables
    # Note: you must run `source secrets.sh` before running this file
    # to make sure these environmental variables are set.
    api = twitter.Api(consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
                      consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                      access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                      access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
                      )

    show_last_tweet(api)

    status = api.PostUpdate(make_text(chains, n_gram))
    print(status.text)
    print("\n")
    

def show_last_tweet(api):
    statuses = api.GetUserTimeline(screen_name=os.environ["TWITTER_HANDLE"])
    print("Here is your last tweet:\n")
    print(statuses[0].text)

# Get the filenames from the user through a command line prompt, ex:
# python markov.py green-eggs.txt shakespeare.txt
# Open the file and turn it into one long string
input_text = open_and_read_file(file_name)


# Get a Markov chain
chains = make_chains(input_text, n_gram)

tweet(chains, n_gram)

while True:
    if input("Enter to tweet again [q to quit]: ") == '':
        tweet(chains, n_gram)

    else:
        quit()

# # Your task is to write a new function tweet, that will take chains as input
# # tweet(chains)
