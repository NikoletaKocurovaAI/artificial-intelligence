from typing import Optional, List, Dict, Any
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import RegistrationForm, LoginForm, RegisterRobotForm, RobotDetailForm
from .models import Robot, RobotRun

"""
    MVC pattern (Model-View-Controller)

    Django's MTV:
    Model - Data from database
    Template - Data presentation
    View - Business logic
"""


def login_user(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": LoginForm()})

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("robot-run")

        else:
            return render(request, "login.html", {"form": LoginForm()})


def register_user(request):
    """
    View function for registering a new user.

    method = ['GET']
    Renders the registration form page with an empty RegistrationForm instance.

    method = ['POST']
    Validates the submitted registration form data.
        - from django.contrib.auth.forms import UserCreationForm
    If the form is valid, saves the new user and renders the login page with an empty LoginForm instance.
        - path("", LoginView.as_view(), name="login"),
        - class LoginForm(forms.Form):
    If the form is invalid, re-renders the registration form page with the validation errors and the submitted form
    data.

    :param request: HttpRequest object representing the HTTP request.
    :return: The function returns a Python response object. Django delivers converted HttpResponse object to the
    browser.
    :raises
    """

    if request.method == "GET":
        return render(request, "register.html", {"form": RegistrationForm()})

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return render(request, "registration/login.html", {"form": LoginForm()})
        else:
            return render(request, "register.html", {"form": RegistrationForm()})


@login_required
def logout_user(request):
    """
    View function for logging out a user.

     Logs out the currently authenticated user by calling Django's logout() function,
     then redirects the user to the login page.

     :param request: HttpRequest object representing the HTTP request.
     :return: HttpResponseRedirect object redirecting the user to the login page.
     :raises
    """

    logout(request)

    return redirect("custom-login")


@login_required
def show_robot_run(request):
    """
    View function for displaying a list of robot runs.

    Retrieves a list of robot runs and renders them on the 'robot_run.html' template.
    If the request method is GET, retrieves all robot runs and paginates them.
    If the request method is POST, filters the robot runs based on the selected status filter.

    :param request: HttpRequest object representing the HTTP request.
    :return: The function returns a Python response object. Django delivers converted HttpResponse object to the
    browser.
    :raises
    """

    page_number: Optional[int] = None
    robots_runs: List[Dict[str, Any]] = list()

    if request.method == "GET":
        robots_runs: List[Dict[str, Any]] = list(RobotRun.objects.filter().values())
        page_number: Optional[int] = request.GET.get("page")

    elif request.method == "POST":
        status: str = request.POST.get("selected_status_filter")

        robots_runs: List[Dict[str, Any]] = list(
            RobotRun.get_filtered_robot_runs(status=status)
        )
        page_number: int = 1

    return render(
        request,
        "robot_run.html",
        {
            "data_robots_runs": RobotRun.add_robot_name(robots_runs),
            "data_robots_names": Robot.objects.filter().values().order_by("name"),
            "data_robots_runs_statuses": RobotRun.get_robots_runs_statuses(),
            "data_robots_runs2": Paginator(robots_runs, per_page=3).get_page(
                page_number
            ),
        },
    )


@login_required
def register_robot(request):
    """
    View function for registering a new robot.

    Renders the 'register_robot.html' template with an empty RegisterRobotForm instance for GET requests.
    Processes the submitted form data to create a new robot instance for POST requests.
    If the robot name already exists, returns an error message indicating duplication.

    :param request: HttpRequest object representing the HTTP request.
    :return: The function returns a Python response object. Django delivers converted HttpResponse object to the
    browser.
    :raises
    """

    form = RegisterRobotForm()

    if request.method == "GET":
        return render(request, "register_robot.html", {"form": form})

    if request.method == "POST":
        try:
            Robot(
                name=request.POST.get("name"), motor_type=request.POST.get("motor_type")
            ).save()

            return render(request, "register_robot.html", {"form": form})

        except IntegrityError:
            return HttpResponse("You have provided the robot name that already exists.")


@login_required
def show_robot_detail(request):
    """
    View function for displaying details of a robot and handling related actions.

    Renders the 'robot_detail.html' template with details of the selected robot if a robot ID is provided via POST
    request.
    Deletes the robot with the provided name if a robot name is provided via POST request.
    Updates the next run datetime for the robot with the provided ID if a new next run datetime is provided via POST
    request.
    Redirects the user to the 'robot-run' URL after handling the actions.

    :param request: HttpRequest object representing the HTTP request.
    :return: HttpResponse object representing the HTTP response or HttpResponseRedirect object redirecting the user.
    :raises
    """

    if request.method == "POST":
        robot_detail_id = request.POST.get("robot_run_selected_robot")
        robot_to_delete = request.POST.get("robot_detail_robot_name")
        robot_next_run = request.POST.get("robot_detail_next_run_datetime")
        robot_id_next_run = request.POST.get("robot_detail_robot_id_for_next_run")

        if robot_detail_id:
            return render(
                request,
                "robot_detail.html",
                {
                    "data": Robot.get_by_id(Robot(), robot_detail_id),
                    "form": RobotDetailForm(),
                },
            )

        if robot_to_delete:
            Robot.objects.filter(name=robot_to_delete).delete()

        if robot_next_run:
            robot = Robot.objects.get(id=int(robot_id_next_run))
            robot.next_run = robot_next_run
            robot.save()

        return redirect("robot-run")
