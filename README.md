# docker-flask-app

Итоговый проект курса "Машинное обучение в бизнесе"

Стек:
- ML: sklearn, pandas, numpy
- API: flask


- Data: kaggle - https://www.kaggle.com/datasets/uciml/adult-census-income
- Задача: бинарная классификация - предсказать, превышает ли доход пользователя 50 000$, или нет.
- Используемые признаки:
    * age - int
    * workclass - obj
    * fnlwgt - int
    * education - obj
    * education.num - int
    * marital.status - obj
    * occupation - obj
    * relationship - obj
    * race - obj
    * capital.gain - int
    * capital.loss - int
    * hours.per.week - int
    * income - целевая переменная
    

- Модель: градиентный бустинг

### Клонирование репозитория и создание образа

```csharp
    $ git clone https://github.com/Porfiryeva/docker-flask-app.git
    $ cd docker-flask-app
    $ docker build -t porfiryeva/docker-flask-app .
```

### Запуск контейнера
app/models/pipeline.dill - предобученная модель

<local_path_to_models> нужно заменить на полный путь к локальному каталогу.

```csharp
    $ docker run -d -p 8180:8180 -v <local_path_to_models>:/app/app/models porfiryeva/docker-flask-app
```

### Переход на localhost:8180


app/models/Client.ipynb - проверка работоспособности

app/models/Model_Pipeline.ipynb - Pipeline и предобучение модели

app/models/pipeline.dill - предобученная модель
