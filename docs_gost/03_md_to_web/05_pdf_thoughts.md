## Генерация PDF

### С плагином mkdocs-with-pdf

Плагин: [mkdocs-with-pdf](https://github.com/orzih/mkdocs-with-pdf)

Установка:

- установить согласно инструкции [WeasyPring](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows) и зависимости;
- установить плагин `pip install mkdocs-with-pdf`.

*2022-05-12* Чтобы плагин не падал с ошибкой, если в доке есть диаграммы mermaid:

```console
pip install beautifulsoup4==4.9.3
pip install mkdocs-with-pdf
```

В конфигурационный файл `mkdocs.yml` добавить секцию:

```yaml
plugins:
  - with-pdf:
      cover: true
      cover_title: Дока
      toc_title: Содержание
      render_js: true
      headless_chrome_path: C:\Program Files\Google\Chrome\Application\chrome.exe
      enabled_if_env: ENABLE_PDF_EXPORT
```

См. все ключи конфигурации в [README](https://github.com/orzih/mkdocs-with-pdf). С указанной конфигурации pdf не будет генерироваться во время `mkdocs serve`. 
Чтобы сгенерировать pdf во время `mkdocs build`, необходимо указать ENV:

```PowerShell
$Env:ENABLE_PDF_EXPORT=1
mkdocs serve
```

Все страницы будут склеены в один pdf в директории `/site/pdf`.

!!! warning
    Этот плагин не умеет генерировать диаграммы mermaid (они будут отображены блоком текста).

### MkDocs PDF with JS Plugin

Плагин: [mkdjcs-pdf-with-js-plugin](https://github.com/smaxtec/mkdocs-pdf-with-js-plugin)

В этом плагине не так много настроек, зато:

- он умеет отображать mermaid диаграммы;
- может генерировать pdf для конкретной страницы, а не все сразу.

Установка:

- установить браузер Chrome, [ChromeDriver](https://chromedriver.chromium.org/) нужной версии и указать путь к ChromeDriver в `PATH`;
- добавить в секцию `plugins` конфигурационного файла ключ `- pdf-with-js`. `enable` - `true` для активации плагина.

```yaml
plugins:
    ...
    - pdf-with-js:
        enable: true
```
