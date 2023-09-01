import re
'''Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .'''

s = 'Banana'
s= s.lower()
point_of_a = 0
point_of_b = 0
for i in range(0, len(s)):
    if s[i] in ['a', 'e', 'i', 'o', 'u']:
        point_of_a = point_of_a + (len(s) - i)
    else:
        point_of_b = point_of_b + (len(s) - i)

print(f"point_of_a is", point_of_a)
print(f"point_of_b is", point_of_b)


# You are given a string S.
# Your task is to find the indices of the start and end of string k in S.
# Print the tuple in this format: (start _index, end _index).
# If no match is found, print (-1, -1).


S, k = input(), input()
pat = re.compile(k)
m = pat.search(S)

if m:
    while m:
        print((m.start(), m.end()-1))
        i = m.start() + 1
        m = pat.search(S, i)
else:
    print((-1, -1))
