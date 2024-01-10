from django.shortcuts import render

from .tests.testing_data import ROBOT, ROBOT_RUN


def login(request):
    return render(request, template_name="login.html")


def register(request):
    return render(request, template_name="register.html")

def get_list(request):
    # all, by status
    return render(request, "robot_run.html", {"data_robot_run": ROBOT_RUN, "data_robot": ROBOT})


def get_one(request):
    return render(request, "robot_detail.html", {"data": ROBOT[1]})
