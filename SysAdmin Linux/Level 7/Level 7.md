# Level 7

```
sshpass -p FLAG-lRGLKGh2895wIAoOvcBbgk4oL ssh neo@challenges.ringzer0team.com -p 10091
```

Let's have a look at running processes:

```
neo@forensics:~$ ps fl -u neo  
F   UID   PID  PPID PRI  NI    VSZ   RSS WCHAN  STAT TTY        TIME COMMAND
4  1003 32505 32503  20   0   3944   256 -      Ss   ?          0:01 /bin/monitor
4  1003 32073 32071  20   0   3944   256 -      Ss   ?          0:01 /bin/monitor
4  1003 31844 31842  20   0   3944   256 -      Ss   ?          0:04 /bin/monitor
4  1003 31624 31622  20   0   3944   256 -      Ss   ?          0:03 /bin/monitor
4  1003 31471 31469  20   0   3944   256 -      Ss   ?          0:02 /bin/monitor
4  1003 31078 31076  20   0   3944   256 -      Ss   ?          0:02 /bin/monitor
4  1003 30040 30038  20   0   3944   256 -      Ss   ?          0:02 /bin/monitor
......
```

Since we can read /bin/monitor as user neo (and /bin/monitor was started using sudo neo -c /bin/monitor) we should be able to trace its syscalls (since we are allowed to attach to a process running as user neo):

```
neo@forensics:~$ strace -p32505
Process 32505 attached - interrupt to quit
restart_syscall(<... resuming interrupted call ...>) = 0
write(4294967295, "telnet 127.0.0.1 23\n", 20) = -1 EBADF (Bad file descriptor)
write(4294967295, "user\n", 5)          = -1 EBADF (Bad file descriptor)
write(4294967295, "FLAG-a4UVY5HJQO5ddLc5wtBps48A3\n", 31) = -1 EBADF (Bad file descriptor)
write(4294967295, "get-cpuinfo\n", 12)  = -1 EBADF (Bad file descriptor)
rt_sigprocmask(SIG_BLOCK, [CHLD], [], 8) = 0
rt_sigaction(SIGCHLD, NULL, {SIG_DFL, [], 0}, 8) = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
nanosleep({10, 0},
```

Bingo! The flag is FLAG-a4UVY5HJQO5ddLc5wtBps48A3.
