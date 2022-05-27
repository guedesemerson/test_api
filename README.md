# Test Api

## Steps

### Execute web service
You can get started building this application locally.

### Building with docker
```bash
docker-compose up
docker-compose exec web python manage.py migrate
```

### Testing Height filtering:
```bash
Example: http://127.0.0.1:8000/v1/exame/list_exame?altura__gt=1.80
```