
# About

This project is a demo for django and elasticsearch.

Use the django, drf-haystack and elasticsearch．

# Usage
* first
```python
pip install -r requirements.txt
```
start mysql , elasticsearch and fill in your ip, port, user, password in d_es_demo/settings.py.
```python
python manage.py migrate
python manage.py rebuild_index
python manage.py runserver
```
http://host/users is the API to create user 

http://host/search/?keyword=??? is the API to search user
