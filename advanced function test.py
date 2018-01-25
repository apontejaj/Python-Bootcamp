# Problem 1
def word_lengths(phrase):
    return map(lambda x: len(x), phrase.split())

print (word_lengths("How long are the words in this phrase"))

# Problem 2
def digits_to_num(digits):
    return (reduce(lambda x,y: (10 * x) + y, digits))

print (digits_to_num([3,4,3,2,1]))

# Problem 3
def filter_words(word_list, letter):
    return (filter(lambda word: word[0]== letter, word_list))

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print (filter_words(l,'h'))

# Problem 4
def concatenate(L1, L2, connector):
    return (["{}{}{}".format(x,connector,z) for x,z in zip(L1,L2)])

print(concatenate(['A','B'],['a','b'],'-'))

# Problem 5
def d_list(L):
   return ({L[x]:x for x in range(len(L))})

print (d_list(['a','b','c']))

# Problem 6
def count_match_index(L):
    return ( len({number:item for number, item in enumerate(L) if number == item }))

print (count_match_index([0,2,2,1,5,5,6,10]))
