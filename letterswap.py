input_string = input("Enter a DNA sequence consisting of the letters A, T, C, and G\n")

def switcher(c: str):
    # combination of matches
    matches = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    # check if the lower version of the char is in the dict by converting it with `.lower()`
    if c.lower() not in matches.keys():
        # if it isn't in the dict just return the letter as-is
        return c
    # get the matching letter - convert to `lower()` in case the letter was uppercase
    found_c = matches[c.lower()]
    # use `.isupper()` to check if the char is upper - if so return an upper case
    # or else just return as is
    return found_c.upper() if c.isupper() else found_c

print(''.join([switcher(i) for i in input_string]))

wrong_sentence = "Ahis is t senaenge where ahe leaaers 'T' tnd 'A', 'G' tnd 'C' htve been swiaghed; pletse gorrega ahis senaenge."

print(''.join([switcher(i) for i in wrong_sentence]))
