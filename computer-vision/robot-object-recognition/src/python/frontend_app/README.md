# Robot Object Recognition Dashboard


## Project set-up

Generate the dashboard subdirectory.

`python manage.py startapp dashboard`

The dashboard is an application folder. The project collects one or more applications. Example: by making a project of 
an on-line store, it could be divided into an application sales, blog and application contact.

Add 'dashboard' to INSTALLED_APPS variable in the dashboard/settings.py folder.

## Start
Start the application server:

`python manage.py runserver`

## Migations

Run the migration every time the change is made to the models.py file. Create migration script:

`python manage.py makemigrations`

Apply migration script:

`python manage.py migrate`

## Tests

Run tests:

`python manage.py test`