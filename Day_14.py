def printAl(arr, n):
    elements = " ".join(str(arr[i]) for i in range(n) if i % 2 == 0)
    return elements


n = 4

arr = [1, 2, 3, 4]

print(printAl(arr, n))


# To reverse the sentence and swap case of e ach letter
sentence = "Dogs are good"
new_sent = []
for word in sentence.split()[::-1]:
    word = word.swapcase()
    new_sent.append(word)
    new_sentence = " ".join(each for each in new_sent)
print(new_sentence)


rev_sen= sentence.split()[::-1]
print(rev_sen)


