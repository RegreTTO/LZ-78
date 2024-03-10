import re

def decompress(data: str):
    PATTERN = re.compile(r"\((\d), '([^']+)'\)")
    tokens = list(re.findall(PATTERN, data))
    dictionary = {0: ''}
    dec = ""
    for token in tokens:
        i, ch = token
        pref = dictionary[int(i)] + ch
        dec += pref
        dictionary[len(dictionary)] = pref
    print(dictionary)
    return dec
        