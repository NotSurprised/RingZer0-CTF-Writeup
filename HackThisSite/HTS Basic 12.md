# **HTS Basic 12**
This mission used to be there.

Maybe due to some CopyRight, cuz it seems come out from ASIS CTF 2014.

![](https://i.imgur.com/QQjSvoc.png)

![](https://i.imgur.com/bF1a9yw.png)

First we got a unknown file `trivia_50_88da3c57a7b4489036943d35d551cab2`.

In hex view or just open with Notepad++, you can see the file type header `FD 37 7A 58 5A` or `xFD 7z`.

![](https://i.imgur.com/HXgEAp2.png)

Decompress it, and you get `trivia_50_88da3c57a7b4489036943d35d551cab2`.

There something special string `NES` in hex view.

Download Nintendo FC/NES simulator and try to open the file.

![](https://i.imgur.com/okZr8Ma.png)

Fail.

If you use Linux system, you can use file command to identify the file type of `trivia_50_88da3c57a7b4489036943d35d551cab2`,
and you will find out that it still a `.tar` compress file.

Decompress it, and you get `trivia_50_1ac1ca160ae4004cd063e0e4b73e7f2c`.

Add it in to Nintendo FC/NES simulator.

![](https://i.imgur.com/Re1mR8i.png)

Complete the level one and get to level two, you'll see.

![](https://i.imgur.com/fMxSi8P.png)

