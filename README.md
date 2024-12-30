# Ltranslator

#### 介绍
现有的文献翻译软件包括两类，一类是将翻译器与PDF阅读器捆绑在一起，必须在指定的PDF阅读器中打开文件才能进行翻译，如[小绿鲸](https://www.xljsci.com/)和[知云文献翻译](https://www.zhiyunwenxian.cn/)。另一类是将翻译器与PDF阅读器分离，用户可以在任何软件中选中文本、启动翻译，其适用范围更广，如知云团队开发的[Xtranslator](https://www.zhiyunwenxian.cn/winx.html)。

文献翻译软件所使用的翻译方式也有两种，一种是调用百度、有道等传统翻译引擎进行翻译，另一种是调用大语言模型进行翻译。一般而言，后者的翻译效果要优于前者。此外，得益于大模型API的大幅度降价，从大模型厂商处自行申请API Key用于文献翻译已经是一种非常经济的做法。目前，对于能力介于GPT-3.5级别和GPT-4级别之间的大模型，每百万token的售价大约在1元左右，如果每天消耗1万token，则一年的费用也仅有3.65元，这还不包括大模型厂商提供的免费额度。

Xtranslator的Windows版虽然提供了大模型翻译功能，但截至2024-10-10，Xtranslator的最新版（2.8.0C）只支持GPT和通义千问两种大模型，此外，如果要使用大模型翻译功能，还需要向知云购买API Key，笔者尝试将自己在阿里云申请的通义千问API Key填写在Xtranslator中，结果软件出现报错，提示API Key存在错误，最终无法使用大模型翻译功能。

此外，Xtranslator使用的是非跨平台技术，Windows版和Mac版需要用不同的框架进行开发，无法做到“一次编写，处处运行”，Mac版的功能与Windows版相比存在欠缺，且至今没有推出Linux版。

Ltranslator则是一款完全基于大模型的跨平台文献翻译工具，操作方式与Xtranslator相似，但支持任何具有OpenAI-compatible API的云端大模型和本地大模型，支持Windows、Linux和Mac系统，可以成为Xtranslator的开源平替。


#### 软件架构
1. 使用Python中的`openai`库调用大语言模型
2. 使用`pyqt5`库搭建用户界面
3. 使用`pynput`库监听快捷键是否被按下
4. 使用`pyperclip`库读取剪贴板内容
5. 使用`pyyaml`库读取配置文件
6. 使用`pyinstaller`库打包应用程序


#### 安装
方法一（推荐）：从本项目Github的release页面下载zip压缩包

方法二：按照下列步骤自行生成可执行文件
1. 安装[Python](https://www.python.org/) 版本≥3.8（对于Linux系统，请确保Python中安装了pip和venv两个模块）
2. 下载本项目，在项目所在文件夹内打开终端
3. 执行命令：`python build.py [env_path]`，其中`env_path`参数为可选参数，用于指定虚拟环境`ltrans_env`的位置。如果不指定，对于Windows，则会在`C:\Users\你的用户名`文件夹下创建虚拟环境，对于mac和Linux系统，则为当前用户的`/home`目录
4. 在`./dist/main`目录下可以找到生成的可执行文件，文件名为main

#### 配置
1. 如果使用云端大模型，请在模型服务厂商处注册账号，申请API Key。启动翻译器，在“设置”选项卡中编辑配置文件，将模型厂商、api key、模型名称、url填入配置文件中，排在最前面的模型服务为软件的默认服务。点击“保存”，重启程序。配置文件中已经预先填写了以下模型服务：[智谱AI](https://open.bigmodel.cn/)、[DeepSeek](https://www.deepseek.com/)、[通义千问](https://www.aliyun.com/product/bailian)、[讯飞星火](https://xinghuo.xfyun.cn/sparkapi)、[字节豆包](https://www.volcengine.com/product/ark)、[腾讯混元](https://console.cloud.tencent.com/hunyuan/start)
2. 如果使用本地大模型，请使用[llama.cpp](https://github.com/ggerganov/llama.cpp)或[vllm](https://github.com/vllm-project/vllm)等工具启动一个OpenAI-compatible server，再修改配置文件中“本地”选项的内容即可
3. 配置文件中“学科”字段的内容与“原文”选项卡中“学科”下拉列表中的选项一一对应
4. “置顶”字段的内容决定了程序启动时界面左侧“置顶”按钮是否被按下
5. “窗口宽度”和“窗口高度”两个字段的内容决定了程序启动时窗口的默认大小
6. 配置文件遵循YAML语法，注意“:”和“-”后面要有一个空格


#### 开始使用
1. 选中一段文本，按CapsLock，此时程序会发送一次“Ctrl+C”指令，选中的内容会经剪贴板传递到Ltranslator中，并发送给大模型进行翻译，界面会自动切换到“译文”选项卡
2. 选中一段文本，按Esc，此时程序会发送一次“Ctrl+C”指令，选中的内容会经剪贴板传递到Ltranslator中，随后追加到待翻译的原文中，界面会自动切换到“原文”选项卡
3. 如果选中的是PDF中的文字，程序会自动去除其中多余的换行符
4. 配置文件中“复制后延迟（秒）”字段的内容决定了从发送“Ctrl+C”指令到程序读取剪贴板中的内容所等待的时间，默认为0.2秒。如果发现程序未能成功获取到本次选中的内容，可考虑增加这一等待时间

5. 侧边按钮
    |名称|作用|
    |-|-|
    |开/关|按下后，使快捷键生效|
    |置顶|按下后，为置顶模式，Ltranslator窗口会始终保持在所有窗口的最上方，未按下时，为浮窗模式，Ltranslator窗口可被其他窗口遮挡，但在按下快捷键时，会自动弹出至最上方，且窗口弹出的位置位于鼠标指针附近|
    |滚动|按下后，当新生成的译文超出文本浏览框时，文本浏览框的滚动条会自动滚动到最下方|
    |摘要|按下后，在翻译的同时还会自动生成摘要|
    |发送|将待翻译的原文发送给大模型，开始翻译|
    |清空|清空原文文本框|





