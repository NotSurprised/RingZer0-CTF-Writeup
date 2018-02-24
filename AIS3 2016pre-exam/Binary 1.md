# **AIS3 pre-exam Binary 1**
![](https://i.imgur.com/p7i0Hm4.png)

先將檔案改成可執行檔，然後用EDB反組譯。在找到比較點後，不斷測試輸入，暴力破解出Key。

![](https://i.imgur.com/CP5NJev.png)
![](https://i.imgur.com/hBYTKON.png)
![](https://i.imgur.com/DJYGENY.png)
![](https://i.imgur.com/Yj7oKip.png)
![](https://i.imgur.com/5g0YrSB.png)

Boik use angr to solve the problem. Following is Boik's example exploit script:

`
import angr

proj = angr.Project('./rev')

argv1 = angr.claripy.BVS("argv1",30*8)
initial_state = proj.factory.path(args=["./rev",argv1])

path_group = proj.factory.path_group(initial_state)

path_group.explore(find=0x4006d7, avoid=0x4006cd)

solution = path_group.found[0].state.se.any_str(argv1)

solution = solution[:solution.find("\x00")]

print solution
`