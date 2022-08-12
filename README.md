# dev_amazon

FastAPI app for classification space images with human footprint on amazon forests

Можно прейти по ссылке на сервис
http://91.206.15.25:5505/docs

### Описание API
#### Примеры запросов
1) Пример запроса классов модели(Amazon Classes List):
```
curl -X 'GET' \
  'http://91.206.15.25:5505/amazon/amazon_classes' \
  -H 'accept: application/json'
```
2) Пример запроса на обработку изображения для предсказания модели(Predict)
```
curl -X 'POST' \
  'http://91.206.15.25:5505/amazon/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'image=@14613546395_15e0bd305f_o-e1447088965932.jpeg;type=image/jpeg'
```
3) Пример запроса на обработку изображения для предсказания по вероятности пренадлежности изображения к классам(Predict Proba)
```
curl -X 'POST' \
  'http://91.206.15.25:5505/amazon/predict_proba' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'image=@14613546395_15e0bd305f_o-e1447088965932.jpeg;type=image/jpeg'
```
4) Пример проверки доступности сервиса(Health Check)
```
curl -X 'GET' \
  'http://91.206.15.25:5505/amazon/health_check' \
  -H 'accept: application/json'
```

### Локальное развертывание
#### Через Python:
Установить все зависимости
``` 
make install
```
Инициализировать dvc
``` 
make init_dvc
```
Скачать актуальные веса
``` 
make download_weights
```
Запустить приложение и открыть тут http://0.0.0.0:5505/docs
``` 
make run_app
```


#### Через Docker:
Сбилдить свежий образ
``` 
make build
```
Запустить контейнер и указать id_image
``` 
docker run -d -p 5505:5505 id_image
```
после открыть http://0.0.0.0:5505/docs

Докер образ с тегом latest есть на gitlab
как спулить не знаю)
```
спулить образ с gitlab ci
``` 


### Запуск тестов:
Запуск юнит тестов
```
make run_unit_tests
``` 
Запуск интеграционных тестов
```
make run_integration_tests
``` 
Запуск всех тестов
```
make run_all_tests
``` 
Получение отчета покрытия тестами
``` 
make generate_coverage_report
```
