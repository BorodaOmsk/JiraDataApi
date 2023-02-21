import sys
import requests
import qdarktheme
import urllib3
import keyring
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg
from PyQt6 import QtCore as qtc

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class SettingsWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Settings')
        self.setFixedSize(350, 320)

        self.url = qtw.QLabel(
            text='Url:',
        )

        self.url_text_edit = qtw.QLineEdit(
            placeholderText='https://domain.ru/',
        )
        # self.url_text_edit.move(100, 120)

        self.username = qtw.QLabel(
            text='Username:',
        )

        self.username_text_edit = qtw.QLineEdit(
            placeholderText='Jira username',
        )

        self.username_error = qtw.QLabel(
        )

        self.password = qtw.QLabel(
            text='Password:',
        )

        self.password_text_edit = qtw.QLineEdit(
            placeholderText='Jira password',
            echoMode=qtw.QLineEdit.EchoMode.Password

        )

        self.password_show = qtw.QPushButton(
            'Show password',
            clicked=self.show_password_click

        )

        self.test_connection_button = qtw.QPushButton(
            'Test connection',
            clicked=self.test_connection
        )

        self.save_button = qtw.QPushButton(
            'Save',
            clicked=self.save_password
        )


        self.closed_button = qtw.QPushButton(
            'Closed',
            clicked=self.close
        )

        self.choosing_theme_text = qtw.QLabel(
            text='Сhoosing theme:',
        )

        self.error_interpretation = qtw.QLabel()
        # text_eror = self.setLayout(qtw.QLabel())

        self.choosing_theme = qtw.QComboBox()
        self.choosing_theme.addItems(qdarktheme.get_themes())
        self.choosing_theme.currentTextChanged.connect(qdarktheme.setup_theme)

        self.setLayout(qtw.QGridLayout())
        self.layout().addWidget(self.url, 0, 0)
        self.layout().addWidget(self.url_text_edit,0,1)
        self.layout().addWidget(self.username, 2, 0)
        self.layout().addWidget(self.username_text_edit , 2, 1)
        self.layout().addWidget(self.password , 3, 0)
        self.layout().addWidget(self.password_text_edit, 3, 1)
        self.layout().addWidget(self.password_show, 3, 2)
        self.layout().addWidget(self.test_connection_button, 4, 0)
        self.layout().addWidget(self.save_button, 4, 1)
        self.layout().addWidget(self.closed_button, 4, 2)
        self.layout().addWidget(self.choosing_theme_text, 5, 0)
        self.layout().addWidget(self.choosing_theme, 5, 1)
        # self.layout().addWidget(self.error_interpretation, 6, 1)
        self.password_shown = False

    def show_password_click(self):
        if not self.password_shown:
            self.password_shown = True
            self.password_text_edit.setEchoMode(qtw.QLineEdit.EchoMode.Normal)
            self.password_show.setText('Hide  Password')

        else:
            self.password_shown = False
            self.password_text_edit.setEchoMode(qtw.QLineEdit.EchoMode.Password)
            self.password_show.setText('Show Password')


    def test_connection(self):
        url_text = self.url_text_edit.text()
        username_text = self.username_text_edit.text()
        password_text = self.password_text_edit.text()
        auth = (username_text, password_text)

        while url_text == '' or username_text == '' or password_text == '':
            if url_text == '':
                self.url.setStyleSheet('background-color: red;')
                self.url_text_edit.setFocus()
                print('Заполните поле Url')
                break
            elif username_text == '':
                self.username.setStyleSheet('background-color: red;')
                self.username_text_edit.setFocus()
                print('Заполните поле Username')
                break
            elif password_text == '':
                self.password.setStyleSheet('background-color: red;')
                self.password_text_edit.setFocus()
                print('Заполните поле Password')
                break
        else:
            self.test_connection_button.setStyleSheet('background-color: green;')

# Отлавливаем ошибки
        try:
            response = requests.post(url_text, auth=auth, verify=False)
            response.raise_for_status()
            if response.status_code == 200:
                self.test_connection_button.setStyleSheet('background-color: green;')
                self.url.setStyleSheet('background-color: black;')
                self.username.setStyleSheet('background-color: black;')
                self.password.setStyleSheet('background-color: black;')

        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
            self.test_connection_button.setStyleSheet('background-color: red;')
            self.error_interpretation.setText("Http Error:" + str(errh))

        except requests.exceptions.ConnectionError as errc:
            self.test_connection_button.setStyleSheet('background-color: red;')
            self.error_interpretation.setText("Error Connecting:" + str(errc))

            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            self.test_connection_button.setStyleSheet('background-color: red;')
            self.error_interpretation.setText("Timeout Error:" + str(errt))

            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            self.test_connection_button.setStyleSheet('background-color: red;')
            print("Error:", err)
            self.error_interpretation.setText("Error:" + str(err))

    def save_password(self):
        url = self.url_text_edit.text()
        user = self.username_text_edit.text()
        password = self.password_text_edit.text()
        while url == '' or user == '' or password == '':
            if url == '':
                self.url.setStyleSheet('background-color: red;')
                self.url_text_edit.setFocus()
                print('Заполните поле Url')
                break
            elif user == '':
                self.username.setStyleSheet('background-color: red;')
                self.username_text_edit.setFocus()
                print('Заполните поле Username')
                break
            elif password == '':
                self.password.setStyleSheet('background-color: red;')
                self.password_text_edit.setFocus()
                print('Заполните поле Password')
                break
        else:
            self.save_button.setStyleSheet('background-color: green;')
            keyring.set_password('Jira Data', user, password)


class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()
        qdarktheme.setup_theme('auto')

        self.setWindowTitle('Jira Data')
        self.setFixedSize(250, 260)
        self.settings_button = qtw.QPushButton(
            'Setings',
            clicked=self.settings_click
        )
        self.custom_fields_button = qtw.QPushButton(
            'CustomFields',
            # clicked=self.edit_messages
        )
        self.issue_type_button = qtw.QPushButton(
            'IssueType',
            # clicked=self.edit_messages
        )
        self.statuses_button = qtw.QPushButton(
            'Statuses',
            # clicked=self.edit_messages
        )
        self.project_button = qtw.QPushButton(
            'Project',
            # clicked=self.edit_messages
        )

        self.help_button = qtw.QPushButton(
            'Help',
            # clicked=self.edit_messages
        )

        self.setLayout(qtw.QVBoxLayout())
        self.layout().addWidget(self.settings_button)
        self.layout().addWidget(self.custom_fields_button)
        self.layout().addWidget(self.issue_type_button)
        self.layout().addWidget(self.statuses_button)
        self.layout().addWidget(self.project_button)
        self.layout().addWidget(self.help_button)
        self.show()

    def settings_click(self):
        self.settings_click = SettingsWindow()
        # self.settings_click.set_messages(self.message_a, self.message_b)
        # self.settings_click.submitted.connect(self.update_messages)
        self.settings_click.show()



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())