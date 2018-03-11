# **Security through obscurity**

![](https://i.imgur.com/IDBtj5E.png)
![](https://i.imgur.com/xaGPu1T.png)

Check the cookies, you'll find something there.

It seems like a base64 encoded message. Decode it.

![](https://i.imgur.com/gfFMoRy.png)

I think we should change all attributes into admin like.

![](https://i.imgur.com/IoeHBX0.png)
![](https://i.imgur.com/BZwefd6.png)

First attribute is simply set to admin, we can't figure out the second one's meaning, so just assum that it is a ID or somthing else that doesn't matter.

I'd change the timestamp for careful reason, maybe it also doesn't matter to the result.

False, of course be changed to true.

![](https://i.imgur.com/ufnBbAo.png)

The last, we found that it is the MD5 encode of those four attributes before it.

![](https://i.imgur.com/cMinnZ9.png)

We simply make the same new MD5 of our new attributes.

![](https://i.imgur.com/rTS2xkT.png)

Finally, we got all attributes modified, then let's base64 encode them into one string.

![](https://i.imgur.com/cyiwDT3.png)

Set it back to cookie, then refresh it.

![](https://i.imgur.com/ZiXleEx.png)

Fin.

