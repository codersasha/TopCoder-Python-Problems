sums = { # sums[n] = set([sums])
    1: set(),
    2: set([(2,)]),
    3: set(),
    4: set([(2, 2)]),
    5: set([(2, 3)]),
    6: set([(3, 3), (2, 2, 2)]),
    7: set([(2, 2, 3), (7,)])
}

DENOMINATIONS = [2, 3, 7]

def fetchCombinations(n):
    for i in range(8, n + 1):
        sums[i] = set([])
        for d in DENOMINATIONS:
            if i - d > 0:
                for x in sums[i - d]:
                    # if we add the sorted tuple, duplicates won't be added
                    # needs to be a tuple so it's hashable by the set
                    sums[i].add(tuple(sorted(x + (d,))))
    return len(sums[n])
