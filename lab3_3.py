# 409829 % 5 = 4
# ЛОМ расстояние 3
import os
import re

for i in [x for x in os.listdir('lab3_tests/3.3') if x.endswith('.txt')]:
    with open('lab3_tests/3.3/' + i, encoding='utf-8') as f:
        file = f.read()
        pattern = r"\b[\w]*л[^лом]{3}о[^лом]{3}м[\w]*\b"
        matches = re.findall(pattern, file, flags=re.IGNORECASE)
        print(i, matches)

for i in [x for x in os.listdir('lab3_tests/3.3') if x.endswith('.txt')]:
    with open('lab3_tests/3.3/' + i, encoding='utf-8') as f:
        file = f.read().strip().lower()
        indexes = [i for i, letter in enumerate(file) if letter == 'л']
        for j in indexes:
            if j + 8 < len(file):
                if file[j + 4] == 'о' and file[j + 8] == 'м' and file[j:j + 9].count('л') == 1 and file[j:j + 9].count(
                        'о') == 1 and file[j:j + 9].count('м') == 1:
                    print(i, file)
                    break
