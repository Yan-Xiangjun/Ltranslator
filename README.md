# Ltranslator

#### 介绍
完全基于大模型的跨平台文献翻译工具，知云Xtranslator的开源平替

#### 软件架构
使用Python中的openai库调用大语言模型
使用pyside2库搭建用户界面
使用pynput库监听快捷键是否被按下
使用pyperclip库读取剪贴板内容
使用pyyaml库读取配置文件


#### 安装教程

1.  安装[Python](https://www.python.org/)
2.  `pip install openai pyside2 pynput pyperclip pyyaml`
3.  进入项目所在文件夹内
4.  `python main.py`

#### 使用说明

1.  可以通过编辑config.yaml来更改“学科”下拉列表中的选项以及“配置”选项卡中的模型厂商、api_key、模型名称、url等
2.  侧边按钮
    |名称|作用|
    |-|-|
    |开/关|按下后，打开翻译功能|
    |置顶|按下后，Ltranslator窗口会始终保持在所有窗口的最上方|
    |滚动|按下后，当有新的译文生成时，译文浏览框会自动滚动到最下方|
    |摘要|按下后，在翻译的同时还会自动生成摘要|
    |发送|将待翻译的原文发送给大模型，开始翻译|
    |追加|将剪贴板中的文本追加到待翻译的原文中|
    |清空|清空原文文本框|
3.  快捷键：选中文本后，按“Ctrl+X”立即启动翻译，按“Ctrl+Z”将选中的文本追加到待翻译的原文中
3.  调用本地大模型：使用[llama.cpp](https://github.com/ggerganov/llama.cpp)或[vllm](https://github.com/vllm-project/vllm)等工具启动一个OpenAI-compatible server，再修改config.yaml中“本地”选项的内容即可





