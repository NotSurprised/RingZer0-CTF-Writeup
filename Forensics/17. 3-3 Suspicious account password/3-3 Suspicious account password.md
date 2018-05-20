# **Suspicious account password?**

First, unzip the file:

```shell
$ uz 5bd2510a83e82d271b7bf7fa4e0970d2.zip 
$ file 5bd2510a83e82d271b7bf7fa4e0970d1 
5bd2510a83e82d271b7bf7fa4e0970d1: data
$ exiftool 5bd2510a83e82d271b7bf7fa4e0970d1 
Error                           : Unknown file type
$ binwalk 5bd2510a83e82d271b7bf7fa4e0970d1 
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
454872        0x6F0D8         Unix path: /www.w3.org/2000/09/xmldsig#sha1"/><DigestValue>3xJjgZc3uS+skhnnwMKXTAz4JHI=</DigestValue></Reference></SignedInfo><SignatureVal
483328        0x76000         Microsoft executable, portable (PE)
1249280       0x131000        Microsoft executable, portable (PE)
1897587       0x1CF473        mcrypt 2.2 encrypted data, algorithm: blowfish-448, mode: CBC, keymode: 8bit
1950830       0x1DC46E        Unix path: /www.microsoft.com/SoftwareDistribution/Server/UpdateRegulationWebService
2101736       0x2011E8        Certificate in DER format (x509 v3), header length: 4, sequence length: 572
```

After we file it, we know that it's probably  a Windows Memory Dump file.

Then we need to find some tool to forensic this file.

Then, from this [post](https://www.aldeid.com/wiki/Volatility/Retrieve-password), we can learn the method to extract user's password from memory dump.

```shell
$ git clone https://github.com/volatilityfoundation/volatility.git
$ cd volatility/
$ python setup.py build
$ sudo python setup.py build install 
````

```shell
$ python vol.py imageinfo -f 5bd2510a83e82d271b7bf7fa4e0970d1
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86
```

As you see it `Suggested Profile(s)` is `Win7SP0x86`. Now we need the hivelist:

```shell
$ python vol.py --profile Win7SP0x86 hivelist -f 5bd2510a83e82d271b7bf7fa4e0970d1
Virtual    Physical   Name
---------- ---------- ----
0x879d0008 0x0c824008 \Device\HarddiskVolume1\Boot\BCD
0x87bd88d8 0x0c0958d8 \SystemRoot\System32\Config\SOFTWARE
0x93d47008 0x03bf3008 \??\C:\Users\flag\ntuser.dat
0x93d4f580 0x01970580 \??\C:\Users\flag\AppData\Local\Microsoft\Windows\UsrClass.dat
0x82090450 0x06491450 \SystemRoot\System32\Config\SAM
0x820984a0 0x06bab4a0 \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT
0x820a0558 0x05c85558 \SystemRoot\System32\Config\SECURITY
0x8210e0d0 0x063e80d0 \??\C:\Windows\ServiceProfiles\NetworkService\NTUSER.DAT
0x8780c008 0x0029b008 [no name]
0x87819938 0x00122938 \REGISTRY\MACHINE\SYSTEM
0x878419d0 0x0008c9d0 \REGISTRY\MACHINE\HARDWARE
0x878c5008 0x0b6b7008 \SystemRoot\System32\Config\DEFAULT
```

The major module is [hashdump](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference#hashdump) of volatility.

> To use hashdump, pass the virtual address of the SYSTEM hive as -y and the virtual address of the SAM hive as -s [name=VolatilityWiki]

```shell
$ python vol.py --profile Win7SP0x86 hashdump -y 0x87819938 -s 0x82090450 -f 5bd2510a83e82d271b7bf7fa4e0970d1
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
flag:1000:aad3b435b51404eeaad3b435b51404ee:3008c87294511142799dca1191e69a0f:::
```

Now, we got the NTLM Hash we need to decrypt.

[Crackstation](https://crackstation.net/) & [NTLM decryptor](https://www.hashkiller.co.uk/ntlm-decrypter.aspx) are online decrypt tool. 

```
Hash                                Type	Result
----------------------------------- ------- --------------
3008c87294511142799dca1191e69a0f	NTLM	admin123
```

Fin.