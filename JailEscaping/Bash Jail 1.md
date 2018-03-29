# **Bash Jail 1**

![](https://i.imgur.com/hBRN91L.png)

```
ubuntu@ubuntu-virtual-machine:~$ ssh level1@challenges.ringzer0team.com -p 10218 
The authenticity of host '[challenges.ringzer0team.com]:10218 ([78.109.87.50]:10218)' can't be established.
ECDSA key fingerprint is SHA256:gJjkCupg596odLvqiT3qRhgElHttbotOA6m3sn3BDEY.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[challenges.ringzer0team.com]:10218,[78.109.87.50]:10218' (ECDSA) to the list of known hosts.
level1@challenges.ringzer0team.com's password: 

RingZer0 Team Online CTF

BASH Jail Level 1:
Current user is uid=1000(level1) gid=1000(level1) groups=1000(level1)

Flag is located at /home/level1/flag.txt

Challenge bash code:
-----------------------------

while :
do
	echo "Your input:"
	read input
	output=`$input`
done 

-----------------------------
Your input:
```

```
Your input:
ls
Your input:
cat flag.txt
Your input:
```

No feedback(still in process), let's execute bash to try to get some feedback.

```
Your input:
/bin/bash
level1@lxc17-bash-jail:~$ 
```

We now get rid of process, let's use bash to cat the flag.

```
level1@lxc17-bash-jail:~$ ls 1>&2
flag.txt  prompt.sh
level1@lxc17-bash-jail:~$ cat flag.txt 1>&2
FLAG-XXXXXX
```

`1>&2` means redirect stdout to stderr, it outputs the message to stderr.

