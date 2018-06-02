# **Level 2**

![](https://i.imgur.com/kRmoqUD.png)

Seems the level number went wrong this time? whatever, that's not a big deal for us to get into this challenge.

```shell
sshpass -p 'VNZDDLq2x9qXCzVdABbR1HOtz' ssh morpheus@challenges.ringzer0team.com -p 10148
```

```shell
grep 'architect' -R / 2>/dev/null | head -n 10
```

`2` means error messages, `2>` will redirect the error messages, `2>/dev/null` means drop the error messages.

`| head -n 10` is a filter to remain 10 results from header.

```shell
/etc/fstab:#//TheMAtrix/phone  /media/Matrix  cifs  username=architect,password=$(base64 -d "RkxBRy14QXFXMnlKZzd4UERCV3VlVGdqd05jMW5WWQo="),iocharset=utf8,sec=ntlm  0  0
/etc/group:challenger:x:1000:morpheus,trinity,architect,oracle,neo,cypher
/etc/group:architect:x:1003:
```

Here we got `username=architect,password=$(base64 -d "RkxBRy14QXFXMnlKZzd4UERCV3VlVGdqd05jMW5WWQo=")`.

Let's decode it.

```shell
echo 'RkxBRy14QXFXMnlKZzd4UERCV3VlVGdqd05jMW5WWQo=' | base64 -d
```

![](https://i.imgur.com/HFS0cUM.png)

`FLAG-xAqW2yJg7xPDBWueTgjwNc1nVY`
