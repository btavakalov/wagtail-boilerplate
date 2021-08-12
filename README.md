# Wagtail boilerplate

Features:

- Custom user model
- JWT auth
- django-split-settings
- django-environ
- Django REST Framework
- Django REST Framework JSON CamelCase
- Swagger generator
- Sentry

TODO:
- Minimalistic registration
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