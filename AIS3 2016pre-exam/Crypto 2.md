# **AIS3 pre-exam Crypto 2**

![](https://i.imgur.com/dCNl18B.png)

crypto 2，官方好像是希望我們用hash extension attack，
但是從它的演算法中會發現它給我們的expire跟auth本身是一對的，
這已經可以通過第一階段認證，再來的問題就只剩他還要求expire>time(0)而已。
	
然後從它的程式碼就發現，第一階段認證使用的是字串切割取出字串前段的expire=XXXXXX來做sha1，然後用GET['auth']來取auth，最後比對expire>time(0)的部分才是真正要用GET['expire']

※而http get的參數的部分，當有重複的參數出現，會使用最後一次出現的參數當作數值。所以只要在url後面再補一次&expire=YYYYYY比原先expire=XXXXXX還大的數字即可。

![](https://i.imgur.com/nE8rmQu.png)

qazbnm456(Boik) use hashpunpy to solve the problem. Following is Boik's example exploit script:

![](https://i.imgur.com/5OEsEer.png)

```
from hashpumpy import hashpump
import requests
import urlparse
import re

for i in xrange(61)
	mac, ext = hashpump('41fe78ff2c2c51e758bf4501fd8e6a9b8d478f4e', 'expire=1467391984', '&expire=2577390020', i)

	ext = urlparse.parse_qs(ext)

	r = requests.get('https://quiz.ais3.org:8014/', params=[('expire', ext["expire"][0]), ('expire', ext["expire"][1]), ('auth', mac)])

	failed = re.search('<div id="flag">.*ais3{.*', r.content)
	if failed:
		print "{}: {}".format(i, failed.group())
		break
```