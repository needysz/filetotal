# FILE TOTAL ( О программе )
____
"_File Total - программа для упрощенного взаймодействия с файлами и другими интеренсыми функциями_"

**Как пользоваться программой:**

**1.** В самом начале вы должны выбрать, с каким режимом будете работать. Список доступных режимов:
  * mode dub - _Dubbing mode. Режим перезаписи файлов_
  
**2. Для каждого режима выделены особые команды**

__DUBBING MODE (Режим перезаписи)__
 * Первым делом вы вводите путь к папке с файлами (path: )
 * Команда start dub - начинает перезапись файлов
 * Команда undo - отменяет перезапись
 * ( После операции перезаписи вам показывается список очищенных файлов )


# FILE TOTAL ( Версии )
____
## Alpha 0.2

✅ Об обновлении:

* Фикс бага с командами "undo" и "exit"
* Если пользователь введет неверный путь в режиме перезаписи - программа отреагирует на это верно
* Удалены ненужные части кода с конструкцией "try / except"
* Фикс бага с выходом из программы. Теперь, после выхода - консоль будет работать без ошибок

❎ Найденные недостатки / текущие недостатки:

* __Программа не зациклена. После каждой неудачной команды/выдачи ошибки - вас выкидывает из среды разработки__
* * Неправильная информация после перезаписи файлов ( mode dub )
____
## Alpha 0.1

В **Alpha 0.1** отсуствует функционал, который задумывался в начале. Вот список возможностей, плюсов и минусов:

✅ Плюсы и возможности:

* Вы можете войти в режим dubbing (перезаписи файлов) и стереть все содержимое, всех, исключительно **ТЕКСТОВЫХ** файлов
* Присутствует команда **exit** и **undo**
* После *"вхождения"* в каждый режим, вам будет показываться вся информация, которая относиться к режиму

❎ Недостатки

* Кривая работа команд **exit** и **undo** (дело в том, что они могут работать не везде)
* __Программа не зациклена. После каждой неудачной команды/выдачи ошибки - вас выкидывает из среды разработки__
* Программа, а именно - пока что единственный режим перезаписи работает только с текстовыми файлами
* Неправильная информация после перезаписи файлов ( mode dub )
