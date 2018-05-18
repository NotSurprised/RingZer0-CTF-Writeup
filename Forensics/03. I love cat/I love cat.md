# **I love cat**
`ssh cat@ringzer0team.com -p 1000`
Password: cat
-A,--show-all = -vET
```
cat@sploit:~$ cat -A flag.txt
FLAG-0K14eDrm4t5g7KD54X8Dl3NNcZ956oCK^M**************************** WHERE IS THE FLAG ? ************************************$
cat@sploit:~$
```

Another method is trying to load flag.txt as a function:
```
cat@sploit:~$ . flag.txt 
-rbash: $'FLAG-0K14eDrm4t5g7KD54X8Dl3NNcZ956oCK\r****************************':
command not found
cat@sploit:~$ 
```

**FLAG-0K14eDrm4t5g7KD54X8Dl3NNcZ956oCK**