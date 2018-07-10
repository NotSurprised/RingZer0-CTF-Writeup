# Windows x86 Reversing is cool

![](https://i.imgur.com/qsEcuiA.png)

![](https://i.imgur.com/M05NNF4.png)
![](https://i.imgur.com/pnsmQan.png)

eax = strlen(scanf());
if(eax == 6) continue;

![](https://i.imgur.com/GMkqpyk.png)

It loop to XOR input with secret(at `0x00401430`) and compare with key after all, equal then show flag.

![](https://i.imgur.com/IjImeFj.png)

After tracing with OllyDBG, we found that string that .exe load here is suspicious.

![](https://i.imgur.com/Xl2BYKO.png)

OllyDBG will translate into ASCII, let's double click in IDApro to chase the hex value.

![](https://i.imgur.com/DitSxey.png)

Switch to `Hex View - 1` tab

![](https://i.imgur.com/YYqPw8w.png)

Here we got. Or you can search it in hex viewer follow clue from OllyDBG: `../../runtime/pseudo-reloc.c`

![](https://i.imgur.com/8pEMnry.png)

```python
import codecs
print (codecs.decode(hex(0x97E0EBA0B8E1 ^ 0xD3D3D3D3D3D3).replace('0x',''),"hex"))
```
Key: `D38sk2`

cmd.exe /k 1231fa8523f32a9118993946bccfb9ec203.exe
Key: D38sk2
FLAG-PIIXtM36MtKJ8347qh72r7C3

![](https://i.imgur.com/Htpb2Z7.png)
