import os
import sys
from dotenv import load_dotenv

"""
    These settings in a Django project are related to internationalization (i18n) and localization (l10n) as well as 
    timezone handling.

    LANGUAGE_CODE
    Specifies the default language for the project. If the user's preferred language matches one of the languages 
    supported by your application, Django will attempt to display content in that language if translations are 
    available.

    TIME_ZONE
    Specifies the default timezone for the project. In this case, "UTC" indicates Coordinated Universal Time. Django 
    will use this timezone for internal time representations and operations unless overridden.

    USE_I18N
    A boolean that specifies whether Django should enable internationalization support. When set to True, Django will 
    use translation files and tools to translate text and localize formats in templates and forms.

    USE_L10N
    A boolean that specifies whether Django should enable localization support. When set to True, Django will use 
    localization features such as formatting dates, numbers, and currency according to the user's locale.

    USE_TZ
    A boolean that specifies whether Django should use timezone-aware datetime objects. When set to True, Django will 
    use timezone support, converting naive datetimes to the project's timezone specified in TIME_ZONE.
"""
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""
    In a Django project, the STATIC_ROOT setting is used to specify the directory where Django will collect all static files 
    from various apps in your project during the process of deployment. These static files can include things like CSS, 
    JavaScript, images, etc.
    
    MEDIA_URL: Similar to STATIC_URL, this setting specifies the base URL for serving media files (e.g., user-uploaded 
    files such as images, videos) in your Django application.
"""
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

"""
    The SECRET_KEY setting in Django is a cryptographic key used for securing session data, CSRF tokens, password 
    hashing, and other security-related mechanisms in your Django application.
"""
SECRET_KEY = "ch)nsa_%cl4q06som9p94n0l6rgi#-9-tek3&ap**rarsn-o^("

"""
    Turn off the debug on production.
    Allowed hosts value can be set to "127.0.0.1".
    
    ALLOWED_HOSTS: Specifies a list of host/domain names that are allowed to access your Django application. This 
    setting helps prevent HTTP Host header attacks and should be configured with the appropriate hostnames for your 
    deployment environment.
"""
DEBUG = True
ALLOWED_HOSTS = []

"""
    "django.contrib.admin"
    This application provides an admin interface that allows authorized users to manage and interact with the data 
    models of your Django application. 
     
    "django.contrib.auth"
    This application provides authentication and authorization functionalities for your Django project. It includes user
    authentication (login, logout, password management), permissions, groups, and other related features.
    
    "django.contrib.contenttypes"
    This application provides generic relations between models in your Django project. It allows you to create 
    relationships between different types of content without having to define the relationship explicitly in your 
    models.
    
    "django.contrib.sessions"
    This application provides session management for your Django project. It allows you to store and retrieve 
    user-specific data across multiple requests and interactions with your website.
    
    "django.contrib.messages"
    This application provides a messaging framework for your Django project. It enables you to display messages to 
    users (e.g., success messages, error messages, informational messages) and manage them easily within your views.
    Example:
    messages.success(request, 'Your profile was updated successfully.')
    These messages can be displayed in your Django templates using the {{ messages }} template variable.
    
    "django.contrib.staticfiles"
     Provides a framework for managing static files such as CSS, JavaScript, images, and other assets in your Django 
     project. It simplifies the process of serving static files during development and collecting them for deployment.
"""
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "dashboard",
]


"""
    "django.middleware.security.SecurityMiddleware"
    This middleware helps you manage various security features in your Django application, such as setting security 
    headers, mitigating clickjacking attacks, and enabling browser XSS filtering.
    XSS stands for Cross-Site Scripting, which is a common security vulnerability in web applications. 
    
    "django.contrib.sessions.middleware.SessionMiddleware"
    This middleware enables session support in your Django application. It manages session data for each user, 
    allowing you to store and retrieve user-specific information across multiple requests.
    
    "django.middleware.common.CommonMiddleware"
    This middleware provides various common functionalities, such as URL rewriting (e.g., adding a trailing slash to 
    URLs), setting the X-Content-Type-Options header, and removing the Content-Length header for streaming responses.
    
    "django.middleware.csrf.CsrfViewMiddleware"
    This middleware provides protection against Cross-Site Request Forgery (CSRF) attacks. It ensures that forms 
    submitted within your application contain a CSRF token, which helps verify the authenticity of the requests.
    
    "django.contrib.auth.middleware.AuthenticationMiddleware"
    This middleware is responsible for associating users with requests. It adds the user attribute to the request 
    object, representing the currently authenticated user (if any).
    
    "django.contrib.messages.middleware.MessageMiddleware"
    This middleware enables the support for messages framework in your Django application. It allows you to display 
    messages to users (e.g., success messages, error messages) and manage them across multiple requests.
    
    "django.middleware.clickjacking.XFrameOptionsMiddleware"
    This middleware helps prevent clickjacking attacks by setting the X-Frame-Options header in HTTP responses. It 
    specifies whether a browser should be allowed to render a page in a frame or iframe.
"""
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "frontend_app.urls"

"""
    This part of a Django settings file configures the template engine used by Django for rendering HTML templates.
    
    BACKEND: Specifies the backend template engine to be used.
    DIRS: A list of directories where Django should look for template files. If this list is empty ([]), Django will 
    only look for templates within the directories of installed Django apps.
    APP_DIRS: A boolean value indicating whether Django should also search for templates within the templates 
    directories of installed Django apps. 
    
    context_processors
    They are responsible for injecting commonly used variables into templates, such as the current user (request.user), 
    messages from the django.contrib.messages framework, etc.
"""
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

"""
    The WSGI_APPLICATION setting in Django specifies the entry point for the WSGI (Web Server Gateway Interface) 
    application used to serve your Django project. WSGI is a standard interface between web servers and Python web 
    applications or frameworks like Django.
"""
WSGI_APPLICATION = "frontend_app.wsgi.application"

"""
    Test and production databases.
"""
load_dotenv()

if "test" in sys.argv:
    # print("Using the sqlite3 test db")
    # settings data ['manage.py', 'test', 'dashboard.tests.test_model.ModelUnitTestCase.test_get_robots_runs_statuses']

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR + "/" + "db.sqlite3",
        }
    }

else:
    # print("Using the production postgres db")
    # ['manage.py', 'runserver']

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "USER": os.getenv("DB_USER"),
            "NAME": os.getenv("DB_NAME"),
            "PORT": os.getenv("DB_PORT"),
        }
    }

"""
    "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    Its purpose is to check if the user's password is too similar to their username or other attributes associated with 
    the user.
    
    "django.contrib.auth.password_validation.MinimumLengthValidator"
    Its purpose is to ensure that user passwords meet a minimum length requirement.
    
    "django.contrib.auth.password_validation.CommonPasswordValidator"
    Its purpose is to check if the user's password is among a list of commonly used or easily guessable passwords.
    
    "django.contrib.auth.password_validation.NumericPasswordValidator"
    Its purpose is to ensure that user passwords contain at least one numeric character.
"""
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
