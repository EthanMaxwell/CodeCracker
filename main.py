import os
import time

from puzzleMaker import makePuzzle
from textInterface import printPuzzle
from userInterface import startUserInterface

wordFile = "5000-more-common.txt"

if os.path.exists("./wordLists/" + wordFile):
    wordFile = "./wordLists/" + wordFile
else:
    wordFile = "./_internal/" + wordFile

words, starting_letters, all_letters = makePuzzle(wordFile)

printPuzzle(words, starting_letters, all_letters)
startUserInterface(words, starting_letters, all_letters)
