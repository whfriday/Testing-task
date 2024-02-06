Перед непосредственным написанием тестов, мною была изучена вся структура программы с целью понимания её работы. 

Были установлены и изучены такие необходимые библиотеки для её работоспособности как : **_Streamlit, Earth Engine_**.

Изучена работа модулей: **_GEOJSON, Mock, Requests_**.


**Для выполнения задания тестирования были написаны тесты:**
* request_test.py
* cloud_test.py
* app_test.py
* data_test.py
* make_test.py

*В папке src/enum/global_enum содержатся маркеры валидации ошибок ко всем тестам.

***_configuration.py_** содержит в себе URl адрес сервиса.
## request_test.py
В этом тестировании проверяется работоспособность сервера.

Проверяем код ответа HTTP-статуса(если 200 - сервер работает)
>assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

Также при изменении атрибута _response.---_ можно получить различную информацию от сервера. 

Например, прописанный 
>_response.headers_

возвращает заголовки сервера, которые он вернул во время ответа.

Работа теста:
![](pictures/тест1.png)
## cloud_test.py
В этом тестировании проверяется работоспособность кода из файла _cloud.py_ - получение данных с клика по карте и работы библиотеки Earth Engine.


Проверка инициализации и аутентификации  Earth Engine.
>_def mock_st_secrets():_


Проверка получения параметров _sand, clay, orgc, elev, diurnal_.
>def test_get_data():

При первоначальном запуске теста получался конфиликт версий библиотеки _Altair_
![](pictures/тест2_1.png)

Из-за чего пришлось прописать в _requirments.txt_

![](pictures/тест2_2.png)

После чего данная ошибка была устранена

Результатом работы данного теста является отсутствие файла _secrets.toml_ необходимого для инициализации _Earth Engine_.

![](pictures/тест2_3.png)

Ошибка инициализации EE

![](pictures/тест2_4.png)

И как следствие - оба непройденных теста

![](pictures/тест2_5.png)


## app_test.py


## data_test.py

В этом тестировании проверяется работоспособность кода из файла _data_analysis.py_ - подсчёт данных и поиск максимально приближённого региона.

Проверка заполнения таблиц полученными данными
>def test_queried_df(): и def test_calculate_soil_mean():

Проверка функции подсчёта данных и выбора наилучшего региона
>def test_comparison():

Проверка функции перевода в проценты и заполнения таблицы данными в JSON формате
>def test_make_queried_json():

Результатом работы теста также является ошибка с отсутствием фала ключа

![](pictures/тест3.png)

## make_test.py
