# **col**

![](https://i.imgur.com/Fxj22YL.png)

```
ssh col@pwnable.kr -p2222 (pw:guest)
```

It's the same to fd, just ssh the server, then you'll see the `col.c` coded like below.

```
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
    int* ip = (int*)p;
    int i;
    int res=0;
    for(i=0; i<5; i++){
        res += ip[i];
    }
    return res;
}

int main(int argc, char* argv[]){
    if(argc<2){
        printf("usage : %s [passcode]\n", argv[0]);
        return 0;
    }
    if(strlen(argv[1]) != 20){
        printf("passcode length should be 20 bytes\n");
        return 0;
    }

    if(hashcode == check_password( argv[1] )){
        system("/bin/cat flag");
        return 0;
    }
    else
        printf("wrong passcode.\n");
    return 0;
}
```

This question means that every four `char` you input will be transformed into one `int`.

Then combined with these 20 `char`(5 `int`) must be the some to 0x21DD09EC.

So, we first use online tool(or whatever you used to) to calculate what these 5 `int` value should be.

![](https://i.imgur.com/zgSU0Lf.png)

Remaind 4, so simply plus 4 to the result for the last one `int`.

![](https://i.imgur.com/DromYgs.png)

After all, use python's `pwn` library, simply transform every `int` back to `char` to become the payload.

Copy & paste, or simply use python io to execute the process with payload, and get your result.




