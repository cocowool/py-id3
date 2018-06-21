# Read ID3v1 tag information
import os
import string

def parse(fileObj, version = 'v1'):
    fileObj.seek(0,2)
    # ID3v1's max length is 128 bytes
    if(fileObj.tell() < 128):
        return False
    fileObj.seek(-128,2)
    tag_data = fileObj.read()

    if(id3v_data[0:3] != b'TAG'):
        return False
    
    return getTag(tag_data)

# Get ID3v1 tag data
def getTag(tag_data):
    tags = {}
    tags['title'] = tag_data[3,33]

    tags['artist'] = tag_data[33:63]

    tags['album'] = tag_data[63:93]

    tags['year'] = tag_data[93:97]

    tags['comment'] = tag_data[97:127]
    #@TODO Need to analyze comment to verfiy v1 or v1.1

    tags['genre'] = ord(tag_data[127:128])

    return tags

# Set ID3v1 tag data
def setTag():
    pass