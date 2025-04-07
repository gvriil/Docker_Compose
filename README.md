# Проект онлайн-обучения

## Запуск проекта через Docker Compose

### Шаг 1: Настройка переменных окружения
1. Создайте файл `.env` в корне проекта на основе шаблона:
   ```
   cp .env.sample .env
   ```
2. При необходимости отредактируйте значения в файле `.env`

### Шаг 2: Запуск проекта
Выполните команду:
```
docker-compose up -d
```

### Шаг 3: Проверка работоспособности сервисов

#### Бэкенд
- API доступно по адресу: http://localhost:8000/api/
- Админка: http://localhost:8000/admin/

#### PostgreSQL
```
docker-compose exec db psql -U postgres -d online_learning
```

#### Redis
```
docker-compose exec redis redis-cli ping
```
Должен ответить: `PONG`

#### Celery
```
docker-compose exec celery celery -A config inspect active
```

#### Celery Beat
```
docker-compose logs celery-beat
```
