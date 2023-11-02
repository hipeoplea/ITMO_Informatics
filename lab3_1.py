#409829 % 6 = 5
#409829 % 4 = 1
#409829 % 7 = 0
#Смайлик - [<(
import os
import re

print('solve using re')
for i in [x for x in os.listdir('lab3_tests/3.1') if x.endswith('.txt')]:
    with open('lab3_tests/3.1/' + i, encoding='utf-8') as f:
        file = f.read()
        print(i, len(re.findall('\[<\(', file)), end='\n')

print('solve without using re')
for i in [x for x in os.listdir('lab3_tests/3.1') if x.endswith('.txt')]:
    with open('lab3_tests/3.1/' + i, encoding='utf-8') as f:
        file = f.read()
        word = ''
        k = 0
        for j in file:
            if j == '[':
                word += '['
            elif j == '<' and word == '[':
                word += '<'
            elif j == '(' and word == '[<':
                k += 1
                word =  ''
            else:
                word = ''
        print(i, k)
