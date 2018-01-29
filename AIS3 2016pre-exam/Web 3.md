# **AIS3 pre-exam Web 3**
![](https://i.imgur.com/0wt3Olr.png)
![](https://i.imgur.com/Ql7xpe2.png)
![](https://i.imgur.com/LlV9BvF.png)
![](https://i.imgur.com/X1x1pAE.png)
![](https://i.imgur.com/aKLfowH.png)
使用../檔案可以向上推一層取得其他目錄中的php，依序是`index`、`download`、`waf`、`you_should_not_pass`
依據`waf.php`可以嚴重懷疑flag為名的txt、php檔案格式，
理解code內容後會發現`download.php`使用GET參數的方式取得p值，
而`waf.php`則使用`parse_url`來取得query欄位的內容，所以如何避開query而讓GET取得值即為重點。
根據[https://bugs.php.net/bug.php?id=55511](https://bugs.php.net/bug.php?id=55511)所示範的巫術，
可以得知只要在`query`欄位裡增加某個值等於`/1:2`，就能讓整個`parse_url`失效。所以在url後面補上`/1:2`即可。
![](https://i.imgur.com/aWqA1ts.png)