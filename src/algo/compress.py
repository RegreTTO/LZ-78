def compress(data: str) -> list:
    dictionary = {}
    compressed = []
    prefix = ""
    for ch in data:
        prefix += ch
        if prefix not in dictionary:
            index = dictionary.get(prefix[:-1], 0)
            compressed += [(index, ch)]
            dictionary[prefix] = len(dictionary) + 1
            prefix = ""
    print(dictionary)
    return compressed
