## Дипломный проект. Задание 3: UI-тесты

### Автотесты для проверки сайта StellarBurgers, направленные на основной функционал

### Реализованные сценарии

Созданы UI-тесты, покрывающие функции: создания пользователя, сброса пароля, создания заказа, проверки номера заказа

Был создан Allure-отчёт (отчет: `allure_results/`)

### Структура проекта

- `allure_results` - папка, содержащая отчёты Allure.
- `tests` - пакет, содержащий тесты, разделенные по функциям. Например, `test_feed.py`, `test_main_functional.py` 
и т.д.
- `utils` - папка содержащая доп. материалы для тестов.
- `conftest` - файл содержащий фикстуры необходимые для тестов

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание Allure-отчета**

>  `$ pytest --alluredir=allure_results`
> '$ allure serve allure_results'
