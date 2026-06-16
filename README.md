# MAISON backend

Backend для Maison Bespoke Atelier на Django + DRF.

## Локальный запуск

```bash
cd back/app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Deploy на Render

В репозитории уже подготовлены:

- `render.yaml` для Blueprint deploy
- production-настройки Django под Postgres и WhiteNoise
- `app/.env.example` с нужными переменными окружения

### Что нужно сделать в Render

1. Открыть `Blueprints` -> `New Blueprint Instance`
2. Подключить репозиторий `MAISON-Bespoke-Atelier-backend`
3. Render сам увидит `render.yaml` и создаст:
   - web service
   - PostgreSQL database
4. После первого деплоя заполнить переменные:
   - `CORS_ALLOWED_ORIGINS=https://<frontend-domain>`
   - `CSRF_TRUSTED_ORIGINS=https://<frontend-domain>`
5. Если нужен доступ в Django admin на free-плане без shell, можно временно задать:
   - `DJANGO_SUPERUSER_USERNAME`
   - `DJANGO_SUPERUSER_EMAIL`
   - `DJANGO_SUPERUSER_PASSWORD`
6. После следующего deploy backend сам создаст superuser. Затем эти переменные лучше удалить.

### Healthcheck

Проверка доступности backend:

- `/api/health/`

### Важно

- В production backend больше не зависит от `sqlite3`, если задан `DATABASE_URL`
- Статика обслуживается через WhiteNoise
- Для пользовательских загрузок в production лучше позже вынести media в S3 / Cloudinary
