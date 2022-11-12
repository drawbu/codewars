from collections import defaultdict


def recoverSecret(triplets: list[list[str]]) -> str:
    data = defaultdict(list)
    for triplet in triplets:
        data[triplet[1]].append(triplet[0])
        data[triplet[2]] += [triplet[0], triplet[1]]
    secret = []

    for key in data.copy():
        for letter in data[key]:
            data[key] += data[letter]
        data[key] = list(set(data[key]))
    data = dict(data)
    for key in data:
        data[key] = len(data[key])
    return "".join(secret)


def test_recoverSecret():
    secret = "whatisup"
    triplets = [
        ['t', 'u', 'p'],
        ['w', 'h', 'i'],
        ['t', 's', 'u'],
        ['a', 't', 's'],
        ['h', 'a', 'p'],
        ['t', 'i', 's'],
        ['w', 'h', 's']
    ]
    assert recoverSecret(triplets) == secret


if __name__ == "__main__":
    test_recoverSecret()
