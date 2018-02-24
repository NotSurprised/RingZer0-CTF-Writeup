# **AIS3 pre-exam Rev 1**
![](https://i.imgur.com/gYGREt6.png)

似乎flag跟背景色混在一起了。

![](https://i.imgur.com/7NUXrzL.png)

使用IDA pro可以找到Print的function位置。

![](https://i.imgur.com/ssmF8fC.png)

追蹤function後可以他print找到一連串float數值。

![](https://i.imgur.com/Q3LII0E.png)

追進Stack可以找到完整的值。

![](https://i.imgur.com/5aOHDQy.png)

![](https://i.imgur.com/Pr6fRJq.png)

擷取後recover回hex，注意Stack堆疊會反序。

![](https://i.imgur.com/VMABlFh.png)

從hex轉回ASCII