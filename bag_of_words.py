def bag_of_words(corpus):

    dict = {}

    for sentence in corpus:
        words = sentence.split(" ")
        for word in words:
            if word not in dict:
                dict[word] = 1

    word_list = dict.keys()
    to_return = []

    for sentence in corpus:
        to_add = [0] * len(word_list)
        words = sentence.split(" ")

        for word in words:
            i = 0
            for item in word_list:
                if item == word:
                    to_add[i] += 1
                    break
                i += 1
        to_return.append(to_add)
    return to_return



corpus = ['this is the first document',
          'this document is the second document',
          'and this is the third one',
          'is this the first document']

print(bag_of_words(corpus))
