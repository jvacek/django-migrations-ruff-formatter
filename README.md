# django-migrations-ruff-formatter

Patches the Django formatter to use ruff, so you don't have to ignore formatting for your migrations.

## Installation

Add to your project one way or another

```bash
uv add --dev 'django-migrations-ruff-formatter>=0.1.0'
```

or if you're living under a rock...

```bash
pip install django-migrations-ruff-formatter
```

and in your settings, add this

```python
INSTALLED_APPS = [
    # ...
    'django_migrations_ruff_formatter.apps.RuffFormatter',
]
```

## Use

Just like before:

```bash
uv run ./manage.py makemigrations
```
