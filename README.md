# Wagtail boilerplate

Features:

- Custom user model
- JWT auth
- dj-rest-auth
- django-split-settings
- django-environ
- Django REST Framework
- Django REST Framework JSON CamelCase
- Schema generator (drf-spectacular)
- Sentry

TODO:
- I18n


## Start development

```shell
./dev.sh up
```

## Start production

```shell
docker-compose build
docker-compose up -d
```


## Default admin user 

Django admin: http://localhost:8000/django-admin/

Wagtail admin: http://localhost:8000/admin/

```
username: admin@example.com
password: ChangeMePlease!
```