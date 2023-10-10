input_string = input("Enter a DNA sequence consisting of the letters A, T, C, and G\n")

def switcher(c: str):
    matches = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    if c.lower() not in matches.keys():
        return c
    found_c = matches[c.lower()]
    return found_c.upper() if c.isupper() else found_c

print(''.join([switcher(i) for i in input_string]))

wrong_sentence = "Ahis is t senaenge where ahe leaaers 'T' tnd 'A', 'G' tnd 'C' htve been swiaghed; pletse gorrega ahis senaenge."

print(''.join([switcher(i) for i in wrong_sentence]))