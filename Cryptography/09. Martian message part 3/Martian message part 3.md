# **Martian message part 3**

Challege just give us a string :`RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS`

So, let's try to decrypt it.

![](https://i.imgur.com/YovogMG.png)

First, we try Base64 decoding.

![](https://i.imgur.com/NmBjyz1.png)

The Output is `EOBD.7igq4;1ikb51ibOO0;:41R`.

It seens still unreadable, I google `EOBD.7igq4;1ikb51ibOO0;:41R` then get a hint that I can XOR to solve it.

`'E' ^ 'F' = 0x03`

![](https://i.imgur.com/SAWu0dZ.png)

```
import base64

Xorflag = base64.b64decode('RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS')
flag=''

for i in Xorflag:
	flag = flag + chr(ord(i) ^ 3)
    
print(flag)
```

Then I get flag.

`FLAG-4jdr782jha62jaLL38972Q`