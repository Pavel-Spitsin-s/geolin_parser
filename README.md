# Geolin parser

Этот репозиторий содержит инструмент, который парсит страницы с сайта математики ИТМО (geolin) и преобразует обработанные тензоры в объекты языка (матрицы). Затем выполняется симметризация/альтернирование тензоров и возвращается ответ в необходимом формате.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/yourrepository.git](https://github.com/Pavel-Spitsin-s/geolin_parser.git
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

## Использование

1. Обработайте тензоры и выполните симметризацию/альтернирование:

```bash
python main.py
```

2. Получите ответ в необходимом формате.

## Пример

```python
# Пример кода для обработки тензоров и выполнения симметризации/альтернирования
from parser import *

tensors = get_results()  # Загрузка тензоров после парсинга
processed_tensors = get_res(tensors)
print(beautify(processed_tensors))
```

## Вклад

Если у вас есть предложения по улучшению или исправлению проблем, пожалуйста, создайте issue или отправьте pull request.

## Лицензия
license.md
