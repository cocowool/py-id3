import os

path = "/Users/rousseau/shiqiang/Music/iTunes/iTunes Media/Music"

def findMp3(path):
    files = os.listdir(path)
    for f in files:
        if( os.path.isdir(os.path.join(path,f)) ):
            findMp3( os.path.join(path,f) )
        else:
            checkIdv(os.path.join(path,f))

def checkIdv(file_name):
    fh = open(file_name, "rb")
    fh.seek(-128,2)
    id3v_data = fh.read()
    fh.close()
    # print(id3v_data[0:3])
    if(id3v_data[0:3] == b'TAG'):
        print(file_name)
        print(id3v_data)

findMp3(path)