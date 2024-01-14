"""frontend_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from dashboard.views import login_user, show_robot_run, show_robot_detail, register_user, logout_user, register_robot, read_data_test


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_user, name="login"),
    path("register", register_user, name="register"),
    path("logout", logout_user, name="logout"),
    path("robot-run", show_robot_run, name="robot-run"),
    path("robot-detail", show_robot_detail, name="robot-detail"),  # TODO: robot-detail/<int:robot_id>
    path("register-robot", register_robot, name="register-robot")
]
