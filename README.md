# Wagtail boilerplate

Features:

- django-split-settings
- django-environ
- custom user model
- Django REST Framework

- Django REST Framework JSON CamelCase
- Swagger generator
- sentry


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