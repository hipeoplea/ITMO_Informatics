import re

def dop2():
    sourceFile = open('lessons.xml', encoding='utf-8',  mode='r')

    depth = 0
    reData = []
    flag = False

    for line in sourceFile.readlines():
        line = line.strip()

        diff = line.count('<') - 2 * line.count('</')

        if diff == -1:
            depth -= 1
        elif diff == 0:
            if '<Type>' in line:
                reData.append(re.sub('<', ' ' * depth + '- ', re.sub('>', ': ', re.sub('<\/\w*>', '', line))))
            else:
                reData.append(re.sub('<', '  ' * depth, re.sub('>', ': ', re.sub('<\/\w*>', '', line))))
        else:
            if 'lesson' not in line:
                reData.append(re.sub('<', '  ' * depth, re.sub('>', ':', line)))
            depth += 1

    outputFile = open('lessons.yaml', encoding='utf-8', mode='w')
    outputFile.write('\n'.join(reData))

dop2()