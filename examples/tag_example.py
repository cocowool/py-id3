import sys

# 这里改为自己本机 pyID3 的存储目录
sys.path.insert(0, '~/Project/py-id3/src/pyID3')

from pyID3 import pyID3
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