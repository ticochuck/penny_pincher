web: gunicorn penny_pincher.wsgi:application --preload --workers 4 --log-level debug
worker: python manage.py process_tasks
