# **Level 1**

![](https://i.imgur.com/lcLX8ZT.png)

Well, is that matrix?  XD

```shell
sshpass -p "VNZDDLq2x9qXCzVdABbR1HOtz" ssh morpheus@challenges.ringzer0team.com -p 10089
```

![](https://i.imgur.com/I3NlMfI.png)

Then you asked for password and you will enter VNZDDLq2x9qXCzVdABbR1HOtz as a password, Now we wanna search for password of trinity so simply we have:

```shell
morpheus@lxc-sysadmin:~$ grep 'trinity' -R /etc/
grep: /etc/shadow-: Permission denied
grep: /etc/mysql/debian.cnf: Permission denied
grep: /etc/gshadow-: Permission denied
grep: /etc/subgid-: Permission denied
grep: /etc/alternatives/netcat: Permission denied
grep: /etc/alternatives/rename: Permission denied
grep: /etc/alternatives/nc: Permission denied
grep: /etc/alternatives/nawk: Permission denied
grep: /etc/alternatives/rcp: Permission denied
grep: /etc/alternatives/w: Permission denied
grep: /etc/alternatives/awk: Permission denied
grep: /etc/skel: Permission denied
/etc/rc.local:/bin/sh /root/files/backup.sh -u trinity -p Flag-08grILsn3ekqhDK7cKBV6ka8B &
grep: /etc/subuid-: Permission denied
grep: /etc/group-: Permission denied
```

It seems `trinity` have used his password for running backup, so the password is hardcoded in `backup.sh` and the flag is `Flag-08grILsn3ekqhDK7cKBV6ka8B`.