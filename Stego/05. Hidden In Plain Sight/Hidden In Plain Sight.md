# **Hidden In Plain Sight**

The text is an article named [Hacker Manifesto](http://www.phrack.org/issues/7/3.html#article) by [The Mentor](https://en.wikipedia.org/wiki/Loyd_Blankenship)

hex dump of both texts and compare them.(Just like hugo challenge)

```shell=
xxd -p original.txt | fold -w 2 > original.hex
```

Cuz `xxd -p` will output continuous hex string, so let's use`fold -w 2` to make int string into `hex`.

```shell=
cat 618d0e51213fa164d93bd92ca5e099c3.txt | cut -d ' ' -f -16 | tr -d ' ' | fold -w 2 > modified.hex
```

`cut -d ' ' -f -16` means use space to seperate it and cut down 0~16 column.

`tr -d ' '` means to replace space with nothing.

```shell=
diff -y --suppress-common-lines *.hex > diff.txt
```

※Attention that `*.hex` means all `.hex` type file in current folder.

```shell=
cat diff.txt | cut -f 1 | tr '\n' ' ' > flag.txt
```

The second column maybe, just make sure that you cut down the right column from `modified.hex`.

Use python or online tool to cover back to char.

```shell=
for i in open('flag.txt').readline().split():
  print(chr(int(i, 16)), end='')
```

```
46							      |	20
4c							      |	69
41							      |	65
47							      |	69
2d							      |	20
4e							      |	2c
6f							      |	20
74							      |	20
68							      |	20
69							      |	20
6e							      |	20
67							      |	6b
49							      |	74
73							      |	68
45							      |	73
76							      |	62
65							      |	6f
72							      |	68
57							      |	79
68							      |	65
61							      |	68
74							      |	6e
49							      |	77
74							      |	65
53							      |	20
65							      |	72
65							      |	20
6d							      |	65
73							      |	0a
```

![](https://i.imgur.com/dL6oyV1.png)


