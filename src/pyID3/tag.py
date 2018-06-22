# Read ID3v1 tag information
import os
import string
import base64
import chardet

def parse(fileObj, version = 'v1'):
    fileObj.seek(0,2)
    # ID3v1's max length is 128 bytes
    if(fileObj.tell() < 128):
        return False
    fileObj.seek(-128,2)
    tag_data = fileObj.read()

    if(tag_data[0:3] != b'TAG'):
        return False
    
    return getTag(tag_data)

# Detect the encoding and decode
def decodeData(bin_seq):
    # print(bin_seq)
    result = chardet.detect(bin_seq)
    # print(result)
    if(result['confidence'] > 0):
        try:
            return bin_seq.decode(result['encoding'])
        except UnicodeDecodeError:
            return 'Decode Failed'


# Get ID3v1 tag data
def getTag(tag_data):
    # STRIP_CHARS = compat.b(string.whitespace) + b"\x00"
    STRIP_CHARS = b"\x00"

    tags = {}
    tags['title'] = tag_data[3:33].strip(STRIP_CHARS)

    if(tags['title']):
        tags['title'] = decodeData(tags['title'])

    tags['artist'] = tag_data[33:63].strip(STRIP_CHARS)
    if(tags['artist']):
        tags['artist'] = decodeData(tags['artist'])

    tags['album'] = tag_data[63:93].strip(STRIP_CHARS)
    if(tags['album']):
        tags['album'] = decodeData(tags['album'])

    tags['year'] = tag_data[93:97].strip(STRIP_CHARS)
    # if(tags['year']):
    #     tags['year'] = decodeData(tags['year'])

    tags['comment'] = tag_data[97:127].strip(STRIP_CHARS)
    #@TODO Need to analyze comment to verfiy v1 or v1.1
    if(tags['comment']):
        tags['comment'] = decodeData(tags['comment'])

    tags['genre'] = ord(tag_data[127:128])

    return tags

# Set ID3v1 tag data
def setTag():
    pass