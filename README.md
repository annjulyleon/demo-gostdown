# Demo Gostdown

Это демонстрационный проект для фреймворка документирования на Gostdown/Mkdocs и python скриптах. 

## Требования

- 📥[pandoc](https://github.com/jgm/pandoc/releases/) 2.18;
- 📥 pandoc-crossref 📥[0.3.13.0](https://github.com/lierdakil/pandoc-crossref/releases/tag/v0.3.13.0) для pandoc 2.18;
- 📥[python](https://www.python.org/downloads/) (tested 3.10);
- 📥[Gostdown](https://gitlab.iaaras.ru/iaaras/gostdown);
- 📥[mkdocs-material](https://squidfunk.github.io/mkdocs-material/getting-started/);
- 📥[mkdocs-bibtex](https://pypi.org/project/mkdocs-bibtex/);
- скачать и установить шрифты [PT Serif, PT Sans и PT Mono](https://www.paratype.ru/public/).

## Workflow

Полный воркфлоу на примере тестового репозитория.

1. Запустить файл `\docs_gost\build-docs.bat`. Убедиться, что в .bat файле указаны правильные пути к вашей установленной среде Python. Скрипт автоматически скопирует файлы картинок, чтобы в документе все правильно отобразилось.
2. Убедиться, что в директории `\docs_gost` появились файлы `report.pdf`, `report.docx`. Файл `report_example.docx` -- для примера.
3. Открыть `.docx` файл и запустить последовательно макросы: FigCapAutoNum, FigReferenceAutoInsert, TblCapAutoNum, TblReferenceAutoInsert. Эти макросы должны быть предварительно сохранены в шаблон `Normal.dot` (см. `\scripts_and_macros\word_macros.txt`).
4. Убедиться, что в документе теперь есть автоматическая нумерация.

Теперь делаем веб-доку:

1. Запустить скрипт `stripper.py` с командного файла `\scripts_and_macros\run_stripper.bat`. Убедиться, что в .bat файле указаны правильные пути к вашей установленной среде Python.
2. Убедиться, что в корне `demo_gostdown` создана директория `docs`.
3. Из корня `demo_gostdown` запустить `mkdocs_serve.bat`. Предварительно, убедитесь, что в `activate.bat` в переменной `VIRTUAL_ENV` указан путь к виртуальной среде с установленным mkdocs и нужными плагинами (например, `set VIRTUAL_ENV=D:\virtualenv\mkdocs\.venv`). Плагины перечислены `mkdocs.yml`.
4. В консоли отобразится процесс запуска и в конце будет выведен адрес для подключения (`http://127.0.0.1:8000/`). Открыть адрес в браузере и полюбоваться на документацию.
5. Завершить исполнение командного файла (`Ctrl + C`).
6. Запустить `mkdocs_build.bat`. В корневой директории появится собранная веб-документация в папке `\site`. Пример собранной веб-доки в `\site_example`.

