# **Can you see through the star**

First, we got a `.tar` file, if you extract it, you will get another compress file.

Extract out the file inside the second compress file, you will get a `.exe` file.

![](https://i.imgur.com/vdDkmSw.png)

After running the `executable` file we understand that we need to know the text of `psw-masked text box`, cause whatever the flag it generate, it all look like `************`.

To decompile the code of executable file we can simply use `Telerik Just Decompile`, download from [here](http://www.telerik.com/products/decompiler.aspx).

![](https://i.imgur.com/frVK72c.png)

With simple knowledge of `Windows Forms Application Developer Strcture` search into `form1` to get where the botton function begin.

```
private void button1_Click(object sender, EventArgs e)
{
    this.maskedTextBox1.text = string.Concat(string.Concat(String.Concat("FLAG-", this.maskedTextBox1.Name), "vc"), this.button1.Name);
}
```

Then search for InitializeComponent function that will give you names of `maskedTextBox1` and `button1`.

So after all we generate the flag:

`FLAG-maskedTextBox1vcbutton1`