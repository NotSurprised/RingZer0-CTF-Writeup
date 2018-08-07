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
So obviously I have to write some C code to read the content of /home/level1/flag.txt. fopen/fread are not allowed so let's do it using open/read:
```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

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
Keep in mind that you'll have to paste only the contents of main():
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
