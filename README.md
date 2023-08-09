# DjangoCarSales

The purpose of creating this project was to use Django Style Guide and search with Elasticsearch search engine
## project setup


1- SetUp venv
```
virtualenv -p python3.10 venv
source venv/bin/activate
```

2- install Dependencies
```
pip install -r requirements_dev.txt
pip install -r requirements.txt
```

3- create your env
```
cp .env.example .env
```

4- Create tables
```
python manage.py migrate
```

6- creat bulk car object
```
python manage.py shell
from car_sales.cars.blogic.services import create_bulk_car
create_bulk_car(number_of_objects) 1000
```



