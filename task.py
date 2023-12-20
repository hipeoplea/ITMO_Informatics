def task():
    sourceFile = open('lessons.xml', encoding='utf-8', mode='r')
    lines = sourceFile.readlines()

    YAMLdata = ''
    depth = 0
    flag = False
    for line in lines:
        line = line.strip().replace('<', '>').split('>')[1:-1]

        if len(line) > 2:
            line = line[:-1]

        if len(line) == 1:
            if line[0][0] == '/':
                if not line[0] == '/lesson':
                    depth -= 1
            elif line[0] == 'lesson':
                if not flag:
                    YAMLdata += f"{'  ' * depth}{line[0]}:\n"
                    depth += 1
                    flag = True
            else:
                YAMLdata += f"{'  ' * depth}{line[0]}:\n"
                depth += 1
        else:
            if len(line) == 0:
                line = ""
            else:
                if line[0] == 'Type':
                    YAMLdata += f"{' ' * depth}- {line[0]}: {line[1]}\n"
                else:
                    YAMLdata += f"{'  ' * depth}{line[0]}: {line[1]}\n"

    fileOutput = open('lessons.yaml', encoding='utf-8',  mode='w')
    fileOutput.write(YAMLdata)
task()