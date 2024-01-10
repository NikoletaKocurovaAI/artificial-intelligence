from django.shortcuts import render
from django.http import JsonResponse

from .tests.testing_data import ROBOT, ROBOT_RUN


def login(request):
    return render(request, template_name="index.html")

def register(request):
    my_data = {'key1': 'value1', 'key2': 'value2'}
    return JsonResponse(my_data)


def get_list(request):
    # all, by status
    return JsonResponse(ROBOT_RUN[0])


def get_one(request):
    return JsonResponse(ROBOT[0])
