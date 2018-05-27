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
