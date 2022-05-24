# Test Api

## Steps

### Execute web service
You can get started building this application locally.

### Building Locally


### This project requires
```bash
* virtualenvwrapper, pyenv virtualenv or virtualenv for local development
* python >= 3.8
* Install [Python](https://www.python.org/downloads/)
```
### Running application: You can download the project dependencies with:

```bash
pip install -r requirements.txt
python manage.py migrate
```

###Optional 
register an administrator locally:
```bash
python manage.py createsuperuser
```
### Run your application locally:
```bash
python manage.py runserver
```

### Testing Height filtering:
```bash
Example: http://127.0.0.1:8000/v1/exame/list_exame?altura__gt=1.80
```