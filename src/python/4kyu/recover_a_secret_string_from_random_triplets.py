#https://www.codewars.com/kata/53f40dff5f9d31b813000774

from collections import defaultdict


def recoverSecret(triplets: list[list[str]]) -> str:
    data = defaultdict(set)
    for triplet in triplets:
        data[triplet[1]].add(triplet[0])
        data[triplet[2]].update({triplet[0], triplet[1]})

    for _ in range(1000):
        for key in data.copy():
            for letter in data[key].copy():
                data[key].update(data[letter])

    return "".join(
        key[0] for key in sorted(data.items(), key=lambda item: len(item[1]))
    )


def test_recoverSecret():
    assert recoverSecret([
        ['t', 'u', 'p'],
        ['w', 'h', 'i'],
        ['t', 's', 'u'],
        ['a', 't', 's'],
        ['h', 'a', 'p'],
        ['t', 'i', 's'],
        ['w', 'h', 's']
    ]) == "whatisup"
