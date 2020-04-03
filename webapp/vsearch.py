def search4letters(phrase: str, letter: str='aeiouAeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'"""
    return set(letter).intersection(set(phrase))