import sys

sys.path.append('../src/')

import pyID3
import os

path = "/Users/rousseau/shiqiang/Music/iTunes/iTunes Media/Music"

def findMp3(path):
    files = os.listdir(path)
    for f in files:
        if( os.path.isdir(os.path.join(path,f)) ):
            findMp3( os.path.join(path,f) )
        else:
            fh = open(os.path.join(path,f), "rb")
            print(parse(fh))

findMp3(path)