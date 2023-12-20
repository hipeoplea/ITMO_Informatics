from pars import Parser

def dop3():
    parser = Parser()
    parser.loadXML('test1.xml')
    parser.writeYAML('test1.yaml')

dop3()
