## Установка тулчейна

Итак, чтобы вся эта красота заработала нам нужно установить:

- pandoc и плагин к нему pandoc-crossref;
- python;
- gostdown;
- mkdocs;
- скачать и установить шрифты [PT Serif, PT Sans и PT Mono](https://www.paratype.ru/public/). Можно и без них, если в шаблоне gostdown измените шрифт на тот, что нравится.

В репозитории вот здесь представлен демо-проект с текстом вот этой статьи, на котором можно ставить эксперименты и проверять, что и как работает (или не работает :)). 
Также для автоматической установки pandoc и pandoc-crossref нужных версий мой коллега @[nicky1038](https://github.com/nicky1038) написал скрипт `install-toolchain.ps1` (также лежит в репозитории).

### Pandoc

[Pandoc](https://pandoc.org/) -- это универсальная утилита для работы с текстовыми форматами. Основная сфера применения -- форматирование математических и технических текстов, говорит нам Википедия. Pandoc удобно использовать для конвертирования между форматами, например, docx в markdown и наоборот.

1. Установить 📥[pandoc](https://github.com/jgm/pandoc/releases/). На момент написания статьи последняя версия -- 2.18 (релиз 04.04.2022), именно эту версию я использую.
2. Скачать 📥[pandoc-crossref](https://github.com/lierdakil/pandoc-crossref/releases). Я использую версию 📥[0.3.13.0](https://github.com/lierdakil/pandoc-crossref/releases/tag/v0.3.13.0) для pandoc 2.18. Нужно иметь в виду, что последняя версия gostdown была выпущена год назад, так что с новыми версиями pandoc и pandoc-crossref могут быть ошибки. Стабильная версия: pandoc [2.17.1](https://github.com/jgm/pandoc/releases/tag/2.17.1) и pandoc-crossref [v0.3.12.1a](https://github.com/lierdakil/pandoc-crossref/releases/tag/v0.3.12.1a). Короче говоря, можете ставить версии pandoc 2.18 и pandoc-crossref 0.3.13.0, а если возникнут ошибки -- в первую очередь попробовать старую версию. У меня пока ошибок не было.
3. Распаковать pandoc-crossref в папку pandoc: `%localappdata%\Pandoc` (положить туда exeшник).
4. Проверить версию pandoс (и что он правильно прописался в PATH). Пуск > Поиск > powershell > запустить Powershell. В powershell ввести команду:

```console
pandoc --version

pandoc.exe 2.18
Compiled with pandoc-types 1.22.2, texmath 0.12.5, skylighting 0.12.3,
citeproc 0.7, ipynb 0.2, hslua 2.2.0
Scripting engine: Lua 5.4
User data directory: C:\Users\Anna\AppData\Roaming\pandoc
Copyright (C) 2006-2022 John MacFarlane. Web:  https://pandoc.org
This is free software; see the source for copying conditions. There is no
warranty, not even for merchantability or fitness for a particular purpose.
```

### Python

Python нам понадобится, чтобы использовать mkdocs (который написан на Python и js) и вспомогательные скрипты. Ну и вообще, Python везде пригодится. Все в этой статье написано для Python 3.10.
Ставится Python очень просто: загрузите 📥[инсталлятор](https://www.python.org/downloads/) с сайта и запустите. Не снимайте галочку с опции про прописать путь в PATH.

Проверьте, что все установилось:

```console
python --version
```

Чтобы не городить огород из библиотек, предлагаю сразу использовать виртуальную среду. Виртуальная среда для Python позволяется вам устанавливать все нужные пакеты в отдельную папку, и из нее запускать обособленный экземпляр Python. Это еще удобно тем, что если что-то пошло не так, то не нужно переставлять весь питон, искать способы переустановки библиотек, а можно просто снести папку и сделать все заново.

Все команды выполняем в PowerShell консоли:

1. Создать папку для нашего mkdocs.
2. Открыть созданную папку, кликнуть Shift + ПКМ по пустой папке и выбрать «Открыть окно PowerShell» здесь.
3. Выполнить команду: `python -m venv .venv`. В папке будет создана директория .venv со средой исполнения Python.
4. Чтобы выполнять команды в этой среде, устанавливать сюда пакеты и вообще с ней работать, нужно её активировать. Не забывайте про это! Выполните: `.\.venv\Scripts\activate`.

Должно получиться вот так. В скобках указана наша виртуальная среда, все команды теперь выполняем тут.

```console
PS D:\virtualenv\mkdocs> .\.venv\Scripts\activate
(.venv) PS D:\virtualenv\mkdocs>
```

### Gostdown

Gostdown не нужно устанавливать, достаточно скачать код из 📥[официального репозитория](https://gitlab.iaaras.ru/iaaras/gostdown).
Вы получите кучу файлов и папок, давайте разберемся, что где и зачем (таблица [-@tbl:gd_files_description]).

| Что | Зачем |
| -----| ----- |
|`demo-report-beginning.md`|это пример начала отчета, здесь есть пример списка исполнителей, список терминов, определений, реферат, введение|
|`demo-report-end.md`|это пример заключительного файла с заключением, списком источников и приложениями|
|`demo-template-espd.docx`|**обязательный файл** -- это файл-шаблон, хоты бы один такой файл должен быть в проекте. Скрипт использует этот файл, чтобы к тексту применять стили. Не меняйте названия стилей. Вы можете отредактировать этот файл (например, добавить титул, добавить рамки, поменять лист регистрации, добавить что угодно до или после `%MAINTEXT%` < именно сюда будет вставлен текст|
|`demo-template-report.docx`|аналогично -- файл-шаблон, но для отчета, а то был для ГОСТ 19|
|`drracket-screenshot.png`|просто картинка пример|
|`gost-r-7-0-5-2008-numeric-iaa.csl`|это файл стилей для списка источников. Если в проекте есть список источников, должен быть в директории проекта|
|`iaa-logo.emf`|еще один пример картинки|
|`linebreaks.lua`|обязательный файл -- разрывы в коде, должен быть в проекте|
|`lunokhod-expo.jpg`|еще одна картинка, пример|
|`oc-plot.emf`|еще одна картинка, пример|
|`build.ps1`|обязательный файл -- это и есть основной скрипт, который творит всю магию|
|`build-demo-espd.bat`|это командный файл, который запускает ps1 с аргументами. В аргументах указывается какой шаблон использовать (template.docx), нужно включать шрифты в файл, нужно ли делать pdf и, самое главное, -- список md файлов в том порядке, котором хотим их видеть в результирующем docx|
|`build-demo-report.bat`|просто еще один пример командного файла|
|`build-docs.bat`|хотя бы один такой файл должен быть обязательно в проекте (ну, если вы не хотите вручную команды вводить|
|`demo.bib`|это список источников в формате BibTex. Обязательно должен быть в проекте, если хотите на что-то ссылаться|
|`demo-espd-beginning.md`|просто пример markdown начала для ГОСТ 19|
|`demo-espd-end.md`|просто окончания markdown начала для ГОСТ 19|
|`demo-main.md`|это основной текст. Хотя бы один md должен быть в проекте|
|`demo-report.pdf`|пример собранного отчета. docx получается большой, если включена в bat опция embedfont|

Table: Описание файлов {#tbl:gd_files_description}

**Обязательно загляните в demo-report.pdf и demo-main.md!** Там есть все инструкции, как писать какие-то штуки в markdown (например, таблицы, ссылки на рисунки, формулы) и как оно будет выглядеть в результирующем файле.

### (Optional) Mkdocs

Mkdocs библиотеки:

- 📥[mkdocs-material](https://squidfunk.github.io/mkdocs-material/getting-started/)
- 📥[mkdocs-bibtex](https://pypi.org/project/mkdocs-bibtex/)

В нашей виртуальной среде выполняем команды:

```console
pip install mkdocs-material
pip install mkdocs-bibtex
```

🌐[Настройки](https://squidfunk.github.io/mkdocs-material/creating-your-site/#configuration) проекта хранятся в файле `mkdocs.yml`.