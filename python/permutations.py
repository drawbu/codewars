# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python

def recur_permutations(s: str, i: int = 0) -> list[str]:
    return [s] if i+2 > len(s) else list(set(
        [s]
        + recur_permutations(s, i+1)
        + recur_permutations(s[:i] + s[i + 1] + s[i] + s[i + 2:], i + 1)
    ))


def permutations(s: str):
    result = recur_permutations(s)
    for _ in range(len(s)):
        for e in result.copy():
            result += recur_permutations(e)
    return list(set(result))


if __name__ == "__main__":
    for e in ("abcd", ):
        print(e, list(sorted(permutations(e))))
