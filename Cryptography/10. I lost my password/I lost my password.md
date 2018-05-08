# I lost my password

First, change mode of new download, then decompress it.
```
chmod 777 d22fdb09ef96576dfc49076a9322a555.tar 
tar xf d22fdb09ef96576dfc49076a9322a555.tar 
```

![](https://i.imgur.com/J8mNZxg.png)

![](https://i.imgur.com/WHbO39w.png)

There's a few data in it, you can simply find the password by browsing, or `grep()` it from folder:

```
grep -R -i 'password'  Policies/*
```

Then you'll get this:
![](https://i.imgur.com/cdD4SLk.png)

```
cpassword="PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw"
```

![](https://i.imgur.com/6hv6kYr.png)

By roughly browsing, we get some clue for this folder, it seems like a backup of group policy.

If you search `Windows policy Password Encryption`, you'll find this [post](https://www.grouppolicy.biz/2013/11/why-passwords-in-group-policy-preference-are-very-bad/).

From [MSDN](https://msdn.microsoft.com/en-us/library/2c15cbf0-f086-4c74-8b70-1f2fa45dd4be.aspx#endNote2), you can find the only AES-32 bits KEY to decrypt for local users' password added via Windows 2008 Group Policy Preferences.

Yap, we know this publishing make this encryption become very useless to the hacker who target on this.

Now, we give it a script to decrypt it.

I simply use AES Key to decrypt it, but failed.

Then I found [this](https://adsecurity.org/?p=63).

So, let's add base64 decoder?

```
from Crypto.Cipher import AES
from base64 import b64decode

key = "\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b"

cpassword = "PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw"
cpassword += "=" * (4 - (len(cpassword) % 4))
password = b64decode(cpassword)

flag = AES.new(key, AES.MODE_CBC, "\x00" * 16).decrypt(password)

print (flag[:-ord(flag[-1])].decode('utf16'))
```

![](https://i.imgur.com/YetmppT.png)

Fin.

## ※Script in Ruby:

```
require 'rubygems'
require 'openssl'
require 'base64'

cpassword = "PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw"

padding = "=" * (4 - (cpassword.length % 4))
cpassword = "#{cpassword}#{padding}"
password = Base64.decode64(cpassword)

key = "\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b"
aes = OpenSSL::Cipher::Cipher.new("AES-256-CBC")
aes.decrypt
aes.key = key
plaintext = aes.update(password)
plaintext << aes.final
password = plaintext.unpack('v*').pack('C*') # UNICODE conversion
puts password

```

![](https://i.imgur.com/NyaKg2I.png)
