import random
print("Guess the charaters of the word")
words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'garden', 'football', 'gaming', 'tennis', 'fire', 'ice', 'thor', 'birthday', 'captain', 'tolerate']
word=random.choice(words)
guesses=''
turns=12
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed +=1
    if failed==0:
        print("You win")
        print('the word is: ', word)
        break
    guess=input('Guess a character:')
    guesses+=guess
    if guess not in word:
        turns-=1
        print('Wrong')
        print('You have',turns,'more guesses')
        if turns==0:
            print('You loose,better luck next time')