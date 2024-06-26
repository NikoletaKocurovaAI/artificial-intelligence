# Robot Object Recognition Dashboard


## Project set-up

### Required packages

Navigate to this directory:
```
cd artificial-intelligence/computer-vision/robot-object-recognition/src/python/frontend_app/
```

Create virtual environment for Mac OS:

```
virtualenv frontend-app-venv
```

#### Activate

Activate virtual environment for Mac OS:

```
source ./frontend-app-venv/bin/activate
```

Install required packages:

```
pip install -r requirements.txt
```

### Create New APP
Generate the dashboard subdirectory.

```
python manage.py startapp <app-name>
```

The <app-name> is an application folder. The project collects one or more applications. Example: by making a project of 
an on-line store, it could be divided into an application sales, blog and application contact.

Add <app-name> to INSTALLED_APPS variable in the <app-name>/settings.py folder.

### Start the Dashboard APP
Start the application server:

```
python manage.py runserver
```

### Migrations

Run the migration every time the change is made to the models.py file. Create migration script:

```
python manage.py makemigrations
```

Apply migration script:

```
python manage.py migrate
```

## Endpoints

- **Endpoint: ""**
- **Method**: [GET, POST]
- **Desciption**: This endpoint is not implemented in the **views.py** file like the other endpoints. It uses the Django's **LoginView.as_view()**,
which is set in the **urls.py** file. The corresponding template is defined within the **templates/registration** directory. Upon successful user login, 
the redirection is configured to follow the endpoint specified in the **LOGIN_REDIRECT_URL** variable within the **settings.py** file.

## Create user

### Super user

```
python manage.py createsuperuser
```

- **Username**: admin
- **Email address**: nikoletakocurovaai@gmail.com
- **Password**: admin

The admin panel is available under the url http://127.0.0.1:8000/admin.

### User

Login details:

- **Username**: UserName1
- **Email address**: nikoletakocurovaai@gmail.com
- **Password**: PassWord25*

Permission group: User1 (employee) permission group

- **Username**: UserName2
- **Email address**: nikoletakocurovaai@gmail.com
- **Password**: PassWord52*

Permission group: User2 (supervisor) permission group

## Tests

Run tests:

```
python manage.py test
```

```
python manage.py test dashboard.tests.test_model.ModelUnitTestCase.test_robot_run_model_created_successfully
```

## CSS

This is for production:

```
python manage.py collectstatic
```