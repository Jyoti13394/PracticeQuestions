# Reverse string

def reverse_string(string_1):
    reversed_sent = [word for word in string_1.split('.') if word]
    reversed_sent.reverse()
    return reversed_sent

a = 'i.like.this.program.very.much' 

print(reverse_string(a))


# Longest Common Prefix using Sorting



def longest_string(arr):
    arr.sort()

    first_word = arr[0]
    last_word = arr[-1]
    print(first_word, last_word)
    i = 0
    min_length = len(first_word)
    longest_str = ""
    while i < min_length and first_word[i] == last_word[i]:
        i = i + 1


    return first_word[:i]




arr = ["apple", "ape", "april", "apricot"]
#arr= ["hello", "world"]
print(longest_string(arr))


       
