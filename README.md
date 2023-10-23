# convert
支持按键及文字输入编辑简谱，自动转为吹笛子的指法谱（目前支持陶笛和哨笛），该工具比较容易上手操作
做这个工具的起因是自己最近入手了一只陶笛，对笛类乐器比较感兴趣，进而又入手了一只爱尔兰哨笛。我希望能吹一些入门教程外的曲目，但自己也只是刚入门，对指法表还不熟，所以希望通过这个工具快速获得笛子的指法按位谱。
对于熟悉该乐器的人来说，这个工具用处没有那么大，但是对于入门者来说，这个可能会大幅降低学习门槛，激发一些兴趣。
开源代码和可执行exe文件都放在了upload文件夹中，可供使用。
两种打开方式：
1、点击main.exe文件
2、cmd命令行
```
cd ./upload
python main.py
```

界面如图所示：
![image](https://github.com/BaymaxCEO/convert/assets/115970307/6605f1b3-2822-4144-b3e8-4bf59689e979)

使用方法：
1、选笛型（目前支持六孔陶笛、哨笛谱生成）
2、直接点击按钮录入简谱（前面有.表示低八度，后面有.表示高八度），点击后在简谱显示框中同步显示。如果输错可以退格删除。也支持直接在简谱显示框中修改。每录入一句之后也可以换行。
注：音符之间一定要有空格，否则会报错无法提交。并且简谱中也不要单独出现.符号，否则也会出错。
3、选择升key数。默认为0，一定要在建议升key数的范围内，否则也无法提交。
4、直接点击提交。程序会生成对应的笛谱指法按位表，显示在笛谱显示框中。

之后可能会增加的功能：
1、支持更多乐器（如竹笛等）
2、支持输入不同持续时间的音符（如区分四分音符、八分音符等）
3、增加试听功能
