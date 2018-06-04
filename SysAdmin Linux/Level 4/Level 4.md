# **Level 4**

![](https://i.imgur.com/AnfjWC8.png)

```shell
sshpass -p 'VNZDDLq2x9qXCzVdABbR1HOtz' ssh morpheus@challenges.ringzer0team.com -p 10146
```

```shell
grep 'oracle' -R / 2>/dev/null
```

`2` means error messages, `2>` will redirect the error messages, `2>/dev/null` means drop the error messages.

![](https://i.imgur.com/tHP1DuX.png)

```shell
strings /backup/c074fa6ec17bb35e168366c43cf4cd19
```

![](https://i.imgur.com/GUYWqw4.png)

My `ESC` key is broken that I cannot use `vim` :(.
So I back to loacal mechine and save the RSA private key.

```shell
ssh oracle@challenges.ringzer0team,com -p 10146 -i ringzer0teamRSAkey
```

![](https://i.imgur.com/PUEGNZu.png)

I forgot to `chmod` the RSA to proper one, so it return with error message.

```shell
chmod 600 ringzer0teamRSAkey
```

![](https://i.imgur.com/2KAQMh4.png)

`RkxBRy1HSUdzMVdxNlY2U3NaOWg0YVFncEdnZGJkUAo=`

It seems base64 encode, let's find it out.

![](https://i.imgur.com/HyyGsYs.png)

```python
import base64
print(base64.b64decode('RkxBRy1HSUdzMVdxNlY2U3NaOWg0YVFncEdnZGJkUAo='))
```

Got it~
`FLAG-GIGs1Wq6V6SsZ9h4aQgpGgdbdP`
