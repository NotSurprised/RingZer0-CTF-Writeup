# Level 7

![](https://i.imgur.com/erhxD3u.png)

```
sshpass -p FLAG-lRGLKGh2895wIAoOvcBbgk4oL ssh neo@challenges.ringzer0team.com -p 10091
```

![](https://i.imgur.com/9OmkFYJ.png)

Let's have a look at running processes:

```
neo@lxc-sysadmin:~$ ps fl -u neo
F   UID   PID  PPID PRI  NI    VSZ   RSS WCHAN  STAT TTY        TIME COMMAND
5  1004 16211 16187  35  15  90492  3224 -      SN   ?          0:00 sshd: neo@pts/4
0  1004 16212 16211  35  15  21192  3608 wait   SNs  pts/4      0:00  \_ -bash
0  1004 16305 16212  35  15  37336  2912 -      RN+  pts/4      0:00      \_ ps fl -u neo
4  1004 14212 14209  35  15   4216   612 hrtime SNs  ?          0:00 /bin/monitor
4  1004   186   175  35  15   4216   612 hrtime SNs  ?          0:00 /bin/monitor

```

Since we can read /bin/monitor as user `neo`, we should be able to trace its syscalls:

```
neo@lxc-sysadmin:~$ strace -p186
strace: Process 186 attached
restart_syscall(<... resuming interrupted nanosleep ...>) = 0
write(-1, "telnet 127.0.0.1 23\n", 20)  = -1 EBADF (Bad file descriptor)
write(-1, "user\n", 5)                  = -1 EBADF (Bad file descriptor)
write(-1, "FLAG-XXXXXXXXXXXXXXXXXXXXXX\n", 31) = -1 EBADF (Bad file descriptor)
write(-1, "get-cpuinfo\n", 12)          = -1 EBADF (Bad file descriptor)
nanosleep({10, 0}, 0x7fffffffec10)      = 0^Z
[1]+  Stopped                 strace -p186
neo@lxc-sysadmin:~$ strace -p14212
strace: Process 14212 attached
restart_syscall(<... resuming interrupted nanosleep ...>) = 0
write(-1, "telnet 127.0.0.1 23\n", 20)  = -1 EBADF (Bad file descriptor)
write(-1, "user\n", 5)                  = -1 EBADF (Bad file descriptor)
write(-1, "FLAG-XXXXXXXXXXXXXXXXXXXXXX\n", 31) = -1 EBADF (Bad file descriptor)
write(-1, "get-cpuinfo\n", 12)          = -1 EBADF (Bad file descriptor)
nanosleep({10, 0},
```

Got it, the flag is FLAG-XXXXXXXXXXXXXXXXXXXXXX.