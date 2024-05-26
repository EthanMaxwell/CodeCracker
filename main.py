import os

from puzzleMaker import makePuzzle
from textInterface import printPuzzle
from userInterface import startUserInterface

wordFile = "wordLists/5000-more-common.txt"

def get_data_file_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, wordFile)

words, starting_letters, all_letters = makePuzzle(get_data_file_path())

printPuzzle(words, starting_letters, all_letters)
startUserInterface(words, starting_letters, all_letters)
