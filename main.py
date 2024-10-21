from Ltranslator import *
from utils import *
import pyperclip as clipboard
from threading import Thread
from threading import Lock
import yaml
from time import time
import os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
for root, dirs, files in os.walk(dirname):
    if 'platforms' in dirs:
        plugin_path = os.path.join(root, 'platforms')
        break
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
lock = Lock()
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.full_load(f)


class Form(QMainWindow):
    signal = Signal(tuple)

    def __init__(self):
        super().__init__()
        # 加载ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.signal.connect(lambda x: x[0](*x[1:]) if len(x) > 1 else x[0]())

        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.text_subject.addItems(config[list(config.keys())[0]])
        self.ui.text_config.addItems(list(config.keys())[1:])
        self.ui.statusbar.showMessage('<token消耗> 输入 0 输出 0 <推理速度> ? tokens/s')
        self.ui.text_summary.setVisible(False)
        self.change_config()
        self.last_content = ''
        self.can_remove = True

        def on_press(key):
            if not self.ui.bu_switch.isChecked():
                return
            try:
                if key == keyboard.Key.esc:
                    copy_to_clipboard()
                    self.signal.emit((self.append_text,))
                elif key == keyboard.Key.caps_lock:
                    copy_to_clipboard()
                    content = clipboard.paste()
                    content = process_new_line(content)
                    self.signal.emit((self.ui.text_content.setPlainText, content))
                    self.signal.emit((self.send,))
            except AttributeError:
                pass

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()

    def send(self):
        content = self.ui.text_content.toPlainText().strip()
        if content == '' or content == self.last_content:
            return
        self.last_content = content
        title = self.ui.text_title.text()
        subject = self.ui.text_subject.currentText()
        summary = self.ui.bu_summary.isChecked()
        url = self.ui.text_url.text()
        key = self.ui.text_key.text()
        model = self.ui.text_model.text()
        prompt = prompt_template.format(
            title=f'\n这是一篇题为{title}的学术论文。' if title != '' else '',
            subject=f'\n这篇论文所属学科为{subject}，请使用论文所属学科的专业词汇。' if subject != '' else '',
        )
        self.ui.text_translation.setPlainText('')
        self.ui.text_summary.setPlainText('')
        self.fold_ui()

        def do_translate(control: QTextBrowser, query: str):
            ret = llm(url, key, model, prompt, query)
            time0 = time()
            for chunk in ret:
                # print(chunk)
                try:
                    if len(chunk.choices) > 0:
                        response = chunk.choices[0].delta.content
                        if response is not None:
                            self.signal.emit((control.insertPlainText, response))
                        if self.ui.bu_scroll.isChecked():
                            self.signal.emit((control.moveCursor, QTextCursor.End))

                    if chunk.usage is not None and chunk.usage.completion_tokens != 0:
                        with lock:
                            status = self.ui.statusbar.currentMessage().split(' ')
                            status[2] = str(int(status[2]) + int(chunk.usage.prompt_tokens))
                            status[4] = str(int(status[4]) + int(chunk.usage.completion_tokens))
                            # print(time() - time0)
                            status[6] = f'{int(chunk.usage.completion_tokens) / (time() - time0):.2f}'
                            self.signal.emit((self.ui.statusbar.showMessage, ' '.join(status)))
                except Exception as e:
                    self.signal.emit((control.setPlainText, str(e)))
                    break

        if len(content.split(' ')) == 1:
            Thread(target=do_translate,
                   args=(self.ui.text_translation,
                         f'请直接写出这个词的音标和中文释义：{content}，回复格式如下：/此处填入音标/ - [ 此处填入中文释义 ]\n例如：/ˈsaɪəns/ - [ 科学 ]')).start()
            return
        Thread(target=do_translate, args=(self.ui.text_translation, f'请将论文中的这些文字翻译成中文：{content}')).start()
        if summary:
            Thread(target=do_translate,
                   args=(self.ui.text_summary, f'请用中文简要概括论文中这些文字的内容：\n{content}\n注意，你的概括应简明扼要，准确反映主旨，字数不要超过150字。')).start()
        self.can_remove = True

    def change_summary(self):
        self.ui.text_summary.setVisible(self.ui.bu_summary.isChecked())
        if not self.ui.bu_summary.isChecked():
            self.ui.text_summary.setPlainText('')

    def change_top(self):
        self.hide()
        self.setWindowFlags(Qt.WindowStaysOnTopHint if self.ui.bu_top.isChecked() else Qt.Widget)
        self.show()

    def change_config(self):
        self.ui.text_url.setText(config[self.ui.text_config.currentText()]['url'])
        self.ui.text_model.setText(config[self.ui.text_config.currentText()]['model'])
        self.ui.text_key.setText(config[self.ui.text_config.currentText()]['key'])

    def fold_ui(self):
        self.ui.bu_fold.setText('﹀')
        self.ui.label_title.setVisible(bool(self.ui.text_title.text()))
        self.ui.text_title.setVisible(bool(self.ui.text_title.text()))
        self.ui.label_subject.setVisible(bool(self.ui.text_subject.currentText()))
        self.ui.text_subject.setVisible(bool(self.ui.text_subject.currentText()))

    def change_fold(self):
        if self.ui.bu_fold.text() == '︿':
            self.fold_ui()
        else:
            self.ui.bu_fold.setText('︿')
            self.ui.label_title.setVisible(True)
            self.ui.text_title.setVisible(True)
            self.ui.label_subject.setVisible(True)
            self.ui.text_subject.setVisible(True)

    def append_text(self):
        if self.can_remove:
            self.ui.text_content.setPlainText('')
            self.can_remove = False
        content = clipboard.paste()
        content = process_new_line(content)
        content0 = self.ui.text_content.toPlainText()
        self.ui.text_content.setPlainText(content if content0 == '' else content0 + ' ' + content)
        self.ui.text_content.moveCursor(QTextCursor.End)


if __name__ == '__main__':
    app = QApplication()
    app.setStyle(QStyleFactory.create('Fusion'))
    form = Form()
    form.setWindowFlags(Qt.WindowStaysOnTopHint)
    form.show()
    app.exec_()
