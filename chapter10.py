import re
from pathlib import Path


def create_mad_libs(input_filename: str, output_filename: str) -> None:
    input_path = Path(input_filename)
    output_path = Path(output_filename)

    try:
        text = input_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found: {input_filename}")
        return

    prompts = {
        "ADJECTIVE": "Enter an adjective: ",
        "NOUN": "Enter a noun: ",
        "ADVERB": "Enter an adverb: ",
        "VERB": "Enter a verb: ",
    }

    def replace_word(match: re.Match) -> str:
        word_type = match.group()
        return input(prompts[word_type])

    completed_text = re.sub(
        r"\b(ADJECTIVE|NOUN|ADVERB|VERB)\b",
        replace_word,
        text,
    )

    print("\nCompleted Mad Lib:\n")
    print(completed_text)

    output_path.write_text(completed_text, encoding="utf-8")
    print(f"\nSaved to: {output_filename}")


create_mad_libs("madlibs.txt", "completed_madlibs.txt")