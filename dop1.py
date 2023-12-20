import xmltodict
import yaml

def dop1():
    sourceFile = open('lessons.xml', encoding='utf-8',  mode='r')
    lines = sourceFile.read()

    xmlDict = xmltodict.parse(lines)

    outputFile = open('lessons.yaml', encoding='utf-8', mode='w')
    yaml.dump(xmlDict, outputFile, default_flow_style=False, allow_unicode=True)
dop1()