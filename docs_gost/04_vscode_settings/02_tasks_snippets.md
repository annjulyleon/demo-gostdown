## Tasks

В VSCode можно настроить запуск кастомных тасков и скриптов. Много примеров и описание в официальной документации: https://code.visualstudio.com/docs/editor/tasks.

## Запускаем сборку документации

Кастомные таски сохраняются в директорию рабочего пространства в `./.vscode/tasks.json`. Такой файл уже есть в демонстрационном репозитории. Вы можете создать его вручную, или командой из терминала VSCode (`Ctrl`+`Shift`+`P`> Tasks: Configure Tasks > Create tasks.json file from template).

В массив `tasks` добавить вот такую задачу (дефолтную можете удалить):

```json
{
    "label": "build report",
    "type": "shell",
    "options": {
        "cwd": "${workspaceFolder}\\docs_gost"
    },
    "command": ".\\build-docs.bat",
    "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared",
        "showReuseMessage": false,
        "clear": true
    },
    "group": {
        "kind": "build",
        "isDefault": false
    }
}
```

Сохраняем. Теперь задачу можно вызвать из меню Terminal > Run Tasks... > выбрать свою таску.

## Запускаем стриппер

Для стриппера в директории `\scripts_and_macros` также есть .bat файл. Сделаем задачу и для него:

```json
{
    "label": "strip gostdown",
    "type": "shell",
    "options": {
        "cwd": "${workspaceFolder}\\scripts_and_macros"
    },
    "command": ".\\run_stripper.bat",
    "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared",
        "showReuseMessage": false,
        "clear": true
       },
    "group": {
        "kind": "build",
        "isDefault": false
        }
    }
```

Точно также можно вызывать и другие командные файлы и даже внешние программы. В демонстрационном проекте сконфигурировано 4 задачи. Проверьте только перед запуском, что в bat файлах указаны правильные пути к исполняемому файлу python.exe и виртуальной среде (для mkdocs).
