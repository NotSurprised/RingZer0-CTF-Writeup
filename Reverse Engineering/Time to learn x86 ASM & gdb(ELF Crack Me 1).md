# Time to learn x86 ASM & gdb(ELF Crack Me 1)

![](https://i.imgur.com/BkSGwZI.png)

Download and change file permission.
`chmod 777 88eb31060c4abd0931878bf7d2dd8c1a`

Install x86 libary for x64 OS.
```
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386
```

Set the breakpoints on function and run it.

![](https://i.imgur.com/B1DXIU6.png)

![](https://i.imgur.com/y60ataa.png)

This code make fllag with strcmp and strcat so we can see it in stack while making it.

Here it is:
`FLAG-4092849uio2jfklsj4kl`

※Another method:

Use gdb.

```
gdb-peda$ info function
All defined functions:

Non-debugging symbols:
0x080482f4  _init
0x08048330  malloc@plt
0x08048340  puts@plt
0x08048350  __gmon_start__@plt
0x08048360  __libc_start_main@plt
0x08048370  memset@plt
0x08048380  _start
0x080483b0  deregister_tm_clones
0x080483e0  register_tm_clones
0x08048420  __do_global_dtors_aux
0x08048440  frame_dummy
0x0804846c  main
0x08048560  __libc_csu_init
0x080485d0  __libc_csu_fini
0x080485d2  __i686.get_pc_thunk.bx
0x080485d8  _fini
gdb-peda$ b main
Breakpoint 1 at 0x8048470
gdb-peda$ r
```

Set breakpoint and run.
`n` to next.

```
0x80484a5 <main+57>:	call   0x8048370 <memset@plt>
0x80484aa <main+62>:	mov    eax,DWORD PTR [esp+0x2c]
0x80484ae <main+66>:	mov    DWORD PTR [eax],0x47414c46
0x80484b4 <main+72>:	mov    DWORD PTR [eax+0x4],0x3930342d
0x80484bb <main+79>:	mov    WORD PTR [eax+0x8],0x32
0x80484c1 <main+85>:	mov    eax,DWORD PTR [esp+0x2c]
0x80484c5 <main+89>:	mov    DWORD PTR [esp+0x1c],0xffffffff
0x80484cd <main+97>:	mov    edx,eax
0x80484cf <main+99>:	mov    eax,0x0
0x80484d4 <main+104>:	mov    ecx,DWORD PTR [esp+0x1c]
0x80484d8 <main+108>:	mov    edi,edx
0x80484da <main+110>:	repnz scas al,BYTE PTR es:[edi]
0x80484da <main+110>:	repnz scas al,BYTE PTR es:[edi]
0x80484dc <main+112>:	mov    eax,ecx
0x80484de <main+114>:	not    eax
0x80484e0 <main+116>:	lea    edx,[eax-0x1]
0x80484e3 <main+119>:	mov    eax,DWORD PTR [esp+0x2c]
0x80484e7 <main+123>:	add    eax,edx
0x80484e9 <main+125>:	mov    DWORD PTR [eax],0x75393438
0x80484ef <main+131>:	mov    DWORD PTR [eax+0x4],0x6a326f69
0x80484f6 <main+138>:	mov    WORD PTR [eax+0x8],0x66
0x80484fc <main+144>:	mov    DWORD PTR [esp],0x80485f8


```
`ESP: 0xffffd060 --> 0x804b160 ("FLAG-4092849uio2jf")`

```
0x8048503 <main+151>:	call   0x8048340 <puts@plt>
```
It put strcmp() string `FLAG-4092849uio2jf` into flag.

```
0x8048536 <main+202>:	mov    DWORD PTR [eax+0x4],0x6c6b34
0x804853d <main+209>:	mov    DWORD PTR [esp],0x8048603
0x8048544 <main+216>:	call   0x8048340 <puts@plt>
```
`EAX: 0x804b172 ("klsj4kl")`
Here it declare string again and strcat() append `klsj4kl` to old one.

So the flag is:
`FLAG-4092849uio2jfklsj4kl`