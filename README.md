# DjangoCarSales

## project description

- پروژه تحت بستر جنگو در ارتباط با یک شرکت فروش خودرو با در نظر گرفتن تعداد حداکثر 10 میلیارد محصول (خودرو) است. 

- نام خودرو، تعداد سیلندر، تعداد سرنشین، رنگ خدرو، حجم سیلندر، نام مالک

- انتخاب دیتابیس جهت ذخیره سازی اطلاعات خودرو بر عهده شماست.

- جهت ایجاد خودرو و جستجو در لیست خودروها نیاز به Authenticate میباشد. تنها کاربرانی که جزء گروه support هستند قابلیت جستجو دارند. تکنولوژی پیاده سازی با در نظر گرفتن قابلیت اعمال بر روی API بر عهده شماست.

- ایمیل های کاربران به صورت Unique در نظر گرفته شود.

- ورود خودرو تنها توسط کاربران در گروه sale قابل انجام باشد و ممکن است چندین کاربر به صورت همزمان اطلاعات را به روز رسانی کنند.

- جستجو باید بر اساس index های انجام شده در Elastic صورت پذیرد. با توجه به نمایش نتایج از طریق API، خروجی باید برای برنامه های Front کارآمد و قابل استفاده باشد.

- جهت جستجوی خودرو نیاز به API میباشد. فیلترهایی نظیر رنگ و تعداد سیلندر و همچنین نام مالک خودرو قابل جستجو باشند.

- دیتای تست به تعداد 1000 عدد و نام کاربری مورد نیاز جهت Authenticate در هنگام تحویل پروژه مورد نیاز است.

- تست صحت عملکرد برنامه پیش از اجرا الزامیست.


## project setup


1- compelete cookiecutter workflow (recommendation: leave project_slug empty) and go inside the project
```
cd DjangoCarSales
```

2- SetUp venv
```
virtualenv -p python3.10 venv
source venv/bin/activate
```

3- install Dependencies
```
pip install -r requirements_dev.txt
pip install -r requirements.txt
```

4- create your env
```
cp .env.example .env
```

5- Create tables
```
python manage.py migrate
```

7- run the project
```
python manage.py runserver
```# django_car_sales
