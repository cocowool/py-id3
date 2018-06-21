import sys

sys.path.append('/Users/rousseau/Projects/python.my/py-id3/src/pyID3')

import tag
import os

print(sys.path)
path = "/Users/rousseau/shiqiang/Music/iTunes/iTunes Media/Music"

def findMp3(path):
    files = os.listdir(path)
    for f in files:
        if( os.path.isdir(os.path.join(path,f)) ):
            findMp3( os.path.join(path,f) )
        else:
            fh = open(os.path.join(path,f), "rb")
            print(tag.parse(fh))

# print(tag)

findMp3(path)