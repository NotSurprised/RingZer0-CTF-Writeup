# **fd**
First, use SSH question afford to connect to the server.
`ssh fd@pwnable.kr -p2222 (pw:guest)`

![](https://i.imgur.com/KTCmKK8.png)

Then you'll find the permission denied.

We deeply trace the source code in the folder:
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
    if(argc<2){
        printf("pass argv[1] a number\n");
        return 0;
    }
    int fd = atoi( argv[1] ) - 0x1234;
    int len = 0;
    len = read(fd, buf, 32);
    if(!strcmp("LETMEWIN\n", buf)){
        printf("good job :)\n");
        system("/bin/cat flag");
        exit(0);
    }
    printf("learn about Linux file IO\n");
    return 0;
}
```
The number argv[1] you input will minus by hex value `1234`. Then it will become `int fildes` value of `read(int fildes, void *buf, size_t nbyte);`.

If `int fildes` is set to 0, `read()` will become `stdin`.

So, we simply input a decimal value that can be minused `0x1234` to `0`.

![](https://i.imgur.com/pjMzCB5.png)

It's 4660.

![](https://i.imgur.com/nJIP0Kf.png)

After we input `4660`, `read()` will become `stdin`, so we can simply input `LETMEWIN` to make `if(!strcmp())` true.

