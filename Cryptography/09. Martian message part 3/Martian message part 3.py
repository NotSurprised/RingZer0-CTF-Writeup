import base64

Xorflag = base64.b64decode('RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS')
flag=''

for i in Xorflag:
	flag = flag + chr(ord(i) ^ 3)
    
print(flag)