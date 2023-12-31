import random

def printPuzzle(words, starting_letters, all_letters):
    random_letters = random.sample(list(all_letters), len(all_letters))
    random_words = random.sample(words, len(words))

    # Print out puzzle
    print("Letters:")
    for i in range(len(all_letters)):
        print(str(i).zfill(2), end=" ")   
    print()
    for i in range(len(all_letters)):
        if random_letters[i] in starting_letters:
            print(random_letters[i], end="  ")
        else:
            print("__", end=" ")

    print("\nWords:")

    for word in random_words:
        for i in range(len(word)):
            print(str(random_letters.index(word[i])).zfill(2), end=" ")
        print()
        for i in range(len(word)):
            if word[i] in starting_letters:
                print(word[i], end="  ")
            else:
                print("__", end=" ")
        print('\n')
        
    print('\n' *10 + "Solution:")
    for i in range(len(all_letters)):
        print(str(i).zfill(2), end=" ")   
    print()
    for i in range(len(all_letters)):
        print(random_letters[i], end="  ")
    print()
    for word in random_words:
        print(word + " " + str(words.index(word)))
        
    print(len(words))