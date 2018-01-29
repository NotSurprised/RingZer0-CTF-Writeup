# **AIS3 pre-exam Misc 2**

![](https://i.imgur.com/JA0pjHG.png)
```
#!/bin/bash
for((i=0;i<=1000;i++))
    do
        pack=$(sed -i '1s/^7Z/7z/g' CTFMisc/7z/*)
        echo $pack
        ps=$(cat CTFMisc/ps/*.txt)
        echo $ps
        unpackit=$(7za x CTFMisc/7z/* -oCTFMisc/temp -p)
        echo $unpackit
        rm CTFMisc/ps/*
        mv CTFMisc/temp/*.txt CTFMisc/ps/
        rm CTFMisc/7z/*
        mv CTFMisc/temp/* CTFMisc/7z/
    done
```

如果出現 `Syntax error: Bad for loop variable`
輸入 `sudo dpkg-reconfigure dash`
選擇 No 把 dash 關掉再試試看，
也許是 dash 的問題。

![](https://i.imgur.com/9qQnEG9.png)
