# 409829 % 6 = 5
import os
import re

# "\w*[ui:ауоыиэяюёе]{2}\w*\s\w*[ui:бвгджзйклмнпрстфхцчшщ]{,3}\w*"g
for i in [x for x in os.listdir('lab3_tests/3.2') if x.endswith('.txt')]:
    with open('lab3_tests/3.2/' + i, encoding='utf-8') as f:
        file = f.read()
        # pattern = '\\b\w*[уеыаоэяию]{2}\w*\s+\\b\w*[^уеыаоэяию\s]{0,3}\\b'
        pattern = r"(\b[\w]*[ёуеыаоэяию]{2}[\w]*\b)\W+\b(?:[ёуеыаоэяию]*[йцкнгшщзхъждлрпвфчсмтьб]|[ёуеыаоэяию]+){1,3}[ёуеыаоэяию]*\b"
        matches = re.findall(pattern, file, flags=re.IGNORECASE)
        print(i, [x for x in matches])

for i in [x for x in os.listdir('lab3_tests/3.2') if x.endswith('.txt')]:
    with open('lab3_tests/3.2/' + i, encoding='utf-8') as f:
        file = f.read().rstrip()
        for n in '.,-':
            file = file.replace(n, '')
        file = file.split()
        print(i, end=' ')
        for x in range(len(file) - 1):
            glas = 'уеыаоэяию'
            l = 0
            for z in file[x]:
                if z in glas:
                    l += 1
                    if l == 2:
                        break
                else:
                    l = 0
            if l == 2:
                k = 0
                for y in file[x + 1]:
                    if y not in 'уеыаоэяию':
                        k += 1
                if k < 4:
                    print(file[x], end=' ')
    print('')
