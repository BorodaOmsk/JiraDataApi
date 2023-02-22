# Получаем данные из Jira DC(Server) 

## Приложение будет получать из Jira DC(Server) следующие данные:
1. CustomFields (Пользовательские поля)
2. IssueType (Типы задач)
3. Statuses (Статусы задач)
4. Project (Проекты)

## Сборка в EXE файл с помощью [Nuitka](https://github.com/Nuitka/Nuitka)  
1. Установить Nuitka: `python -m pip install nuitka` 
2. Выполнить в Terminal: `python -m nuitka --standalone --windows-disable-console --plugin-enable=pyqt6 --onefile JIraDataMainWindow.py`

***Сборка протестирована для Windows 10***



## Автор 
 [Lebedkov](https://github.com/BorodaOmsk)
