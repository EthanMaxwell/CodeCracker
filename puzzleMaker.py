import random

def makePuzzle(file_path, extra_words=0):
    # Read the words from the file into a set
    with open(file_path, 'r') as file:
        all_words = [word.strip().upper() for word in file]

    def check_matches(check_word, poses):
        matches = []
        for word in all_words:
            if len(word) != len(check_word):
                continue
            match = True
            for l in poses:
                if word[l] != check_word[l]:
                    match = False
                    break
            
            if match:
                matches.append(word)
        
        return len(matches)

    num_matches = 100
    starting_word = ""
    starting_poses = []

    while num_matches > 1:
        starting_word = ""
        while len(starting_word) < 4:
            starting_word = random.choice(all_words)

        starting_poses = random.sample(range(len(starting_word)), 2)

        num_matches = check_matches(starting_word, starting_poses)

    known_letters = set()
    known_letters.update({char for char in starting_word})

    words = [starting_word]

    def has_mixed_letters(word, letter_set):
        return any(letter not in letter_set for letter in word) and any(letter in letter_set for letter in word)

    def positions_of_letters(word, letters_to_check):
        return {index for index, letter in enumerate(word) if letter in letters_to_check}


    while len(known_letters) < 26:
        num_matches = 100
        new_word = ""
        while num_matches > 1:
            new_word = random.choice(all_words)
            if not has_mixed_letters(new_word, known_letters):
                continue
            
            new_poses = positions_of_letters(new_word, known_letters)
            
            num_matches = check_matches(new_word, new_poses)
            
        known_letters.update({char for char in new_word})
        words.append(new_word)
        
    starting_letters = {starting_word[i] for i in starting_poses}
    
    add_words = []
    while len(add_words) < extra_words:
        new_word = random.choice(all_words)
        if not any(char in new_word for char in starting_letters):
            add_words.append(new_word)
    
    words += add_words
        
    return words, starting_letters, known_letters
