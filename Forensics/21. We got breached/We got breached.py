def findFlag(pcap):
    flag = [20 for i in range(37)]
    f = open(pcap,'r')
    for line in f:
        if not 'User id:1' in line or not 'flag AS' in line:
            continue
        p = line.strip().split(' ')
        if not p[-2:-1][0] == 'was':
            continue
        last = p[-3:][0]
        print(last)
        last, c = last.split('>')
        print(last)
        print(c)
        c, n = int(c), int(last.split(',')[2]) - 1
        print(c)
        print(n)
        if p[-2:-1][0] == 'was' and flag[n] < c:
            flag[n] = c
    print (''.join(chr(c + 1) for c in flag))

if __name__ == '__main__':
	findFlag('SQLmapPCAP.txt')
