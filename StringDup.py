def getMax(param0):
    freq = {} # freq[c] = (len - first_index, freq)
    for i, character in enumerate(param0):
        if character in freq:
            freq[character][1] += 1
        else:
            freq[character] = [len(param0) - i, 1]
    return max((freq[c][1], freq[c][0], c) for c in freq)[-1]
