# Trivia Python Project

Welcome to my Trivia Python project for Computer Science Principals.

This was written using Python 3.9, so it might not work 100% properly on 3.8. I have tried to ensure compatability.

**I am not done with all of the `.questions` files to meet the requirement for 3 questions on the same topic yet**

## To Run

Install the dependancy:
`pip install -r requirements.txt`

And simply execute `main.py`

## About .questions format

Please make sure to follow the syntax properly. I have not yet implemented any syntax checking, so making a mistake might result in undefined behavior.

1. Indentation is not required, but it is encouraged for readablity
2. `.questions` files must end with `end` on the last line, which signals the end of the file
3. Each question declaration is started with `q:`
4. After making a question, an answer token (`a:`) must be the next token used and it needs to be followed by a string that is a potential answer to the question. A user is prompted with all of the answers when playing
5. Each answer must be followed with one points value (an integer defined with the token `p:`) and one comment (a string defined with the token `c:`) provding feedback about that answer to the user that selected it
6. Each question can have as many answers as you wish
7. Lines that start with any thing that is not a token in the `.questions` format (the tokens are `q:`, `a:`, `p:`, `c:`, and `end`) is ignored
8. For the program to detect the `.questions` file, it needs to be in the program directory. This can be changed by passing a `pathlib.Path` object to the call to `get_question_files` in the main function in `main.py`
9. For a sample `.questions` file, see `sample.questions`. You can also look at any of the other ones
