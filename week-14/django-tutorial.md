
Before you do anything below, enter the selected pre-created conda environement
by typing
```
conda activate <your_environment_name>
```

1. PostgreSQL installation, using psycopg3
   ```
   pip install "psycopg[binary]"
   ```

2. Install Django
   ```
   pip install Django 
   ```

3. Verifying
   ```py
   import django
   print(django.get_version())
   ```

## Writing your first Django app, part 1

We will create a basic poll application.
This site consists of two parts:
- A public site that lets people view pools and vote in them.
- An admin site that lets you add, change, and delete polls.

### Create a project directory
Create a directory where you store all your codes
```
./poll-site-project/
```

Enter that directory using `cd`, and type
```sh
django-admin startproject mysite
```
This will create `mysite` directory inside `./poll-site-project/` directory with the following 
structure
```
poll-site-project/
├─ mysite/
│  ├─ __init__.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ asgi.py
│  └─ wsgi.py
└─ manage.py
```


### Start server

Inside `./poll-site-project/`, start the development server
```sh
python manage.py runserver
```

Automatic reloading of `runserver`   
It might be possible when adding a new file, you have to restart the server.

### Create the Polls app

Inside `./poll-site-project/`, (the same directory
with `manage.py`), create the Polls app by entering
this command
```sh
python manage.py startapp polls
```
This will create the following directory structure
```
poll-site-project/
├─ mysite/
├─ polls/
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations/
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  └─ views.py
└─ manage.py
```

### Write your first view
This will be your "Hello World!" for Django app.

Open file `polls/views.py`, and put the following code

**`polls/view.py`**
```py
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, world. You're at the polls index.)
```

To call this view (`polls/view.py`), we need to map
it to a URL - as for this we need a URLconf (see
[URL dispatcher](https://docs.djangoproject.com/en/4.2/topics/http/urls/) for the complete explanation).

Create a file `urls.py` inside `polls` directory.
This file will serve as URLconf for `polls` app.
Add the following code to that file.

**`polls/urls.py`**
```py
from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
]

```
This will set a URLconf in app level.

If we run our program at this moment, it won't show
anything. This is because we have not set the
URLconf in our project level. In `mysite/urls.py`, 
insert the following command

**`mysite/urls.py`**
```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  path("polls/", include("polls.urls")),
  path("admin/", admin.site.urls),
]
```

Run again the server with the following command
where the terminal is inside the director `poll-site-project`
```sh
python manage.py runserver
```

We will the following result


## Writing your first Django app, part 2