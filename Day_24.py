# Reverse string

def reverse_string(string_1):
    reversed_sent = [word for word in string_1.split('.') if word]
    reversed_sent.reverse()
    return reversed_sent

a = 'i.like.this.program.very.much' 

print(reverse_string(a))