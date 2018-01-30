# **leaky**
![](https://i.imgur.com/xM5R478.png)
another pwn test. let's go through source code.
![](https://i.imgur.com/4fyUIFG.png)
key value is stock between two other constant value in stack.
this time bufferoverflow will not work again.
try format string attack like `%x`.
![](https://i.imgur.com/SVgnmIT.png)
attention! constant value will compile into stack by desc order.
