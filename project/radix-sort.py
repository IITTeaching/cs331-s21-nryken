import urllib
import requests

#w = maximum element length
#n = number of elements

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'): #w*n
    text = book_to_words(book_url)
    sortedText = listRemover(bucket_all(text, 0, longest(text)))

    return sortedText

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')

    return bookascii.split()

def listRemover(theList): #w*n
    out = []
    for part in theList:
        if type(part) == list:
            out += listRemover(part)
        elif part != None:
            out.append(part)

    return out

def char_bucketer(words, depth=0): #n
    buckets = [None]*129
    for word in words:
        try:
            index = word[depth]
            if buckets[index] == None:
                buckets[index] = [word]
            else:
                buckets[index].append(word)
        except:
            if buckets[0] == None:
                buckets[0] = [word]
            else:
                buckets[0].append(word)

    return buckets

def bucket_all(words='', depth=0, longer=0): #w*n
    buckets = char_bucketer(words, depth)
    depth += 1
    if depth < longer:
        for index in range(1, len(buckets)):
            if buckets[index] != None and len(buckets[index]) > 1:
                buckets[index] = bucket_all(buckets[index], depth, longer)

    return buckets

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
    print('There were ' + str(errors) + ' number of errors between mine of length ' + str(len(mine)) + ' and python of length ' + str(len(python)))
