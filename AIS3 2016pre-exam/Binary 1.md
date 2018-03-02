# **AIS3 pre-exam Binary 1**
![](https://i.imgur.com/p7i0Hm4.png)

先將檔案改成可執行檔，然後用EDB反組譯。在找到比較點後，不斷測試輸入，暴力破解出Key。

![](https://i.imgur.com/CP5NJev.png)
![](https://i.imgur.com/hBYTKON.png)
![](https://i.imgur.com/DJYGENY.png)
![](https://i.imgur.com/Yj7oKip.png)
![](https://i.imgur.com/5g0YrSB.png)

qazbnm456(Boik) use angr to solve the problem. Following is Boik's example exploit script:

```
import angr

proj = angr.Project('./rev') #set the binary path.

argv1 = angr.claripy.BVS("argv1",30*8) #BVS means "bitvector symbolic", this line means to set the input parameters call "argv1", lengh is 30*8 bits. 8 bits is for char. 30 is nobody know, sorry.

initial_state = proj.factory.path(args=["./rev",argv1]) #means to set symbolic execution's path & this will default to start from binary main()

path_group = proj.factory.path_group(initial_state) #setting all the attribute to angr.path_group, then call explore to find the path.

path_group.explore(find=0x4006d7, avoid=0x4006cd)  #find || avoid's adr must be beginning of basic block, otherwise, it will become deadend.

solution = path_group.found[0].state.se.any_str(argv1)  #"se" means to call solver engine

solution = solution[:solution.find("\x00")]

print solution
```