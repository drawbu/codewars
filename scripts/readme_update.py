import os
from collections import defaultdict
from pprint import pprint


text = (
    "# My codewars' katas\n\n"
    "These are the solution for the kata I resolved.\n\n"
    "## My solutions:\n\n"
)

katas: dict[str, dict[str, dict[str, str]]] = {
    f"{difficulty}kyu": defaultdict(dict) for difficulty in range(9)
}

for language in os.listdir("src/"):
    for difficulty in os.listdir(f"src/{language}"):
        if len(difficulty) != 4:
            continue
        if not difficulty.endswith("kyu"):
            continue
        try:
            int(difficulty[0])
        except ValueError:
            continue
        for kata in os.listdir(f"src/{language}/{difficulty}"):
            kata_name = kata.split('.')[0].replace('_', ' ').capitalize()
            katas[difficulty][kata_name][language] = kata

for difficulty, katas_list in katas.items():
    if not katas_list:
        continue

    text += (
        f"\n### {difficulty[0]} {difficulty[1:]} "
        f"({len(katas_list)} katas)\n\n"
        "<details>\n"
        "  <summary>\n"
        "    <i>show</i>\n"
        "  </summary>\n\n"
    )
    for title, kata in katas_list.items():
        text += f"- {title} " + " ".join(
            (
                f"[`.{kata_file.split('.')[1]}`]"
                f"(src/{language}/{difficulty}/{kata_file})\n"
            )
            for language, kata_file in kata.items()
        )

    text += "\n</details>\n"

with open("README.md", "w") as f:
    f.write(text)
