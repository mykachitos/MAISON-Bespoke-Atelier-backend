# MAISON backend

Backend для Maison Bespoke Atelier на Django + DRF.

## Что важно перед деплоем

- Сейчас проект использует локальный `sqlite3` файл: `back/app/db.sqlite3`
- Для production лучше перейти на внешний PostgreSQL
- Для production не стоит хранить `DEBUG=True`, `ALLOWED_HOSTS=['*']` и `CORS_ALLOW_ALL_ORIGINS=True`
- Если размещать backend на Vercel, нужно адаптировать Django под Python Functions и вынести базу/медиа во внешние сервисы

## Локальный запуск

```bash
cd back/app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Рекомендуемый продакшн-стек

- Frontend: Vercel
- Backend: Render или Railway
- Database: Neon / Supabase Postgres
- Media: Cloudinary / S3 / Vercel Blob
