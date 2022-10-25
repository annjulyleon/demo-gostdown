## Пишем markdown с gostdown

Все возможные примеры, которые вам могут понадобиться есть в репозитории Gostdown в файле [демке](https://gitlab.iaaras.ru/iaaras/gostdown/-/blob/master/demo-main.md), и файле [pdf](https://gitlab.iaaras.ru/iaaras/gostdown/-/jobs/14344/artifacts/file/demo-report.pdf) (как это все отображается). 

Ниже я описала операции, которые мне нужны чаще всего.

### Настройка обработки

В самом первом обрабатываемом файле .md (в данном случае это `report-beginning.md`) должен быть блок с настройками обработки файлов. Вот как он выглядит:

```text
---
chapters: false
figureTitle: Рисунок
tableTitle: Таблица
tableEqns: true
titleDelim: "&nbsp;–" 
link-citations: true
linkReferences: true
csl: gost-r-7-0-5-2008-numeric-iaa.csl
bibliography: sources.bib
...
```

Это стандартный блок для любых отчетов, можете смело его использовать без изменений. Из важных настроек тут:

- `csl` -- название файла со стилем списка литературы (должен быть в корне);
- `bibliography` -- название файла со списком литературы.

Если у нас не отчет, а просто дока (гост 19, 34), то шапка будет вот такой:

```text
---
chapters: false
figureTitle: Рисунок
tableTitle: Таблица
tableEqns: true
titleDelim: "&nbsp;–" 
link-citations: true
linkReferences: true
...
```

### Нумерация заголовков

Ничего особенного для этого делать не нужно, заголовки первого уровня (`#`) становятся заголовками `Заголовок 1`.
Это нужно помнить, когда какой-то раздел разбиваете на несколько файлов.

### Рисунки

Вот как выглядит вставка рисунка в обычном markdown:

```text
![Пример полносвязной нейронной сети](_img/rcg_fcnn.png)
```

А вот так нужно сделать, чтобы получился gostdown. Обратите внимание, что пробел перед `{#fig:fully_connected_neural_network}` отсутствует (если будет пробел -- то скрипт будет ругаться, что на нашел куда ссылаться).

```text
![Пример полносвязной нейронной сети](_img/rcg_fcnn.png){#fig:fully_connected_neural_network}
```

А вот ссылка на рисунок выше в тексте:

```text
Изначально использовались полносвязные нейронные сети (англ. fully connected), 
то есть сети, в который каждый нейрон с одного слоя связан со всеми нейронами 
следующего слоя (см. рисунок [-@fig:fully_connected_neural_network]).

![Пример полносвязной нейронной сети](_img/rcg_fcnn.png){#fig:fully_connected_neural_network}
```

Чтобы Gostdown понимал, как обращаться с рисунками, необходимо чтобы все ссылки на рисунки были указаны относительно `.bat` и `.ps1` (командного файла, который собирает доку).

Рассмотрим структуру:

```text
/docs
-- /_img
---- some_image.png
-- example.md
build.bat
build.ps1
```

В `example.md` присутствует ссылка на рисунок: 

```text
Вот какой-то красивый рисунок [-@fig:some_image_id]`.

![Красивый рисунок](_img/some_image.png){@fig:some_image_id}
```

В этом случае `build.ps1` не найдет картинку, так как будет искать папку `_img` относительно себя любимого, а не относительно файла `example.md`. Чтобы картинка отобразилась, нужно сделать вот так:

```text
/docs
-- example.md
/_img
--some_image.png
build.bat
build.ps1
```

Вот, теперь скрипт сможет найти картинку. Если хочется, чтобы картинке отображались и в редакторе, то можно папки с картинками дублировать вот так:

```text
/docs
-- /_img
---- some_image.png
-- example.md
/_img
---some_image.png
build.bat
build.ps1
```

Теперь скрипт сможет все собрать, и картинки отобразятся в редакторе.

### Таблицы

Название таблицы пишем через строку после нее вот так вот:

```markdown
| Заголовок | Заголовок | Заголовок |
|--------------|--------------|--------------|
|Ячейка 1|Ячейка 2|Ячейка3|

Table: Название таблицы {#tbl:table_id}
```

Обратите внимание на пробел после названия.
Ссылаемся также, как и для рисунков.

```markdown
Информация в таблице [-@tbl:table_id].

| Заголовок | Заголовок | Заголовок |
|--------------|--------------|--------------|
|Ячейка 1|Ячейка 2|Ячейка3|

Table: Название таблицы {#tbl:table_id}
```

### Источники

Все источники записываются в файл `.bib` в корне проекта. Я чаще всего использую два типа BibTex: article и online. Пример файла bibtex приложен репозитории.

```text
# онлайн источник. Обратите внимание на "note = russian", обязательно добавляйте его в онлайн источники.
@online{rcg_ntw_intel,
  author  = {{Корпорация Intel}},
  title   = {{Что такое машинное зрение?}},
  url     = {https://www.intel.ru/content/www/ru/ru/manufacturing/what-is-machine-vision.html},
  note    = {russian},
  urldate = {2022-02-18}
}

# Статья. Если "note = russian" не добавить, то все названия для этого источника в списке литературы будут на английском (например, Том = Volume, С. - Pages и т.ж.)
# По ГОСТ по хорошему английские источники должны быть на английском (то есть "note = russian" добавлять не нужно), но иногда заказчики ругаются, так что можно и добавить.

@article{beh_survey2,
  author = {Zamini, Mohamad and Hasheminejad, Seyed Mohammad Hossein},
  year = {2019},
  month = {04},
  title = {A comprehensive survey of anomaly detection in banking, wireless sensor networks, social networks, and healthcare},
  note    = {russian},
  journal = {Intelligent Decision Technologies}
}
```

Чтобы сослаться на любой источник в тексте, нужно указать его вот так: `[@beh_survey2;@rcg_ntw_intel]`.
