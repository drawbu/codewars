# https://www.codewars.com/kata/586dd26a69b6fd46dd0000c0/solutions/python


def interpreter(code: str, tape: str) -> str:
    pointer = 0
    i = -1
    tape = list(tape)
    loop_indexes = []
    while len(code) > i + 1:
        i += 1
        if code == "*>[[]*>]<*":
            print(i, code[i])
        match code[i]:
            case ">":
                if pointer + 1 == len(tape):
                    return "".join(tape)
                pointer += 1
            case "<":
                if pointer == 0:
                    return "".join(tape)
                pointer -= 1
            case "*":
                tape[pointer] = str((int(tape[pointer]) + 1) % 2)
            case "[":
                if tape[pointer] == "0":
                    nested = 0
                    for _ in code[i:]:
                        if i + 1 == len(code):
                            return "".join(tape)
                        i += 1
                        if code[i] == "[":
                            nested += 1
                            continue
                        if code[i] == "]":
                            if nested > 0:
                                nested -= 1
                                continue
                            break
                    continue
                loop_indexes.append(i)
            case "]":
                i = loop_indexes.pop(-1) - 1
    return "".join(tape)


def test_my_first_interpreter():
    assert interpreter("*", "00101100") == "10101100"
    assert interpreter(">*>*", "00101100") == "01001100"
    assert interpreter("*>*>*>*>*>*>*>*", "00101100") == "11010011"
    assert interpreter("*>*>>*>>>*>*", "00101100") == "11111111"
    assert interpreter(">>>>>*<*<<*", "00101100") == "00000000"
    assert interpreter("*[>*]", "0000000000000000000") == "1111111111111111111"
    assert interpreter("[>*]", "0000000000000000000") == "0000000000000000000"
    assert interpreter("*>[[]*>]<*", "100") == "100"
    assert interpreter("[*>[>*>]>]", "11001") == "01100"
