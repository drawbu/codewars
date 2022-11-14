import os

text = (
    "# My codewars' katas\n\n"
    "These are the solution for the kata I resolved.\n\n"
    "## My solutions:\n\n"
)
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

        text += (
            f"\n### {difficulty[0]} {difficulty[1:]} "
            f"({len(os.listdir(f'src/{language}/{difficulty}'))} katas)\n\n"
            "<details>\n"
            "  <summary>\n"
            "    <i>show</i>\n"
            "  </summary>\n\n"
        )
        for kata in os.listdir(f"src/{language}/{difficulty}"):
            text += (
                f"- {kata.split('.')[0].replace('_', ' ').capitalize()} "
                f"[`.{kata.split('.')[1]}`]"
                f"(src/{language}/{difficulty}/{kata})\n"
            )

        text += "\n</details>\n"

with open("README.md", "w") as f:
    f.write(text)
