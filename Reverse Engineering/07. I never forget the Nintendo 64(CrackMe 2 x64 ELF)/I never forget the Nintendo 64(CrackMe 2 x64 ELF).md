# I never forget the Nintendo 64(CrackMe 2 x64 ELF)

![](https://i.imgur.com/vERujpx.png)

First, Download the binary.

![](https://i.imgur.com/WxZwCk6.png)

Take a look at the header for file type: `.ELF`

![](https://i.imgur.com/ogfifmw.png)

Change usage permission of download file.o
`chmod 777 922cb8ea8a0ef26b7cd18388b10fd70d`

![](https://i.imgur.com/FYG088H.png)

Set breakpoint on `main()` then run it.

![](https://i.imgur.com/BADtsj0.png)

`n` for `next` line, one by
Then input something for password.

![](https://i.imgur.com/jSGBu0k.png)

Change `RAX` to `RDX` value.

`set $rax = 0x6f7499ec` to set register value.
`i r rax` to show the segister value now.

![](https://i.imgur.com/MSSEyNb.png)

![](https://i.imgur.com/IoE9KvT.png)

![](https://i.imgur.com/BZnkyrY.png)

Well, this VM lost some library maybe?
But, I'm sure it will work.

Let's get another method:

Run this .ELF in `edb`.

![](https://i.imgur.com/0Q6jEwv.png)

Toggle breakpoint on `0x004006ef`.

![](https://i.imgur.com/oqbRzkx.png)

Input something.

![](https://i.imgur.com/bk081cp.png)

Set Register `RAX` same with `RDX`.

![](https://i.imgur.com/1xQfpvY.png)

Here's we got:  FLAG-6f749f251869912556
