from Crypto.Cipher import AES
from base64 import b64decode

key = "\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b"

cpassword = "PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw"
cpassword += "=" * (4 - (len(cpassword) % 4))
password = b64decode(cpassword)

flag = AES.new(key, AES.MODE_CBC, "\x00" * 16).decrypt(password)

print (flag[:-ord(flag[-1])].decode('utf16'))