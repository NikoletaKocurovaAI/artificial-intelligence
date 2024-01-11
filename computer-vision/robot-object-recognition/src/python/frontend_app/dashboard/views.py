from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

from .crud import Crud
from .forms import RegistrationForm

crud_api = Crud()


def login_user(request):
    """
    This ..

    :param request:
    :return:
    :raises
    """
    form = RegistrationForm()

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        # user = authenticate(request, username=username, password=password)
        # if user
        # login(request, user), return robot_run.html

        return render(request, "login.html", {"form": form})

    return render(request, "login.html", {"form": form})


#login required
def register_user(request):
    """
    This ..

    :param request:
    :return:
    :raises
    """
    # request.POST data passed via form
    # user = form.save() stores data into DB
    # if form.is_valid()

    return render(request, template_name="register.html")


# login required
def logout_user(request):
    #logout(request)

    return redirect("login")


# login required
def show_robot_run(request):
    """
    This ..

    :param request:
    :return:
    :raises
    """
    robot_run = crud_api.get_list(status="COMPLETED")
    robot = crud_api.get_one(id="1")

    # if not.user.is_authenticated
    # Add id to html "{% url 'robot-detail' item.id %}"

    return render(request, "robot_run.html", {"data_robot_run": robot_run, "data_robot": robot})


#@login_required
def register_robot(request):
    """
    This ..

    :param request:
    :return:
    :raises
    """
    # html calls on submit create_one
    # if form is valid
    # name = form.cleaned_data["name"]
    # motor_type = form.cleaned_data["motor_type"]
    # robot = Robot(
    # robot.save()
    # else redirect register robot

    return render(request, "register_robot.html")


# login required
def show_robot_detail(request):
    robot = crud_api.get_one(id="1")

    return render(request, "robot_detail.html", {"data": robot})
