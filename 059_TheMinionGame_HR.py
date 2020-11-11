# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules:
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Reference: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    n = len(string)
    # Total possible substrings are given by sum of natural numbers till n
    total = (n*(n+1))//2
    vowel = 0
    for i in range(n):
        if(string[i] in 'AEIOU'):
            vowel = vowel+n-i
    conso = total-vowel
    if(vowel > conso):
        print('Kevin', vowel)
    elif(conso > vowel):
        print('Stuart', conso)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
