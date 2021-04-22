from urllib import request

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    return dictonaryRemover(bucket_all(textGet(), 0, longest(textGet())))

def textGet(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    words = []
    file = request.urlopen(book_url)
    for line in file:
        decoded_line = line.decode("utf-8")
        words += decoded_line.split(' ')
    return words

def char_bucketer(words, loc=0):
    buckets = {}
    for word in words:
        try:
            buckets[word[loc:loc+1]].append(word)
        except:
            buckets[word[loc:loc+1]] = [word]
    return buckets

def key_sorter(keys):
    keys = list(keys)
    sorted_keys = []
    for _ in range(len(keys)):
        val = min(keys)
        sorted_keys.append(keys.pop(keys.index(val)))
    return sorted_keys

def bucket_all(words='', depth=0, longer=0):
    out = char_bucketer(words, depth)
    depth += 1
    if depth < longer:
        for key in list(key_sorter(out.keys())):
            if key != '':
                out[key] = bucket_all(out[key], depth, longer)
    return out

def dictonaryRemover(theInput):
    out = []
    if type(theInput) == list:
        return theInput
    else:
        for key in list(key_sorter(theInput)):
            out += dictonaryRemover(theInput[key])
        return out
   
def longest(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

def testAndCompare(words):
    mine = radix_a_book(words)
    python = sorted(words)
    errors = 0
    for index in range(len(mine)):
        if mine[index] != python[index]:
            errors += 1
            print("Failute at index " + str(index))
    print(errors)