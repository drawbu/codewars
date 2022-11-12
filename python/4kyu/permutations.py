# https://www.codewars.com/kata/5254ca2719453dcc0b00027d


def permutations(s: str) -> list[str]:
    result = []
    temp = [s]
    while temp:
        e = temp[0]
        result.append(e)
        temp.pop(0)

        for i in range(len(e) - 1):
            if e[i] == e[i + 1]:
                continue

            perm = e[:i] + e[i + 1] + e[i] + e[i + 2:]
            if perm in temp or perm in result:
                continue
            temp.append(perm)
    return result


def test_permutations() -> None:
    import timeit

    assert sorted(permutations("a")) == ["a"]
    assert sorted(permutations("ab")) == ["ab", "ba"]
    assert sorted(permutations("aabb")) == [
        "aabb", "abab", "abba", "baab", "baba", "bbaa"
    ]
    assert sorted(permutations("abcd")) == [
        "abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "bacd", "badc",
        "bcad", "bcda", "bdac", "bdca", "cabd", "cadb", "cbad", "cbda",
        "cdab", "cdba", "dabc", "dacb", "dbac", "dbca", "dcab", "dcba",
    ]
    assert timeit.timeit(lambda: permutations("abdefgh"), number=1) < 0.25
