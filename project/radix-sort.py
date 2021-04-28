import urllib
import requests

#w = maximum key length
#n = number of elements
#k = number of keys

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    text = book_to_words(book_url)
    return dictonaryRemover(bucket_all(text, 0, longest(text)))

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def char_bucketer(words, loc=0): #n
    buckets = {}
    for word in words:
        try:
            buckets[word[loc:loc+1]].append(word)
        except:
            buckets[word[loc:loc+1]] = [word]
    return buckets

def key_sorter(keys): #k^2
    keys = list(keys)
    sorted_keys = []
    for _ in range(len(keys)):
        val = min(keys)
        sorted_keys.append(keys.pop(keys.index(val)))
    return sorted_keys

def bucket_all(words='', depth=0, longer=0): #w*n
    out = char_bucketer(words, depth)
    depth += 1
    if depth < longer:
        for key in list(key_sorter(out.keys())):
            if key != '':
                out[key] = bucket_all(out[key], depth, longer)
    return out

def dictonaryRemover(theInput): #n
    out = []
    if type(theInput) == list:
        return theInput
    else:
        for key in list(key_sorter(theInput)):
            out += dictonaryRemover(theInput[key])
        return out
   
def longest(words): #n
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

def testAndCompare(book_url='https://www.gutenberg.org/files/84/84-0.txt'): #Personal Test
    mine = radix_a_book(book_url)
    python = sorted(book_to_words(book_url))
    errors = 0
    for index in range(len(mine)):
        if mine[index] != python[index]:
            errors += 1
            print("Failute at index " + str(index))
    print(errors)