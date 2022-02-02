# 译排

一个为翻译领域的工作人员/学生设计的排版小工具。也是”有「译」有得“系列的第一款软件。

## 快速入门

下面简单介绍软件处理文件的流程，这可以帮助你理解本软件的使用方法，也可以帮助你自定义一些选项。

1. 读取待处理的文件夹内的所有docx格式的文件，将里面的所有文字写入`.YiPai\.process\`下的一个同名的md格式的文件内，这一步会丢失源文件的所有排版，包括字体、字号、缩进
2. 对`.YiPai\.process\`内的所有md后缀名进行格式化处理（包括删除西文空格，替换全半角数字等操作）
3. 以上一步生成的文件为基础，生成指定排版要求的docx，如果有需要，还会生成一个PDF文件
4. 将上一步生成的docx和pdf移到指定的文件夹

如果你是一名开发者，更详细的技术细节请阅读`DEVELOPMENT_GUIDE.md`

##  注意事项

1. 软件包含2个部分，分别是 `.exe`后缀名的文件和`.YiPai`文件夹，请不要删除`.YiPai`文件夹，也不要通过`右键-属性`来隐藏这个文件夹————这两种方式都会导致软件无法初始化
2. 目前软件会一次性处理同文件夹下的**所有**Docx、md后缀名的文件，运行前请确认文件数量，防止电脑卡顿
3. 生成的docx会直接**覆盖旧**文件，重要文件请做好备份
4. 运行前请检查待处理文件是否被其他软件打开
5. 请确保安装有Microsoft Word，只安装了WPS Word 的用户请自行下载安装
6. 请不要在Windows 文件管理器的`下载`文件夹内运行该软件，有关这个bug的技术细节讨论，可以在这个Issue[软件无法生成docx文件](https://github.com/NoHeartPen/YiPai/issues/1)处查看

## 特性 

- 以段为单位进行完美的双列排版，满足日常基本需要
- 灵活多样的替换功能: 
    - 自动替换OCR的多余换行符
    - 自动替换西文空格
    - 自动替换《天声人语》的标记
    - 自动替换全角数字为半角
    - ……
- 默认分发绿色版的zip，开箱即用，不向C盘写入任何数据
- ~~简洁美观的设计~~🤣，适配Windows10的 Microsoft's Sun Valley 视觉风格
……

# 待办

功能、UI下条目的顺序可以理解为之后将会新增的功能顺序，会结合反馈进行调整。如果你有建议欢迎提交[Issue](https://github.com/NoHeartPen/YiPai/issues)，也可以直接发送邮件到NoHeartPen@outlook.com

## 功能

- 支持自定义字体，字号，缩进
    - 支持以中文排版的常用单位进行自定义，比如“小五”、“2字符”
- 支持保存自定义配置
- 打印CMD控制台的信息，便于报告Bug
- 支持只导出需要的文件，不需要的文件直接删除
- 支持处理其他文件夹的文件
- 支持处理单个文件
- 执行完毕后以指定的软件打开，默认以MS Office 打开Word
    - 支持自定义软件打开，需要自己填入软件的安装路径
- 支持保存源文件中的图片
- 快捷键运行
- 多平台支持（虽然 Python 是一门解释型语言，但编写时没有注意不同平台路径的`/`和 `\`的问题，还使用了大量`win32`的API，对于跨平台的支持会比较糟糕，此外，由于时间有限，这条 Todo 可能只是给有想法的同学一个提醒，更多具体的技术细节请阅读`DEVELOPMENT_GUIDE.md`）
    - Linux 测试 
        - 计划: 一个月内会在Windows平台上的 Virtual Box 6.1上使用 Debian 测试除了打印为PDF的其他功能，其他发行版本的话请自行测试
        - Termux虽然支持在Android上模拟Linux环境，但是要想读取Android系统的内的文件估计比较麻烦，欢迎有能力有兴趣的同学替大家踩雷
    - Mac 测试 （由于我没有Mac设备，有条件、有需要的同学请自行测试。注意本App基于Python3进行开发，Mac 自带的Python 2.7 版本需要修改部分语法，也可以选择另外安装Python 3.X）
- 源文件支持HTML格式的离线网页，即提取其中的文字部分
    - 优先适配日本的新闻网站
        - Yooho首页的新闻
        - 青空文库 （默认采用的Shift_JS编码）
        - 维基百科 词条
        - ……
    - 优先适配的微信公众号文章网页 
        - 联普日语社区
        - CATTI与考研
        - ……
    - 删除假名注音的`<ruby></ruby>`的HTML语法标记，便于直接复制查词
- 将处理的文章的文本上传到[チュウ太の道具箱](https://chuta.cegloc.tsukuba.ac.jp/tools.html)获取文章的词汇难度
- 以句为单位，切分排版
- 同时调用各大厂商（百度、搜狗、Google）的机器翻译API翻译文章，并将翻译结果单独编为一列，便于进行比较
- 调用百度OCR的接口，将文档内的图片转为文字
……

## UI

- 提供按钮的交互反馈
- 优化启动速度
- 优化软件安装包大小
- 制作软件图标
- 新增暗黑模式
- 自动切换暗黑/明亮模式
- 多语言界面支持
……

# 贡献

欢迎提出建议、提交Bug、交流语言学习的看法……

如果有兴趣翻译这款软件，可以直接通过邮件与我联系，我会负责大部分的技术细节。

# 版权和鸣谢

感谢我的室友LHY，没有他的鼓励与建议，就不会有这个项目。也感谢一直以来包容、支持我的亲人、朋友、同学、老师……遇见你们真好。：）

版权所有 (c) 2022 [NoHeartPen](https://github.com/NoHeartPen) 和其他贡献者。保留所有权利。

使用 **[MPL 2.0 许可证](https://github.com/NoHeartPen/YiPai/blob/main/LICENSE)** 进行许可。

## 使用的软件包

- [Sun-Valley-ttk-theme](https://github.com/rdbende/Sun-Valley-ttk-theme) MIT 许可证

- ……

## 开发环境

- Python 3.9 
