# **HTS Application 5**
Alt+E 到達程式正在執行的區塊。
![](https://i.imgur.com/6jX0b0S.png)

由前兩個BP可得知密碼最常16位數。
![](https://i.imgur.com/bj7LnbI.png)

CMP EAX,DWORD PTR SS:[EBP+EDX*4-18]是主要比對判斷處。
![](https://i.imgur.com/TBjCCc0.png)

在view裡點選watches來設置觀察項目。
![](https://i.imgur.com/fZMREKj.png)

每次程式比對四個字元，由左至右。如當初輸入abcd的話，此處則為64 63 62 61。根據watch所觀察的標準修改EAX值。
![](https://i.imgur.com/zs7yMv7.png)

程式只會印出當時輸入的值，所以將紀錄下的比對hex值由左至右轉換回來，0A是換行，可無視。
![](https://i.imgur.com/QGegbL2.png)

Fin.
![](https://i.imgur.com/JkqPmNl.png)



