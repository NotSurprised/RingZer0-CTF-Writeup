# **random**

First, SSH to the server.

![](https://i.imgur.com/TtsBHG7.png)
```
#include <stdio.h>

int main(){
    unsigned int random;
    random = rand(); // random value!

    unsigned int key=0;
    scanf("%d", &key);

    if( (key ^ random) == 0xdeadbeef ){
        printf("Good!\\n");
        system("/bin/cat flag");
        return 0;
    }

    printf("Wrong, maybe you should try 2^32 cases.\\n");
    return 0;
}
```
List it, then cat `rand.c` to see the source code.
You'll see that if `(key ^ random) == 0xdeadbeef`, it will print flag.
The random value is assigned from `rand()`, it doesn't set seed value by `srand()`, so the `rand()` value with seed (default as 1) will always be the same.

![](https://i.imgur.com/lh25F7H.png)
![](https://i.imgur.com/vPv748v.png)

Implement a code to print the `rand()` value.

![](https://i.imgur.com/lGYZ7n5.png)

Use python to quickly get the correct key value by Xor the `rand()` value and `0xdeadbeef`.

![](https://i.imgur.com/RhOWjgJ.png)

Input the correct key value to the process with ssh connection.

