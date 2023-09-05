# Python program to read file word by word
import os
print(os.getcwd())

with open(r'C:\Users\prasa\OneDrive\Desktop\pythonProject\Python Prac Ques\File_Data\word_by_word.txt', 'r') as file:
    # Reading each line
    for line in file:
        for word in line.split():
            print(word)


# Python program to read character by character from a file

with open(r'C:\Users\prasa\OneDrive\Desktop\pythonProject\Python Prac Ques\File_Data\word_by_word.txt', 'r') as file_1:
    while 1:
        chr = file_1.read(2)
        if not chr:
            break
        print(chr)

# Eliminating repeated lines from a file using Python
lines = set()
with open(r'C:\Users\prasa\OneDrive\Desktop\pythonProject\Python Prac Ques\File_Data\removed_repaeted_lines.txt', 'w') as write_file:
    with open (r'C:\Users\prasa\OneDrive\Desktop\pythonProject\Python Prac Ques\File_Data\repaeted_lines.txt', 'r') as read_file:
        for line in read_file:
            if line not in lines:
                write_file.write(line)
                lines.add(line)