# **Someone steal my flag again**

![](https://i.imgur.com/uvQfPCg.png)

First, we see the a .pcap similar to **Someone steal my flag**.

So, we quickly filter to remain ICMP packets.

![](https://i.imgur.com/JUgQdcr.png)

After research, there's secret sequence number and data comming behind.

Then we XOR they two, we got some message.

So we quickly write down a script to automatically compute this out for us.

```python
#!/usr/bin/env python3
import codecs

pcapIcmpSecretOutput = 'pcapIcmpExtract.txt'

def pcapDecoder(file):
    buffer = []
    key = []
    flag = ''
    f = open(file,'r')
    for line in f:
        if '0020  ' in line:
            key = [line.split(' ')[10],line.split(' ')[11]]
            buffer = [line.split(' ')[12],line.split(' ')[13],line.split(' ')[14],line.split(' ')[15],line.split(' ')[16],line.split(' ')[17]]
            print(key)
            
        elif '0030  ' in line:
            buffer.append(line.split(' ')[2])
            buffer.append(line.split(' ')[3])
            print(buffer)
            for i in range(0,len(buffer),2):
                tmp1 = hex(int(buffer[i],16) ^ int(key[0],16))
                tmp2 = hex(int(buffer[i+1],16) ^ int(key[1],16))
                print(tmp1,tmp2)
                strTmp1=str(tmp1)    
                strTmp2=str(tmp2)
                print(strTmp1,strTmp2)
                strTmp1=strTmp1.replace('0x','')
                strTmp2=strTmp2.replace('0x','')
                flag = flag + strTmp1 + strTmp2
                print(strTmp1,strTmp2)
            
    print(flag)
    print(codecs.decode(flag,'hex'))

if __name__ == '__main__':
	pcapDecoder(pcapIcmpSecretOutput)
```

`This is super confidential! FLAG-4338J10B01I7Bzo6LT1ROhyLEX`