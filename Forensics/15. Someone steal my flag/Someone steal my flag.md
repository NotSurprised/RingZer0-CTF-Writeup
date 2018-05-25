# **Someone steal my flag!**

![](https://i.imgur.com/rk05CGi.png)

![](https://i.imgur.com/67cU9Ha.png)

![](https://i.imgur.com/VJrf6bN.png)

```python
#!/usr/bin/env python3
import base64
import codecs

pcapIcmpSecretOutput = 'icmpOutput.txt'

def pcapDecoder(file):
    hexBuffer = ''
    f = open(file,'r')
    for line in f:
        if 'Name:' in line:
            hexTmp = line.strip().split(' ')[1].split('.')[0]
            print('hexTmp='+hexTmp)
            hexBuffer += hexTmp
            print("--------------------------------")
    hexStr = codecs.decode(hexBuffer,'hex')
    flag = base64.b64decode(hexStr)
    print(flag)

if __name__ == '__main__':
	pcapDecoder(pcapIcmpSecretOutput)
```

![](https://i.imgur.com/3sU2ZCp.png)

```python
#!/usr/bin/env python3
import base64
import codecs

pcapIcmpSecretOutput = 'icmpOutput.txt'

def pcapDecoder(file):
    hexBuffer = ''
    checkDouble = ''
    f = open(file,'r')
    for line in f:
        if 'Name:' in line:
            hexTmp = line.strip().split(' ')[1].split('.')[0]
            print('hexTmp='+hexTmp)
            if hexTmp != checkDouble: 
                print('checkDouble='+checkDouble)
                checkDouble = hexTmp
                hexBuffer += hexTmp
                print("--------------------------------")
    hexStr = codecs.decode(hexBuffer,'hex')
    flag = base64.b64decode(hexStr)
    print(flag)

if __name__ == '__main__':
	pcapDecoder(pcapIcmpSecretOutput)
```

![](https://i.imgur.com/bmccmMT.png)
