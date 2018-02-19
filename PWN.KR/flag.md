# **flag**

![](https://i.imgur.com/l0EJXos.png)

If you binwalk the file given by question, you will see the UPX in result.

![](https://i.imgur.com/PdtjNTm.png)

To deshield the file, you need to install the upx tool.

![](https://i.imgur.com/VLFx9md.png)

Then deshield the file.

![](https://i.imgur.com/WlUku0v.png)

Of course, it's still a .ELF file. Run the file then you'll see it hints that the flag was malloc() and stored in stack.
You can simply cat it or debug it with wdb to get the flag.

![](https://i.imgur.com/YQmFOBl.png)

Here it is.

