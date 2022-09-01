import os
import random
import sys
import time
from pathlib import Path
from typing import Any, List, Sequence
from colorama import init as colorama_init, Fore

from questions_reader import questions_reader


def get_questions_files(path_to_search: Path = Path.cwd()) -> List[Path]:
    """Returns a list of pathlib.Path containing all of the paths to .questions files in the specified directory
    
    path_to_search must be a directory"""
    if path_to_search.is_file(): raise ValueError(path_to_search)

    questions_files: List[Path] = []

    for file in path_to_search.iterdir():
        if str(file).endswith(".questions"):
            questions_files.append(file)

    return questions_files


def valid_int_input(lower_limit: int,
                    upper_limit: int,
                    prompt: str = "Enter a Number: ") -> int:
    """Get a valid int input
    lower_limit and upper_limit are inclusive"""
    while True:
        user_input = input(Fore.YELLOW + prompt)
        try:
            as_num = int(user_input)
        except ValueError:
            # Was not an int
            continue
        if not lower_limit <= as_num <= upper_limit:
            # Does not fit between upper and lower limit
            continue
        return as_num


def choice(options: Sequence[Any]) -> Any:
    """Lets the user choose from a selection of options, returns the index of the chosen option"""
    for num, option in enumerate(options, 1):
        print(Fore.MAGENTA + f"\t[{num}] {option}")

    # Get a valid int input
    index = valid_int_input(1, len(options)) - 1
    return options[index]


def clear_term() -> None:
    """Clears the terminal"""
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def main():
    colorama_init(True)
    points: int = 0

    # Let user select a set of questions
    questions_files = get_questions_files()
    if len(questions_files) == 0:
        print("No files with the extention .questions were found, exiting")
        exit(1)

    print(f"""{Fore.GREEN} It's trivia time!

    {Fore.CYAN}Please select a set of questions to play with:""")

    for num, file in enumerate(questions_files, 1):
        print(f"\t[{num}] {file.stem}")

    # Get a valid int input
    set_index = valid_int_input(1, len(questions_files)) - 1

    clear_term()
    # Read the questions file
    questions = questions_reader(questions_files[set_index])
    # Main loop
    while len(questions) > 0:
        # Pick the question to ask the user
        question = random.choice(questions)
        # ask the user it
        print(question)
        # let the user answer one of the answers
        answers = question.get_answers()
        random.shuffle(answers)
        answer = choice(answers)
        # give user the comment as feedback
        print(question.get_comment(answer))
        # inc points accordinly
        points += question.get_points_value(answer)
        # remove the question so it is not used again
        questions.remove(question)
        input("Press enter to continue")
        clear_term()
    # Done with all questions
    clear_term()
    print(
        f"{Fore.LIGHTGREEN_EX}Thanks for playing! Your final score was {points}!"
    )


if __name__ == "__main__": main()