def best_handles(handle, handles, k = 2):

    handles_score = []
    handle = handle.lower()

    for value in handles:
        #print(value)
        value = value.lower()
        score = 0
        used_letters = set()
        for letter in handle:

            if not letter in used_letters:
                #print(letter)
                if letter in value:
                    score += 1
                else:
                    score -= 1

            used_letters.add(letter)

        for letter in value:

            if not letter in used_letters:
                #print(letter)
                if letter in handle:
                    score += 1
                else:
                    score -= 1

            used_letters.add(letter)

        handles_score.append((score,value))

    handles_score.sort()
    #print(handles_score)
    return handles_score[-k:]

handle = "ilovedogs"
handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']

print(best_handles(handle, handles))
