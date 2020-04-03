

def listVersion():
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = input("Provide a word to search for vowel.")
    found = []

    for letter in word:
        if letter.lower() in vowels:
            if letter not in found:
                found.append(letter)

    for vowel in found:
        print(vowel)


def setVersion():
    vowels = set('aeiouaeiouAEIOUAEIOU')  # set , no duplicate
    word = input("Provide a word to search for vowel.")
    found = vowels.intersection(set(word))

    for vowel in sorted(found):
        print(vowel)


def tupleVersion():
    vowels = ('a', 'e', 'i', 'o', 'u')
    word = input("Provide a word to search for vowel.")
    found = []

    for letter in word:
        if letter.lower() in vowels:
            if letter not in found:
                found.append(letter)

    for vowel in found:
        print(vowel)


def dictVersion():
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = input("Provide a word to search for vowel.")
    found = {'a': 0, 'e': 0, 'i': 0, 'o': 0}
    found['u'] = 0

    for letter in word:
        if letter.lower() in vowels:
            found[letter] += 1

    for k, v in sorted(found.items()):
        # print(k, 'was found ', found[k], " time(s).")
        print(k, 'was found ', v, " time(s).")


def dictVersion2():
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = input("Provide a word to search for vowel.")
    found = {}

    for letter in word:
        lowLetter = letter.lower()
        if lowLetter in vowels:
            found.setdefault(lowLetter, 0)
            found[lowLetter] += 1

    for k, v in sorted(found.items()):
        print(k, 'was found ', v, " time(s).")


def search4vowels(word: str) -> bool:
    """ Return a boolean based on any vowels found. """
    vowels = set('aeiouAEIOU')
    found = vowels.intersection(set(word))
    return bool(found)


def search4letters(phrase: str, letter: str='aeiouAeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'"""
    return set(letter).intersection(set(phrase))


# print(search4letters("Today is a nice day", "ToDaY"))
print(search4letters(letter="ToDay", phrase="Today is a nice day"))
# print(search4letters("Today is a nice day"))
# print(search4vowels("Today is a nice day"))
# tupleVersion()
# setVersion()
# listVersion()
# dictVersion()
# dictVersion2()