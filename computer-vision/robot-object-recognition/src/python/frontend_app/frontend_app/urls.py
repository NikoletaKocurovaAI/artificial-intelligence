"""
    Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from dashboard.models import Robot, RobotRun
from dashboard.views import (
    show_robot_run,
    show_robot_detail,
    login_user,
    register_user,
    logout_user,
    register_robot,
)


"""
     Used to register Django model classes with the Django admin interface, allowing you to manage and interact with 
     instances of these models through the Django admin.
"""
admin.site.register(Robot)
admin.site.register(RobotRun)


"""
    When browser sends request HTTP to a specific URL, URL dispatcher looks for a function registered here.
    Django runs the found function with the argument request containing the data from the browser turned into a Python 
    object.
"""
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_user, name="custom-login"),
    path("register", register_user, name="register"),
    path("logout", logout_user, name="logout"),
    path("robot-run", show_robot_run, name="robot-run"),
    path("robot-detail", show_robot_detail, name="robot-detail"),
    path("register-robot", register_robot, name="register-robot"),
]
