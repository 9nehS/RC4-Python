#!/usr/bin/env python

"""a simple encryption script using RC4"""


def text_to_bytes(File):

    byteList = []
    f = open(File, 'rb')

    while True:
	byte = f.read(1)
	if len(byte) == 0:
	    break
	else:
	    byteList.append(ord(byte))

    f.close()
    return byteList

def bytes_to_text(ByteList, File):

    f = open(File, 'wb')

    for byte in ByteList:
	f.write(chr(byte))

    f.close()

def hex_to_bytes(File):

    byteList = []
    f = open(File)

    hexStr = f.read()
    for i in range(0, len(hexStr), 2):
	byte = hexStr[i:i+2]
	byteList.append(int('0X' + byte, 16))

    f.close()
    return byteList

def bytes_to_hex(ByteList, File):

    f = open(File, 'w')

    for byte in ByteList:
	hexStr = '0' + hex(byte)[2:]
	f.write(hexStr[-2:].upper())

    f.close()

def crypt(PlainBytes, KeyBytes):

    keyStreamList = []
    cipherList = []

    keyLen = len(KeyBytes)
    plainLen = len(PlainBytes)
    S = range(256)

    j = 0
    for i in range(256):
	j = (j + S[i] + KeyBytes[i % keyLen]) % 256
	S[i], S[j] = S[j], S[i]

    i = 0
    j = 0
    for	m in range(plainLen):
	i = (i + 1) % 256
	j = (j + S[i]) % 256
	S[i], S[j] = S[j], S[i]
	k = S[(S[i] + S[j]) % 256]
	keyStreamList.append(k)
	cipherList.append(k ^ PlainBytes[m])
	
    return keyStreamList, cipherList

def main():
    
    Plain = 'Plain.txt'
    Key = 'Key.txt'
    Cipher = 'Hex.txt'
    KeyStream = 'KeyStream.txt'

    KeyBytes = text_to_bytes(Key)

    n = input('Enter 1 to encypt, 2 to decrypt, others to quit:\n')

    if n == 1:
	PlainBytes = text_to_bytes(Plain)
	KeyStreamBytes, CipherBytes = crypt(PlainBytes, KeyBytes)
	bytes_to_hex(KeyStreamBytes, KeyStream)
	bytes_to_hex(CipherBytes, Cipher)
    elif n == 2:
	CipherBytes = hex_to_bytes(Cipher)
	KeyStreamBytes, PlainBytes = crypt(CipherBytes, KeyBytes)
	bytes_to_hex(KeyStreamBytes, KeyStream)
	bytes_to_text(PlainBytes, Plain)
    else:
	return


if __name__ == '__main__':
    main()
