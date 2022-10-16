web: gunicorn Rmash.wsgi
web: python manage.py migrate && gunicorn Rmash.wsgi
web: python manage.py collectstatic && gunicorn Rmash.wsgi