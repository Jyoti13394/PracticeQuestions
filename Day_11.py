from collections import Counter

Input = 'aaaabbbccd'

#Output- 4a3b2c1d

#i = Counter(Input)
#print(i)

output_string = ''
empty_list = []
for i in Input:
    if i not in empty_list:
        empty_list.append(i)
        counter = Input.count(i)
        output_string = output_string + (str(i)+str(counter))
print(output_string)


############################

# Generate an infinite fibonnaci series by using a generator
# 0,1,1,2,3,5,8,13,....


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i in fib():
    if i <100:
        print(i)

