from django.shortcuts import render
from django.http import JsonResponse

from .tests.testing_data import ROBOT, ROBOT_RUN


def login(request):
    return render(request, template_name="base.html")


def register(request):
    my_data = {"key1": "value1", "key2": "value2"}
    return JsonResponse(my_data)


def get_list(request):
    # all, by status
    return render(request, "robot_run.html", {"data": ROBOT_RUN})


def get_one(request):
    return render(request, "robot_detail.html", {"data": ROBOT[1]})
