# **Someone steal my flag**

![](https://i.imgur.com/rk05CGi.png)

There's some packet show that their **Destination unreachable**.

The **Destination Name** got some secret data before it.

![](https://i.imgur.com/67cU9Ha.png)

![](https://i.imgur.com/VJrf6bN.png)

Let's extract this out to make it more eazier to implement a script to compute the **Flag**.

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

It seems the packet are double, let's drop the same one and compute again.

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

Here's we are.
