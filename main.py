from puzzleMaker import makePuzzle
from textInterface import printPuzzle
from userInterface import startUserInterface

words, starting_letters, all_letters = makePuzzle("enable-170000.txt")

#printPuzzle(words, starting_letters, all_letters)
startUserInterface(words, starting_letters, all_letters)