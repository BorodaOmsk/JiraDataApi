# Получам данны из Джира DC (Сервер) 
# Статус: Развивать

## Приложение будет получат из Джира ДК (Сервер), сладуущище данны:
1. CustomFields (Ползовательские поля)
2. IssueType (Типы задач)
3. Статуи (Статусы задач)
4. Проект (Проэкты)

## Сборка в EXE файл с поместю [Nuitka](https://github.com/Nuitka/Nuitka)  
1. Установить Нуитка : `питон -м пип установить нуитка` 
2. Выполни в Терминале: `python -m nuitka --standalone --windows-disable-console --plugin-enable = pyqt6 --onefile JIraData.py`

***Сборка протестирована для Windows 10***



## Автор 
 [Лебедьков](https://github.com/BorodaOmsk)
