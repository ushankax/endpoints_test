# Автотесты эндпоинтов с сайта httpbin.org

Тестовое задание для компании "Озон".

### В работе использовал:
* Python 3.9 (pytest + requests)
* Travis CI

### Есть два варианта проверки работоспособности тестов:
1. Результаты работы тестов в последней сборке на разных версиях Python (3.6, 3.9) доступны в Travis CI [по ссылке](https://app.travis-ci.com/github/ushankax/ozon_httpbin_test_task/builds/231704334).
2. Чтобы убедиться локально, потребуется клонировать репозиторий, установить Python и зависимости к нему (pip install -r requirements.txt), после чего применить команду 'pytest' в директории проекта.

## Тест кейсы:
### Кейсы для эндпоинта /status/:code (POST-запросы)
#### 1. Проверка на корректность возвращаемого HTTP-статуса в ответе при указании существующего HTTP-кода.
Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем POST-запрос на адрес https://httpbin.org/status/:code, где :code - существующий статус HTTP.
2. Проверяем, какой HTTP-статус вернулся в ответе.

Функция для воспроизведения: tests/test_status_endpoint.py::test_status_post_request_returns_correct_response_status_code

Ожидаемый результат: Вернулся тот HTTP-статус, который мы передаем в запросе на месте :code.
Фактический результат: Есть 5 существующий HTTP-статусов, которые отрабатывают некорректно:
1. Попытка передать 100-й запрос возвращает ConnectionError;
2. Коды 301, 302, 303 и 307 возвращают 404-й код ошибки.

#### 2. Проверка, что возвращается 502-я ошибка в случае передачи в запросе несуществующих не трехзначных HTTP-статусов.
Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем POST-запрос на адрес https://httpbin.org/status/:code, где :code - несуществующий не трехзначный статус HTTP (например, 9 или 99).
2. Проверяем, какой HTTP-статус вернулся в ответе.

Функция для воспроизведения: tests/test_status_endpoint.py::test_status_post_request_with_incorrect_code_returns_502

Ожидаемый результат: Возвращается 502-я ошибка.
Фактический результат: Возвращается 502-я ошибка.

#### 3. Проверка, что возвращается 502-я ошибка в случае передачи в запросе несуществующего трехзначного HTTP-статуса.
Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем POST-запрос на адрес https://httpbin.org/status/:code, где :code - несуществующий трехзначный статус HTTP (например, 999).
2. Проверяем, какой HTTP-статус вернулся в ответе.

Функция для воспроизведения: tests/test_status_endpoint.py::test_status_post_request_with_incorrect_3_digit_code_returns_502

Ожидаемый результат: Возвращается 502-я ошибка.
Фактический результат: Возвращается ответ с несуществующим HTTP-статусом (например, 999).

#### 4. Проверка, что возвращается 400-я ошибка в случае передачи в запросе текста вместо HTTP-статуса.
Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем POST-запрос на адрес https://httpbin.org/status/:code, где :code - текст, который не переводится в тип данных int (например, 'text_code').
2. Проверяем, какой HTTP-статус вернулся в ответе.

Функция для воспроизведения: tests/test_status_endpoint.py::test_status_post_request_with_text_status_code_returns_400

Ожидаемый результат: Возвращается 400-я ошибка.
Фактический результат: Возвращается 400-я ошибка.

#### 5. Проверка, что возвращается 404-я ошибка, если ничего не передать в поле :code.
Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем POST-запрос на адрес https://httpbin.org/status/:code, где в :code ничего не передается, т.е.: 'https://httpbin.org/status/'.
2. Проверяем, какой HTTP-статус вернулся в ответе.

Функция для воспроизведения: tests/test_status_endpoint.py::test_status_post_request_with_empty_status_code_returns_404

Ожидаемый результат: Возвращается 404-я ошибка.
Фактический результат: Возвращается 404-я ошибка.

#### 6. Проверка работоспособности рандомного возврата кода в случае передачи в запросе нескольких кодов в задуманном формате.
Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем POST-запрос на адрес 'https://httpbin.org/status/:code1,:code2', где :code1 и :code2 - существующие HTTP-статусы.
2. Проверяем, какой HTTP-статус вернулся в ответе.

Функция для воспроизведения: tests/test_status_endpoint.py::test_status_post_request_with_two_status_codes_returns_one_of_them_in_response

Ожидаемый результат: Возвращается один из двух указанных в запросе HTTP-статусов.
Фактический результат: Возвращается один из двух указанных в запросе HTTP-статусов.

#### 7. Проверка работоспособности рандомного возврата кода в случае передачи в запросе нескольких кодов вместе с весом кода в задуманном формате.
Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем POST-запрос на адрес 'https://httpbin.org/status/<code1>:<weight1>,<code2>:<weight2>', где code1 и code2 - существующие HTTP-статусы, а weight1 и weight2 - их вес.
2. Проверяем, какой HTTP-статус вернулся в ответе.

Функция для воспроизведения: tests/test_status_endpoint.py::test_status_post_request_with_two_codes_and_weights_returns_correct_response_status_code

Ожидаемый результат: Возвращается один из двух указанных в запросе HTTP-статусов.
Фактический результат: Возвращается один из двух указанных в запросе HTTP-статусов.

#### 8. Проверка, что возвращается 400-й код ошибки в случае запроса всего одного кода вместе с его весом.
Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем POST-запрос на адрес https://httpbin.org/status/<code>:<weight>, где code1 - существующий HTTP-статус, а weight1 - его вес.
2. Проверяем, какой HTTP-статус вернулся в ответе.

Функция для воспроизведения: tests/test_status_endpoint.py::test_status_post_request_with_only_code_and_weight_returns_400

Ожидаемый результат: Возвращается 400-я ошибка.
Фактический результат: Возвращается 400-я ошибка.

#### 9. Проверка, что передаваемый в запросе вес HTTP-статуса работает корректно.
Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Создаем словать для учета количества вернувшихся HTTP-статусов после запроса из шага 2. Словарь состоит из двух существующих HTTP-статусов, предусмотренных для тестирования. Например, 200 и 300.
2. Отправляем POST-запрос на адрес 'https://httpbin.org/status/<code1>:<weight1>,<code2>:<weight2>', где code1 и code2 - существующие предусмотренные HTTP-статусы, а weight1 и weight2 - их вес, причем weight1 значительно больше weight2.
3. Проверяем, какой HTTP-статус вернулся в ответе.
4. Увеличиваем счетчик на единицу в пользу HTTP-статуса, который вернулся.
5. Повторяем цикл со второго шага 10 раз.

Функция для воспроизведения: tests/test_status_endpoint.py::test_weight_in_status_post_request_works_correct

Ожидаемый результат: Чаще возвращается тот HTTP-статус, чей вес был больше.
Фактический результат: Чаще возвращается тот HTTP-статус, чей вес был больше.

### Кейсы для эндпоинта /headers (GET-запросы)
#### 1. Проверка, что корректный GET-запрос возвращает 200-й ответ.
Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем GET-запрос на адрес 'https://httpbin.org/headers'
2. Проверяем, какой HTTP-статус вернулся в ответе.

Функция для воспроизведения: tests/test_headers_endpoint.py::test_headers_response_correct_status_code

Ожидаемый результат: Возвращается 200-й HTTP-статус.
Фактический результат: Возвращается 200-й HTTP-статус.

#### 2. Проверка, что корректный GET-запрос возвращает ожидаемое содержимое в ответе.
Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем GET-запрос на адрес 'https://httpbin.org/headers'
2. Проверяем, какой HTTP-статус вернулся в ответе.
3. Если вернулся 200-й статус, то проверяем, какое вернулось содержимое ответа.

Функция для воспроизведения: tests/test_headers_endpoint.py::test_headers_response_returns_headers_content

Ожидаемый результат: Возвращается json с заголовками, внутри которого есть содержимое.
Фактический результат: Возвращается json с заголовками, внутри которого есть содержимое.

#### 3. Проверка, что корректный GET-запрос корректно возвращает заголовки, указанные нами вручную.
Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Подготавливаем несколько созданных вручную заголовков, чтобы передать в запросе ('User-Agent', 'Content-Type', 'Accept-Language', 'Referer')
2. Отправляем GET-запрос на адрес 'https://httpbin.org/headers' с созданными заголовками.
3. Проверяем, какой HTTP-статус вернулся в ответе.
4. Проверяем, что за содержимое вернулось в ответе.

Функция для воспроизведения: tests/test_headers_endpoint.py::test_headers_response_correctly_returns_custom_headers

Ожидаемый результат: В ответе вернулись, в том числе, созданные нами заголовки.
Фактический результат: В ответе вернулись, в том числе, созданные нами заголовки.

#### 4. Проверка, что в ответе возвращается правильный тип данных, даже если мы запрашиваем другой. 
Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Подготавливаем созданный вручную заголовок, чтобы передать в запросе ('Content-Type': 'text/plain')
2. Отправляем GET-запрос на адрес 'https://httpbin.org/headers' с созданным заголовком.
3. Проверяем, какой HTTP-статус вернулся в ответе.
4. Проверяем, какой вернулся тип данных в ответе.

Функция для воспроизведения: tests/test_headers_endpoint.py::test_headers_response_returns_correct_content_type

Ожидаемый результат: В ответе вернулся 'Content-Type': 'application/json'.
Фактический результат: В ответе вернулся 'Content-Type': 'application/json'.

### Кейсы для эндпоинта /redirect/:n (GET-запросы)
#### 1. Проверка, что корректный GET-запрос с одним перенаправлением возвращает 302-й ответ.

Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем GET-запрос на адрес 'https://httpbin.org/redirect/:n', где :n - число редиректов. Указываем значение :n = 1.
2. Проверяем, какой вернулся HTTP-статус.

Функция для воспроизведения: tests/test_redirect_endpoint.py::test_get_request_request_makes_one_redirect_correctly

Ожидаемый результат: Возвращается 302-й ответ.
Фактический результат: Возвращается 404-й ответ.

#### 2. Проверка, что корректный GET-запрос с двойным перенаправлением возвращает 302-й ответ.

Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем GET-запрос на адрес 'https://httpbin.org/redirect/:n', где :n - число редиректов. Указываем значение :n = 2.
2. Проверяем, какой вернулся HTTP-статус.

Функция для воспроизведения: tests/test_redirect_endpoint.py::test_get_request_request_redirects_more_than_one_times_correctly

Ожидаемый результат: Возвращается 302-й ответ.
Фактический результат: Возвращается 404-й ответ.

#### 3. Проверка, что возвращается 404-й статус, если отправить GET-запрос с нулевым количеством редиректов.

Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем GET-запрос на адрес 'https://httpbin.org/redirect/:n', где :n - число редиректов. Указываем значение :n = 0.
2. Проверяем, какой вернулся HTTP-статус.

Функция для воспроизведения: tests/test_redirect_endpoint.py::test_get_request_request_doesnt_work_with_0_redirects

Ожидаемый результат: Возвращается 404-й ответ.
Фактический результат: Возвращается 404-й ответ.

#### 4. Проверка, что возвращается 404-й статус, если отправить GET-запрос без передачи количества редиректов.

Необходимо для воспроизведения:
1. Python 3.9;
2. Установленные библиотеки: pytest, requests.

Действия для воспроизведения:
1. Отправляем GET-запрос на адрес 'https://httpbin.org/redirect/:n', где :n - число редиректов. Значение :n не указываем, т.е. такой запрос: 'https://httpbin.org/redirect/'.
2. Проверяем, какой вернулся HTTP-статус.

Функция для воспроизведения: tests/test_redirect_endpoint.py::test_get_request_request_doesnt_work_without_number_of_redirects

Ожидаемый результат: Возвращается 404-й ответ.
Фактический результат: Возвращается 404-й ответ.