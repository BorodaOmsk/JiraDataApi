# Получам данны из Джира DC (Сервер) 
# Статус: Close

## Приложение будет получат из Джира ДК (Сервер), сладуущище данные:
1. CustomFields (Ползовательские поля)
2. IssueType (Типы задач)
3. Project (Проекты)

## Сборка в EXE файл с помощью [Nuitka](https://github.com/Nuitka/Nuitka)  
1. Установить Нуитка : `питон -м пип установить нуитка` 
2. Выполни в Терминале: `python -m nuitka --standalone --windows-disable-console --plugin-enable = pyqt6 --onefile JIraData.py`

***Сборка протестирована для Windows 10***



## Автор 
 [Лебедьков](https://github.com/BorodaOmsk)
