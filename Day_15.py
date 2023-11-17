# To print all missing numbers and strings from the given string
import string
s = "789667huhkjlkjdty989"
digits = [0,1,2,3,4,5,6,7,8,9]
final_result = ""
comp_str = string.ascii_lowercase
for each in range(9, -1 ,-1):
    comp_str = str(each) + comp_str

for each in comp_str:
    if each not in s:
        final_result = final_result + each
#print(comp_str)
print(final_result)
