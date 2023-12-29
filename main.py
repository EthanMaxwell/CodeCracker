import random

# Specify the path to your text file
file_path = "wordlist.10000.txt"

# Read the words from the file into a set
with open(file_path, 'r') as file:
    all_words = [word.strip().upper() for word in file]

num_matches = 100
starting_word = ""
starting_poses = []

while num_matches > 1:
    while len(starting_word) < 4:
        starting_word = random.choice(all_words)

    starting_poses = random.sample(range(len(starting_word)), 2)

    matches = []
    for word in all_words:
        if len(word) != len(starting_word):
            continue
        match = True
        for l in starting_poses:
            if word[l] != starting_word[l]:
                match = False
                break
        
        if match:
            matches.append(word)
            
    num_matches = len(matches)

print(starting_word)  
print(num_matches)
print(starting_poses)