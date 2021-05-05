import argparse
import sys
from GUI import gui
from console import console


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--insert')
    parser.add_argument('-v', '--view')
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.insert !=None:
        console.get(str(namespace.insert))
    elif namespace.view !=None:
        print(console.view())
    else :
        gui.wind()
