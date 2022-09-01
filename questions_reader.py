from typing import List
from question import Question
from pathlib import Path


def questions_reader(questions_path: Path) -> List[Question]:
    """Takes a path to a .questions file and translates the contents into a list of Questions"""
    # It should be fully implmented, but missing error handling and proper syntax checking
    with questions_path.open('r') as file:
        data = file.readlines()

    making_question: bool = False
    current_question: Question = Question("")
    # Tells which parts needed for constructed the answer have been found
    # Order is points_value, comment
    current_answer_progress: List = [False, False]
    current_answer: str = ""
    current_points_value: int = 0
    current_comment: str = ""

    all_questions: list[Question] = []

    for line in data:
        line = line.strip()
        if line.startswith("q:") or line.startswith("end"):
            if making_question:
                all_questions.append(current_question)
            making_question = True
            current_question = Question(line[2:])
        elif line.startswith("a:"):
            if not making_question:
                raise SyntaxError(
                    "Expected a question declaration before this line: " +
                    line)
            current_answer = line[2:]
        elif line.startswith("p:"):
            current_answer_progress[0] = True
            current_points_value = int(line[2:])
        elif line.startswith("c:"):
            current_answer_progress[1] = True
            current_comment = line[2:]

        if not (False in current_answer_progress):
            current_question.add_answer(current_answer, current_points_value,
                                        current_comment)
            current_answer_progress = [False, False]

    return all_questions


if __name__ == "__main__":
    print("This file is not intended to be run")