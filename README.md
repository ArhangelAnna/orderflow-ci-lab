# OrderFlow — CI Audit Lab (расширенная версия)

Учебный сервис управления заказами: каталог, расчёт стоимости, скидки, доставка,
учёт остатков, импорт поставщиков, пользователи, аналитика, отчёты и HTTP API.
Код намеренно содержит дефекты **разных типов**, часть из которых проявляется
только в граничных сценариях и не обнаруживается существующими unit-тестами.
Проект не предназначен для реального использования или публичного размещения как сервиса.

## Быстрый старт

Требуется Python 3.11 или новее.

```bash
python -m pip install -e '.[dev]'
python -m pytest -q
ruff check src
semgrep scan --config rules/orderflow.yml --error --metrics=off src
```

В Windows PowerShell при установке можно использовать `python -m pip install -e ".[dev]"`.
Если нужен только запуск unit-тестов: `python -m pip install pytest`.

### HTTP API

```bash
python -m pip install -e .
python -m orderflow.web
```

Адрес: `http://127.0.0.1:8765/health`.

Маршруты сохранены: `/health`, `/api/products`, `/api/inventory`,
`/api/export`, `/api/orders/search`, `/api/quote`.

## Состав

- `catalog.py`, `models.py`: каталог товаров
- `orders.py`, `fulfillment.py`: оформление и резервирование
- `promotions.py`, `shipping.py`: скидки и доставка
- `storage.py`: SQLite
- `accounts.py`: учётные записи и права
- `imports.py`: импорт файлов и документов
- `reporting.py`, `analytics.py`: отчёты
- `audit.py`: журнал аудита
- `web.py`: HTTP API
- `rules/orderflow.yml`: учебные правила Semgrep
- `.github/workflows/ci.yml`: тесты, Ruff и Semgrep

## Задача студента

Создать Fork, выполнить первый CI, исследовать предупреждения, подтвердить проблемы
в контексте приложения, исправить минимум три **разных** дефекта и представить PR.
Не отключайте правила, тесты, workflow или проверки; исправляйте причины замечаний.

Важно: зелёные тесты не доказывают отсутствия ошибок. По желанию добавьте тест
на граничный случай или проверку сохранения бизнес-инвариантов.
