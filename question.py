from typing import List


class Question:
    def __init__(self, question: str):
        self._question = question
        self._answers: List[str] = []
        self._points_values: List[int] = []
        self._comments: List[str] = []

    def __repr__(self) -> str:
        return self._question

    def add_answer(self, answer: str, points_value: int, comment: str):
        """Adds an answer."""
        self._answers.append(answer.lower())
        self._points_values.append(points_value)
        self._comments.append(comment)

    def get_points_value(self, answer: str) -> int:
        """Returns the points value for a given answer"""
        answer = answer.lower()
        answer_index = self._answers.index(answer)
        return self._points_values[answer_index]

    def get_comment(self, answer: str) -> str:
        """Returns the comment for a given answer"""
        answer = answer.lower()
        answer_index = self._answers.index(answer)
        return self._comments[answer_index]

    def get_question(self) -> str:
        """Returns the question"""
        return self._question

    def get_answers(self) -> List[str]:
        """Returns a list containing all of the answers"""
        return self._answers
