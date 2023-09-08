# Data_CLeaning_LoBs
*(перевод на русский язык см. после английского текста)*

# Script on cleaning of historical data before uploading to relational database
Script’s purpose is cleaning of historically accumulated data before upload to relational database. Before system implementation data has been collected in Excel. Because of no controls to keyed to Excel values, data is inconsistent and requires pre-upload cleaning. Analysis detected three types of data inconsistency:
1)	Several values are keyed to one Excel cell
2)	Duplicated rows
3)	Keyed values sometimes differ from values stored in DB and cannot be recognized automatically. Preliminary data analysis also revealed that number of incorrectly keyed values is limited. A separate excel file was arranged to store mapping of misspelled values to correct ones. This file is automatically appended with new misspelled values if such are found in the uploaded dataset. 

Script prints required SQL-instructions instead of executing them in DB directly as Python is blocked because of security considerations.

# Скрипт очистки данных перед загрузкой в реляционную БД в рамках миграции исторических данных 
До введения в эксплуатацию нового функционала информация накапливалась в файлах Excel, куда вводилась вручную. Никаких контролей вводимых в excel данных предусмотрен не было. Анализ показал, что существует три вида сложностей, осложняющих загрузку:
1)	В одну ячейку в Excel введено несколько значений
2)	Записи могут быть задублированы
3)	Введенные значения отличаются от хранящихся в БД, соответственно, не могут быть распознаны автоматически. В результате анализа также было установлено, что отличающиеся от хранимых в базе введенные значения, имеют конечный (и достаточно ограниченный) набор значений. Для хранения связки пар неправильно введенных и хранящихся в базе значений создан отдельный excel файл. Данный файл при необходимости автоматически дополняется новыми значениями, если они обнаружены в загружаемом массиве. 

Скрипт только выводит в поток набор SQL-инструкций, а не исполняет их непосредственно в БД, поскольку Python был заблокирован по соображениям безопасности.
