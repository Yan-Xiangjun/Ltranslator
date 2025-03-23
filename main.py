from Ltranslator import *
from utils import *
import pyperclip as clipboard
from threading import Thread
from threading import Lock
import yaml
from time import time, sleep
import os
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtGui import *

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = find_plugin_path(PyQt5)
lock = Lock()


class Form(QMainWindow):
    signal = Signal(tuple)

    def __init__(self):
        super().__init__()
        # 加载ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.signal.connect(lambda x: x[0](*x[1:]) if len(x) > 1 else x[0]())

        self.ui.tabWidget.setCurrentIndex(0)
        with open('config.yml', 'r', encoding='utf-8') as f:
            s = f.read()
            self.ui.text_config_file.setPlainText(s)
            self.config = yaml.full_load(s)
        if self.config['置顶']:
            self.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.ui.bu_top.setChecked(True)
        self.resize(self.config['窗口宽度'], self.config['窗口高度'])
        self.ui.text_subject.addItems(self.config[list(self.config.keys())[0]])

        # self.ui.text_config.addItems(list(self.config.keys())[5:]) (deprecated)
        # only show the models with url, model, key
        model_keys = []
        for k, v in self.config.items():
            if isinstance(v, dict) and {'url', 'model', 'key'} <= set(v.keys()):
                model_keys.append(k)
        self.ui.text_config.addItems(model_keys)

        self.ui.statusbar.showMessage('<token消耗> 输入 0 输出 0 <推理速度> ? tokens/s')
        self.ui.text_summary.setVisible(False)
        self.change_config()
        self.last_content = ''
        self.can_remove = True

        # add proxy option
        self.proxy = self.config.get('代理端口', None)
        if self.proxy:
            os.environ['http_proxy'] = "http://" + self.proxy
            os.environ['https_proxy'] = "http://" + self.proxy
            print("You have enabled proxy. Proxy port is: ", self.proxy)
        
        def on_press(key):
            if not self.ui.bu_switch.isChecked():
                return
            try:
                screen = QDesktopWidget().screenGeometry(self)
                X, Y = screen.width(), screen.height()
                mouse_position = mouse.Controller().position
                x, y = mouse_position
                x1, y1 = calc_window_pos(X, Y, x, y, self.width(), self.height())

                if key == keyboard.Key.esc:
                    copy_to_clipboard()
                    self.ui.tabWidget.setCurrentIndex(0)
                    sleep(self.config['复制后延迟（秒）'])
                    self.move_and_pop(x1, y1)
                    self.signal.emit((self.append_text,))
                elif key == keyboard.Key.caps_lock:
                    copy_to_clipboard()
                    self.ui.tabWidget.setCurrentIndex(1)
                    sleep(self.config['复制后延迟（秒）'])
                    self.move_and_pop(x1, y1)
                    content = clipboard.paste()
                    content = process_new_line(content)
                    self.signal.emit((self.ui.text_content.setPlainText, content))
                    self.signal.emit((self.send,))
            except AttributeError:
                pass

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()

    def move_and_pop(self, x, y):
        if not self.ui.bu_top.isChecked():
            self.move(x, y)
            self.showNormal()
            self.activateWindow()

    def send(self):
        self.ui.tabWidget.setCurrentIndex(1)
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
            try:
                ret = llm(url, key, model, prompt, query)
                time0 = time()
                for chunk in ret:
                    if len(chunk.choices) != 0 and chunk.choices[0].delta.content is not None:
                        response = chunk.choices[0].delta.content
                        if response is not None:
                            self.signal.emit((control.insertPlainText, response))
                        if self.ui.bu_scroll.isChecked():
                            self.signal.emit((control.moveCursor, QTextCursor.End))
                self.show_usage(chunk, time0)

            except Exception as e:
                self.signal.emit((control.setPlainText, str(e)))

        if len(content.split(' ')) == 1:
            Thread(target=do_translate, args=(self.ui.text_translation, word_prompt.format(content))).start()
            return
        Thread(target=do_translate, args=(self.ui.text_translation, trans_prompt.format(content))).start()
        if summary:
            Thread(target=do_translate, args=(self.ui.text_summary, summary_prompt.format(content))).start()
        self.can_remove = True

    def show_usage(self, chunk, time0):
        with lock:
            status = self.ui.statusbar.currentMessage().split(' ')
            status[2] = str(int(status[2]) + int(chunk.usage.prompt_tokens))
            status[4] = str(int(status[4]) + int(chunk.usage.completion_tokens))
            # print(time() - time0)
            status[6] = f'{int(chunk.usage.completion_tokens) / (time() - time0):.2f}'
            self.signal.emit((self.ui.statusbar.showMessage, ' '.join(status)))

    def change_summary(self):
        self.ui.text_summary.setVisible(self.ui.bu_summary.isChecked())
        if not self.ui.bu_summary.isChecked():
            self.ui.text_summary.setPlainText('')

    def change_top(self):
        self.hide()
        self.setWindowFlags(Qt.WindowStaysOnTopHint if self.ui.bu_top.isChecked() else Qt.Window)
        self.show()

    def change_config(self):
        self.ui.text_url.setText(self.config[self.ui.text_config.currentText()]['url'])
        self.ui.text_model.setText(self.config[self.ui.text_config.currentText()]['model'])
        self.ui.text_key.setText(self.config[self.ui.text_config.currentText()]['key'])

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

    def save_config(self):
        with open('config.yml', 'w', encoding='utf-8') as f:
            f.write(self.ui.text_config_file.toPlainText())
        QMessageBox.information(self, '提示', '已保存，重启后生效！')

    def closeEvent(self, event):
        msgbox = QMessageBox(QMessageBox.Question, '提示', '退出还是最小化？', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, self)
        msgbox.setDefaultButton(QMessageBox.Yes)
        msgbox.button(QMessageBox.Yes).setText('退出')
        msgbox.button(QMessageBox.No).setText('最小化')
        msgbox.button(QMessageBox.Cancel).setText('取消')
        ret = msgbox.exec_()
        if ret == QMessageBox.Yes:
            event.accept()
        elif ret == QMessageBox.No:
            event.ignore()
            self.showMinimized()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle(QStyleFactory.create('Fusion'))
    form = Form()
    form.show()
    app.exec_()
