"""
    Is used to set up the ASGI (Asynchronous Server Gateway Interface) application for running Django in an asynchronous
    environment. ASGI is a standard interface between Python asynchronous web servers and applications.

    get_asgi_application
    This function returns the ASGI application for your Django project, which is used to handle asynchronous HTTP
    requests.

    setdefault("DJANGO_SETTINGS_MODULE", "frontend_app.settings")
    This ensures that Django knows which settings to use when running in an ASGI environment.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frontend_app.settings")

application = get_asgi_application()
