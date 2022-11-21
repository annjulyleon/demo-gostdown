# Служебные скрипты

## copy_img

Получает все изображения из указанной директории 1 и субдиректорий и копирует их в директорию 2 (без иерархии). Дополнительный флаг удаляет скопированные картинки из директории 2. Документация вызывается флагом `--help`.

Запуск:

```console
python .\copy_img.py -s "..\docs" -d "..\docs\_img" -с
```

где:

- `-s` - путь, откуда будем брать картинки
- `-p` - путь, куда будем копировать
- `-c` - флаг, что надо скопировать

Взять из файла copied_files.json пути и удалить файлы с этими путями.

```console
python .\copy_img.py -r
```

Добавить в bat:

1. Перед сборкой вызываем скрипт с флагом -c.
2. После сборки вызываем скрипт с флагом -r.

Получаем минимум дублирования, плюс лишние файлы удаляться не будут. Пример вызова из bat:

```console
@echo off
python %~dp0\..\scripts_and_macros\copy_img.py -s "..\docs" -d "..\docs\_img" -c
@echo on
```

## stripper.py

Скрипт для всех документов .md в указанной папке убирает теги Gostdown.

Пример запуска:

```console
python .\stripper.py -s docs_gost -d docs -i -i *.png *.bat *.ps1 *.lua end.md begin.md
```

- `-s`, `--source` - директория, которую копируем
- `-d`, `--destination` - название директории, куда копируем
- `-i`, `--ignored` - список игнорируемых файлов и расширения, передаются списком через пробел

## acterm_list_maker.py

Вспомогательный скрипт для автоматизации создания списков сокращений и терминов. Процесс работы записывает в лог-файл.

### Workflow

1. В тексте выделяем нужный текст сокращения, нажимаем `Ctrl + Shift + A` (acronym).
Для быстрого поиска аббревиатур по тексту используем регулярное выражение: `\w*[A-ZА-Я][A-ZА-Я\d]+\w*`.
2. Выделенный текст добавляется в файл `abbreviations.txt` в директории проекта.
3. В тексте выделяем нужный текст термина, нажимаем `Ctrl + Shift + T` (term).
4. Выделенный текст добавляется в файл `glossary.txt` в директории проекта.
5. Повторяем 1-4 для всех нужных сокращений и терминов. Получается два файла.
Файлы можно упорядочить по алфавиту в VScode (Выделить весь текст > Ctrl + Shift + p > Sort Lines Asc...).
6. Дубликаты можно удалить в VScode (Выделить весь текст > Ctrl + Shift + p > Delete Duplicated lines...).
7. Запускаем скрипт `acterm_list_maker.py` с параметрами для терминов или сокращений, в параметрах также указываем словари. Словарей может быть несколько, рекомендуемый порядок применения: словарь проекта, специальный словарь (например, `ml.dic` - термины машинного обучения), общий словарь.
8. Получаем на выходе файл `abbreviations.md` или `glossary.md` со списком сокращений/расшифровок и терминов/определений в формате таблицы markdown (или в формате mkdocs) без шапки.

### VScode

В VSCode в `tasks.json` проекта добавляем две таски:

```json
{
            "label": "add_acronym",
            "type": "shell",
            "options": {
                "cwd": "${workspaceFolder}" 
            },
            "command": "echo '${selectedText}' >> abbreviations.txt",
            "presentation": {
                "echo": false,
                "reveal": "silent",
                "focus": false,
                "panel": "shared",
                "showReuseMessage": false,
                "clear": true,
                "close": true
            },
            "promptOnClose": false,
            "group": {
                "kind": "none",
                "isDefault": false
            },
            "problemMatcher": []
        },
        {
            "label": "add_term",
            "type": "shell",
            "options": {
                "cwd": "${workspaceFolder}" 
            },
            "command": "echo '${selectedText}' >> glossary.txt",
            "presentation": {
                "echo": false,
                "reveal": "silent",
                "focus": false,
                "panel": "shared",
                "showReuseMessage": false,
                "clear": true,
                "close": true
            },
            "promptOnClose": false,
            "group": {
                "kind": "none",
                "isDefault": false
            },
            "problemMatcher": []
        }
```

В VScode идем в File > Preferences > Keyboard Shortcuts. Откроется список горячих клавиш. В правом верхнем углу нажать маленькую кнопку Open Keyboard Shortcuts (JSON). Откроется JSON с пользовательскими кнопками. Добавить в файл в массив кнопки:

```json
{
        "key": "ctrl+shift+a",
        "command": "workbench.action.tasks.runTask",
        "when": "editorTextFocus",
        "args": "add_acronym" 
    },
    {
        "key": "ctrl+shift+t",
        "command": "workbench.action.tasks.runTask",
        "when": "editorTextFocus",
        "args": "add_term" 
    }
```

Все, теперь в VSCode термины и сокращения можно добавлять в отдельный файл.

### Скрипт

Скрипту `acterm_list_maker.py` нужен один лишний пакет: `chardet` для работы с кодировкой файла (bat создает кривой файл). 

Пример запуска для обработки `abbreviations.txt`:

```console
python .\acterm_list_maker.py -i "abbreviations.txt" -d "acronyms/project.dic,acronyms/common.dic,acronyms/ml.dic" -o "abbreviations.md"
``` 

Пример запуска для обработки `glossary.txt`:

```console
python .\acterm_list_maker.py -i "glossary.txt" -d "glossary/project.dic,glossary/common.dic,glossary/ml.dic" -o "glossary.md" 
```

Предусмотрено несколько словарей (в аргументе можно передать список). Каждый словарь - dictionary, где key - термин, value - определение. Рекомендуется сначала передавать скрипту словарь проекта, затем словарь предметной области, затем общий словарь.

```json
{
    "АРМ": "автоматизированное рабочее место",
    "БД": "база данных",
    "ВМ": "виртуальная машина" 
}

{
    "маппинг": "определение соответствия данных между потенциально различными семантиками одного объекта или разных объектов" 
}
```

## md_creator.py

Создает иерархию папок и файлов .md с содержимым из конфигурационного файла .json.

Запустить скрипт командой: 

```console
python .\md_creator.py
```

По умолчанию будет создана директорий из конфига `md_creator_config.json` с родительской папкой `docs_gost`. 

Чтобы указать свои параметры, запустить скрипт командой:

```console
python .\md_creator.py -cf "md_creator_config.json" -fn "docs"
```
