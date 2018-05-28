# **Encrypted ZIP**

![](https://i.imgur.com/vvyPH6l.png)

Hint said it got weird.zip which encrypt compress from weird.txt, and flag.zip use the same encrypt key.

![](https://i.imgur.com/FdoqsmA.png)

![#f03c15 12356](https://placehold.it/15/f03c15/000000?text=+)

First, we got a compress file. Uncompress it.
```shell=
chmod 777 65a4fae4a9c5fd8cf9e4a5a5a295ade9.zip 
unzip 65a4fae4a9c5fd8cf9e4a5a5a295ade9.zip 
```

![](https://i.imgur.com/03OQKhE.png)

After some Google search, you'll got some information of a paper with a tool which can deal this situation well: **pkcrack**.

```shell=
sudo su
wget https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack/pkcrack-1.2.2.tar.gz
tar xzf pkcrack-1.2.2.tar.gz
cd pkcrack-1.2.2/src
make

mkdir -p ../../bin
cp extract findkey makekey pkcrack zipdecrypt ../../bin
cd ../../
```

To make pkcrack work properly, it needs three files to fill four arguments' requirements:
things:
- encrypted file you want to crack
- clear text of something encrypted with the same password
- encrypted version of that clear text

Arguments:
* -C encrypted zip name (in this case wierd.zip)
* -c file in encrypted zip (the weird.txt in weird.zip)
* -P encrypted zip that we have a clear text of (wierd.txt found in the file)
* -p file in encrypted zip that we have a cleartext version of (clear.zip)

![](https://i.imgur.com/syFBWMn.png)

```shell=
zip w.zip weird.txt 
```

![](https://i.imgur.com/kAAKcXu.png)

```shell=
pkcrack -C weird.zip -c weird.txt -P w.zip -p weird.txt
```

![](https://i.imgur.com/mNGYgLX.png)

However, it still crash.

I guess the question is that this challenge use **zip 2.0.1** to compress with encrypt key.

But I can't found the old version to make the same compression(without key).

So, I surrender & search the WriteUP.

The encrypt key is `testtest`.